from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users Must Have An Email Address!')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.save()
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name = 'email address',
                              max_length=255,unique=True)
    is_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        '''Does The User Have A Specific Permission?'''
        #Yes
        return True
    def has_module_perms(self, app_label):
        '''Does The User Have Permissions To View The App app_label?'''
            #yes
        return True

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,
                                primary_key=True,)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    preferred_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile-images')
    fb_profile = models.CharField(max_length=100)
    github_name = models.CharField(max_length=100)
    Users = models.OneToOneField(User, on_delete=models.CASCADE, related_name="ProfileOfUser")

    LEVELS = (
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior')
    )
    current_level = models.CharField(choices=LEVELS,max_length=50)
    phone = models.IntegerField()
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'