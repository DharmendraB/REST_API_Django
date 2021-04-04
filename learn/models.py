from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=50)
    hod = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Notice(models.Model):
    subject = models.CharField(max_length=500)
    msg = models.TextField()
    pub_date = models.DateField(auto_now_add=False)
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True, blank=True)
    
class profile(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True, blank=True)
    sem = models.IntegerField(default=1, choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)))
    marks_10 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    marks_12 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    marks_aggr = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
    rn = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True,unique=True)
    phone = models.CharField(validators=[RegexValidator("0?^[5-9]{1}\d{9}$")],max_length=20, null=True, blank=True)    
   
    # pip install pillow==6.0.0 --user
    image = models.ImageField(upload_to="learn/images", default="")
    resume = models.FileField(upload_to="learn/doc", default="")

    def __str__(self):
        return "%s (%s)" %(self.name,self.branch)



class Question(models.Model):
    subject = models.CharField(max_length=500)
    msg = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=CASCADE, blank=True, null=True,unique=True)
    def __str__(self):
        return self.subject


