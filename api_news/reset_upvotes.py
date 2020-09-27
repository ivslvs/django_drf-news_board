from django_cron import CronJobBase, Schedule
from .models import Post


class ResetAmountOfUpvotes(CronJobBase):
    """Reset amount of post upvotes"""

    RUN_AT_TIMES = ["00:00"]

    schedule = Schedule(run_every_mins=RUN_AT_TIMES)
    code = "news_board.api_news.reset_upvotes"

    def do(self):
        post_list = Post.objects.filter(amount_of_upvotes__gt=0)
        post_list.update(amount_of_upvotes=0)
