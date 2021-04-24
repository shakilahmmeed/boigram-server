from django.dispatch import receiver
from django.db.models.signals import pre_save
from core.models import Book, Category, Author
from utils.slug_generator import unique_slug_generator


@receiver(pre_save, sender=Book)
def create_product_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, for_=instance.title)


@receiver(pre_save, sender=Category)
def create_product_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, for_=instance.title)


@receiver(pre_save, sender=Author)
def create_product_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, for_=instance.name)
