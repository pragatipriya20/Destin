from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin



#****************************************

class MusicProfile(models.Model):
    genres = models.TextField(null=False, default='')
    artists = models.TextField(null=False, default='')
    popularities = models.TextField(null=False, default='')
    durations = models.TextField(null=False, default='')
    release_dates = models.TextField(null=False, default='')

class ReadingProfile(models.Model):
    pass

class AnimeProfile(models.Model):
    pass

class MoviesProfile(models.Model):
    pass

class Interests(models.Model):
    music = models.OneToOneField(MusicProfile, on_delete=models.CASCADE, null=True)
    reading = models.OneToOneField(ReadingProfile, on_delete=models.CASCADE, null=True)
    Anime = models.OneToOneField(AnimeProfile, on_delete=models.CASCADE, null=True)
    movies = models.OneToOneField(MoviesProfile, on_delete=models.CASCADE, null=True)



#*******************************************
class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('date_of_birth', '2000-01-01')
        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be a staff'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be a superuser'
            )
        return self._create_user(email, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,max_length=255,blank=False)
    is_staff = models.BooleanField('staff status',default=False)
    is_active = models.BooleanField('active',default=False)
    is_superuser = models.BooleanField('superuser',default=False)
    date_joined = models.DateTimeField('date joined',default=timezone.now)
    has_profile = models.BooleanField('has profile', default=False, null=False)
    date_of_birth = models.DateField('date of birth', null=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()
    def __str__(self):
        return self.email
    def full_name(self):
        return self.first_name + " "+ self.last_name

class UserProfile(models.Model):
    user  = models.OneToOneField(CustomUser, on_delete = models.CASCADE , null = True)
    image = models.ImageField(default ='default.jpg' , upload_to = 'profile_pic')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=200)
    age = models.IntegerField(max_length=10)
    matches = models.ManyToManyField(CustomUser , related_name= 'matched_user')
    pending = models.ManyToManyField(CustomUser , related_name= 'pending_users')
    GENDER = [
        ("M", "Male"),
        ("F", "Female"),
        ("N", "Non_binary"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER)
    sexual_orientation = models.CharField(max_length=1, choices=GENDER)
    interests = models.OneToOneField(Interests, on_delete=models.CASCADE)
     
    def __str__(self):
       return f'{self.user} Profile'







