from django.core.management.base import BaseCommand, CommandError

from market.models import Category, Product, SubCategory
from bs4 import BeautifulSoup
import requests
from django.core.files import File
import shutil
from prj.settings import BASE_DIR

STOP_WORDS = ['ООО', 'ТОВ', 'ТД', 'ЧП', 'ТМ', 'Украин']

def get_products(cat,subcat,url):
    print('Downloading from %s' % url)
    rez = requests.get(url, verify=False)
    soup = BeautifulSoup(rez.text, 'html.parser')
    for item in soup.findAll('div', {'class': 'company_pic'}):
        img = item.find('img')
        in_stop = False
        # отсеиваем ненужное
        for w in STOP_WORDS:
            if img.get('title').find(w) > -1:
                in_stop = True
        if img.get('src').find('no_image') > -1:
            in_stop = True

        if not in_stop:
            print(img.get('title'))
            pr = Product()
            pr.category = cat
            pr.name = img.get('title')
            pr.subcategory = subcat
            img_url = 'https://gastronoma.net/%s' % img.get('src')
            img_response = requests.get(img_url, stream=True, verify=False)
            # сохраняем временный файл
            with open('tmp.png', 'wb') as out_file:
                shutil.copyfileobj(img_response.raw, out_file)
            # читаем временный файл и загружаем его программно в модель
            with open('%s/tmp.png' % BASE_DIR, 'rb') as img_file:
                pr.image.save('product.png', File(img_file), save=True)
            pr.save()


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Clearing DB')
        # удаляем записи и картинки
        Category.objects.all().delete()
        SubCategory.objects.all().delete()
        Product.objects.all().delete()
        shutil.rmtree('%s/media' % BASE_DIR)

        # достаем главную страницу и парсим
        URL = 'https://gastronoma.net'
        print('Start importing from %s' % URL)
        rez = requests.get(URL, verify=False)
        soup = BeautifulSoup(rez.text, 'html.parser')

        # находим нужный див и в нем картинки
        content = soup.find('div',{'class': 'body_20'})
        for img in content.findAll('img'):
            c = Category()
            c.name = img.get('alt')
            img_url = 'https://gastronoma.net/%s' % img.get('src')
            img_response = requests.get(img_url, stream=True, verify=False)
            # сохраняем временный файл
            with open('tmp.png', 'wb') as out_file:
                shutil.copyfileobj(img_response.raw, out_file)
            # читаем временный файл и загружаем его программно в модель
            with open('%s/tmp.png' % BASE_DIR, 'rb') as img_file:
                c.image.save('cat.png', File(img_file), save=True)
            c.save()
            # забираем подкатегории
            for subcat in img.find_parent('tr').find('div').findAll('a'):
                sc = SubCategory()
                sc.category = c
                sc.name = subcat.text
                sc.save()
                get_products(c,sc,subcat.get('href'))
            
                

        