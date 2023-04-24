from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cart, Customer

@receiver(post_save, sender=Customer)
def create_cart(sender, instance, created, **kwargs):
    if created:
        
        Cart.objects.create(customer=instance, total=0.00, notes='')
