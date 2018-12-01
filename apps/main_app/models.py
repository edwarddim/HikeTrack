from django.db import models
import re
import bcrypt
from datetime import date
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

today = date.today().isoformat()
# Create your models here.
class UserManager(models.Manager):
    def registrationValidate(self, postData):
        error = {}
        #VALIDATE FIRST AND LAST NAME
        if len(postData['first_name']) < 3:
            error['first_name'] = 'Your first name must be longer than 3 characters'
        if not postData['first_name'].isalpha():
            error['first_name_alpha'] = 'Your name must only be alphabets'

        if len(postData['last_name']) < 1:
            error['last_name'] = 'Your last name must be longer than 3 characters'
        if not postData['last_name'].isalpha():
            error['last_name_alpha'] = 'Your name must only be alphabets'
        
        #VALIDATE WITH EMAIL REGEX AND CHECK FOR DUPES
        if not EMAIL_REGEX.match(postData['email']):
            error['email_format'] = 'Your email must be in valid format'
        if User.objects.filter(email=postData['email']):
            error['emaildupe'] = 'Your email is already registered'
        
        #VALIDATE PASSWORD AND CONFIRM THAT PASSWORD AND C_PASSWORD MATCHES
        if len(postData['password']) < 8:
            error['password'] = 'Your password must be longer than 8 characters'
        if postData['password'] != postData['c_password']:
            error['passwordmatch'] = 'Your password and confirm passowrd does not match'
        return error

    def loginValidate(self, postData):
        error = {}
        #VALIDATE WITH REGEX AND CHECK FOR EMAIL IN DB
        if not EMAIL_REGEX.match(postData['email']):
            error['email'] = 'Your email must be in valid format'
    
        #CHECK IF PASSWORD GIVEN MATCHES THE PASSWORD IN DB
        if not User.objects.filter(email=postData['email']):
            error['loginemail'] = 'Email does not exist within DB'
            return error
        user = User.objects.get(email=postData['email'])
        if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
            pass
        else:
            error['credentials'] = 'Your credentials do not match'
        return error

class TripManager(models.Manager):
    def overnightValidate(self,postData):
        error = {}
        #VALIDATE FOR CORRECT DATES
        if postData['end'] < postData['start']:
            error['traveldate'] = 'Your end date should be later than your start date'
        if today > postData['start']:
            error['invalidstart'] = "Your start date needs to be later than today"
        if today > postData['end']:
            error['invalidend'] = "Your end date needs to be later than today"

        #VALIDATE FOR EMPTY ENTRIES
        if not postData['end']:
            error['invalidend'] = 'Enter End Date'
        if not postData['start']:
            error['invalidstart'] = 'Enter Start Date'
        if len(postData['description']) < 1:
            error['description'] = 'You must enter a description'
        return error
    def tripValidate(self, postData):
        error = {}
        if today > postData['start']:
            error['invalidstart'] = "Your trip date needs to be later than today"
        if not postData['start']:
            error['emptystart'] = 'Enter Start Date'
        if len(postData['description']) < 1:
            error['description'] = 'You must enter a description'
        return error

class User(models.Model):
    user_level = models.PositiveSmallIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=UserManager()

class Trip(models.Model):
    planner = models.ForeignKey(User, related_name="planned_trip", on_delete=models.CASCADE)
    crew = models.ManyToManyField(User, related_name="on_trip")

    comment = models.TextField()
    trail_api_id = models.PositiveIntegerField()
    start_date = models.DateField(auto_now_add=False, auto_now=False)
    end_date = models.DateField(auto_now_add=False, auto_now=False)
    overnight = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TripManager()

class Picture(models.Model):
    uploader = models.ForeignKey(User, related_name="uploaded", on_delete=models.CASCADE)
    trippic = models.ForeignKey(Trip, related_name="trip_pic", on_delete=models.CASCADE)

    picture = models.ImageField(upload_to='uploads')
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Trail(models.Model):
    trip = models.ForeignKey(Trip, related_name="trail", on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    difficulty = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Location(models.Model):
#     trail = models.OneToOneField(Trail, related_name="location", on_delete=models.CASCADE)

#     street_num = models.PositiveIntegerField()
#     street_name = models.CharField(max_length=50)
#     street_type = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class TrailReview(models.Model):
    trail = models.ForeignKey(Trail, related_name="review", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviewd_trail", on_delete=models.CASCADE)

    comment = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
