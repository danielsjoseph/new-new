from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
myList= [801,802,803,901,902,903]

class User(AbstractUser):
    slug = models.SlugField(null=True,blank=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True,null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_agent = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','password','is_agent']
    
    def __str__(self):
        return self.email
    def save(self, *args, **kwargs):
        self.name= f'{self.first_name} {self.last_name}'
        self.username=f'{self.first_name}{self.last_name}'
        import random
        randomC = random.randint(10000, 99999)
        self.slug = slugify(f'{self.first_name} {self.last_name} {randomC}')
        return super().save(*args,**kwargs)

from django.conf import settings 

class AgentProfile(models.Model):
    slug = models.SlugField(unique=True,null=True,blank=True)
    display_picture = models.ImageField(default='images/default.jfif', upload_to='images/')
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.IntegerField(default=123456789)
    wa_number = models.CharField(max_length=255, null=True,blank=True)

    def __str__(self):
        return self.name.name
    def save(self, *args, **kwargs):
        import random
        # user = User.objects.get(name=self.name)
        # self.slug = user.slug
        self.wa_number = f"https://api.whatsapp.com/send/?phone={self.contact}&text=Gooday%20I'm%20interested%20in%20a%20property%20you%20posted"
        return super().save(*args,**kwargs)

# @receiver(post_save,sender=User)
def createAgentProfile(sender,instance,created,**kwargs):
    if created and instance.is_agent==True:
        AgentProfile.objects.create(name=instance,slug=instance.slug)
        instance.agentprofile.save()
post_save.connect(createAgentProfile, sender=User)
 
class UserProfile(models.Model):
    slug = models.SlugField(unique=True,null=True,blank=True)
    name = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    contact= models.IntegerField(default=00000000000)
    wa_number = models.CharField(max_length=255, null=True,blank=True)

    def __str__(self):
        return self.name.name
    def save(self,*args,**kwargs):

        self.wa_number = f"https://api.whatsapp.com/send/?phone={self.contact}&text=Gooday%20Have%20you%20seen%20my%20catalogue"
        return super().save(*args,**kwargs)

def createUserProfile(sender,created,instance,**kwargs):
    if created and instance.is_agent==False:
        UserProfile.objects.create(name=instance,slug=instance.slug)
        instance.userprofile.save()
post_save.connect(createUserProfile,sender=User)

availability=[
    ("Available","Available"),
    ("Rented","Rented"),
    ("Sold","Sold"),
]
user_looking_for=[
    ("Rent","Rent"),
    ("Sale","Sale"),
]
property=[
    ('Duplex','Duplex'),
    ('Bungalow','Bungalow'),
    ('Apartment','Apartment'),
    ('Land','Land'),
]
class Apartments(models.Model):
    slug = models.SlugField(unique=True,null=True,blank=True)
    agent= models.ForeignKey(AgentProfile,on_delete=models.CASCADE)
    location = models.TextField(max_length=255)
    is_available = models.CharField(max_length=255, choices=availability)
    looking_for = models.CharField(max_length=255,choices=user_looking_for)
    property_type = models.CharField(max_length=255,choices=property)
    display_picture = models.ImageField(upload_to='images/')
    image1 = models.ImageField(null=True,blank=True)
    image2 = models.ImageField(null=True,blank=True)
    image3 = models.ImageField(null=True,blank=True)
    image4 = models.ImageField(null=True,blank=True)
    
    def save(self, *args, **kwargs):
        import random
        randomC = random.randint(10000, 99999)
        self.slug = slugify(f'{self.location} {randomC}')
        return super().save(*args,**kwargs)
    def __str__(self) -> str:
        return self.location

