from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  
from django.db.models.signals import post_save 
from django.dispatch import receiver  

class Profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    genderChoices = [
        ('M', '남성'),
        ('W', '여성'),
    ]#튜플의 첫번째 요소가 저장될 값, 두번째 요소가 사람이 읽을 수 있는 이름
    gender = models.CharField(max_length=1, choices=genderChoices)
    politicalOrientation = models.IntegerField()


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()
