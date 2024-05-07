import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'users.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import Profile
from faker import Faker

fake = Faker()

def generate_users(num_users):
    for _ in range(num_users):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(profile_name=username, user=user)
    print('feito!')

if __name__ == '__main__':
    num_users = 100 
    generate_users(num_users)
