from django.core.management.base import BaseCommand, CommandError

from market.models import Category, Product, SubCategory
from bs4 import BeautifulSoup
import requests
from django.core.files import File
import shutil
from prj.settings import BASE_DIR



class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Clearing DB')
        # удаляем записи и картинки
        Category.objects.all().delete()
        SubCategory.objects.all().delete()
        Product.objects.all().delete()
       