# add a signal after creating a review

from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_review
from cine.models import Review


@receiver(post_save, sender=Review)
def send_review_task(sender, instance, created, **kwargs):
    if created:
        print('intercepted signal for Sending Review Task to Celery')
        send_review.apply_async()
