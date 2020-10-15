import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_board.settings")
CELERY_BROKER_URL = (os.environ.get("CELERY_BROKER_URL", "redis://redis:6379"),)
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379")

app = Celery("task", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=0, minute=0), reset_upvotes.s(), name="reset all upvotes at 00:00"
    )


@app.task(name="reset upvotes task")
def reset_upvotes():
    from api_news.models import Post

    Post.objects.filter(amount_of_upvotes__gt=0).update(amount_of_upvotes=0)
