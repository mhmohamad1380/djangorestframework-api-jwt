import os
from django.db import models
from django.dispatch import receiver
from . validators import image_size_validator
from .tasks import send_mail_for_new_posts
# Create your models here.


class Food(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"


class FoodsPictures(models.Model):
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="foods", blank=False,
                                # validators=[image_size_validator]
                                )

    class Meta:
        verbose_name = "FoodsPicture"
        verbose_name_plural = "FoodsPictures"


@receiver(models.signals.pre_delete, sender=FoodsPictures)
def delete_all_image_files(sender, instance, **kwargs):
    food_relation = instance.food.id
    for image in sender.objects.all():
        if instance.picture:
            if os.path.isfile(image.picture.path):
                if image.food.id == food_relation:
                    os.remove(image.picture.path)


class Email(models.Model):
    email = models.EmailField(blank=False,unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"

@receiver(models.signals.post_save,sender=Food)
def send_mail(sender,instance,**kwargs):
    emails = list(email.email for email in Email.objects.all())
    send_mail_for_new_posts.delay(instance.title, emails)