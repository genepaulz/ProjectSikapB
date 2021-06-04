from django.db import models
from passlib.hash import pbkdf2_sha256

# Create your models here.


class User(models.Model):
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    user_type = models.IntegerField()
    isVerified = models.IntegerField()
    companyName = models.CharField(max_length = 100)
    industry = models.CharField(max_length = 100)
    region = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)

    class Meta:
        db_table = "User"



class Posts(models.Model):
    email = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    yearsOfExperience = models.IntegerField()
    industry = models.CharField(max_length = 100)
    region = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    age = models.IntegerField()
    dateadded = models.DateField()
    isAgeViewable = models.IntegerField()
    
    class Meta:
        db_table = "Posts"

