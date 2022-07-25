import os
from django.db import models
from django.dispatch import receiver
from . validators import image_size_validator
from .tasks import send_mail_for_new_posts
# Create your models here.


class Shop(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"


class ShopPictures(models.Model):
    shop = models.ForeignKey(to=Shop, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="shop/items", blank=False,
                                # validators=[image_size_validator]
                                )

    class Meta:
        verbose_name = "ShopsPicture"
        verbose_name_plural = "ShopsPictures"


@receiver(models.signals.pre_delete, sender=ShopPictures)
def delete_all_image_files(sender, instance, **kwargs):
    shop_relation = instance.shop.id
    for image in sender.objects.all():
        if instance.picture:
            if os.path.isfile(image.picture.path):
                if image.shop.id == shop_relation:
                    os.remove(image.picture.path)


class Email(models.Model):
    email = models.EmailField(blank=False,unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"

@receiver(models.signals.post_save,sender=Shop)
def send_mail(sender,instance,**kwargs):
    emails = list(email.email for email in Email.objects.all())
    send_mail_for_new_posts.delay(instance.title, emails)