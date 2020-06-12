from django.core.management.base import BaseCommand, CommandError
from market.models import UserProfile
from django.contrib.auth.models import User



class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('Clearing users')
        User.objects.all().delete()
        user = UserProfile()
        user.username = 'admin'
        user.name = 'admin'
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.set_password('admin')
        user.save()
       