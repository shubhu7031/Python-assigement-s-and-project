from django.db import models
from django.utils import timezone
import math

# Create your models here.

choice=(("Chairman","Chairman"),("Member","Member"))

class user(models.Model):
    email = models.EmailField(unique= True,max_length=50)
    password = models.CharField(max_length = 30)
    otp = models.IntegerField(default = 459)
    role = models.CharField(max_length = 10,choices=choice)
    is_active = models.BooleanField(default=False)
    is_verfied = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self)-> str:
        return self.email


class chairman(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    block_no=models.CharField(max_length=50,null=True)
    house_no=models.CharField(max_length=50,null=True)
    about_me= models.TextField(max_length=5000,null=True)
    pic=models.FileField(default="media/images/default.png")


    def __str__(self)->str:
        return str(self.user_id)


class notice(models.Model):
    user_id= models.ForeignKey('chairman',on_delete=models.CASCADE)
    notice_title= models.CharField(max_length=75,null=False)
    notice_content= models.TextField(max_length=255,null=False)
    img=models.ImageField(upload_to="images/notice/",null=True)
    video=models.FileField(upload_to="images/notice/video/",null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self)-> str:
        return self.notice_title

    
    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


gender=(("Male","Male"),("Female","Female"))


class member(models.Model):
    member_id= models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    DOB=models.CharField(max_length=50)
    address=models.TextField(max_length=50,null=True)
    total_member=models.CharField(max_length=50)
    number_of_vehicle=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,choices=gender)
    phone=models.CharField(max_length=50)
    Email=models.EmailField(max_length=75,null=True)
    photo=models.ImageField(upload_to="images/Member",null=True, blank=True,default="images/Member/MD.jpg")
    work_info=models.TextField(max_length=500,null=True, blank=True)

    def __str__(self)-> str:
        return self.firstname
