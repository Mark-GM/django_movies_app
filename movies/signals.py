from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from iti_proj1.settings import EMAIL_HOST_USER
from .models import Movie


@receiver(post_save, sender=Movie)
def new_movie_notifier(sender, instance, created, *args, **kwargs):
    if created:
        send_mail(
            subject="New movie is released!",
            message=f"'{instance.name}' is now available!",
            from_email=EMAIL_HOST_USER,
            recipient_list=["example@example.com"],
            fail_silently=True,
        )
