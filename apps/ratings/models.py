from apps.common.models import TimeStampedUUIDModel
from apps.profiles.models import Profile
from django.db import models
from django.utils.translation import gettext_lazy as _
from real_estate.settings.base import AUTH_USER_MODEL


# Create your models here.


class Rating(TimeStampedUUIDModel):
    class Range(models.IntegerChoices):
        Rating_1 = 1, _("Poor")
        Rating_2 = 2, _("Fair")
        Rating_3 = 3, _("Good")
        Rating_4 = 4, _("Very Good")
        Rating_5 = 5, _("Excellent")

    rater = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("User Providing The Rating"),
        on_delete=models.SET_NULL,
        null=True,
    )
    agent = models.ForeignKey(
        Profile,
        verbose_name=_("Agent Being Rated"),
        related_name="agent_review",
        on_delete=models.SET_NULL,
        null=True,
    )

    rating = models.IntegerField(
        verbose_name=_("Rating"),
        choices=Range.choices,
        help_text=_("1 = Poor, 2 = Fair, 3 = Good, 4 = Very Good, 5 = Excellent"),
        default=0,
    )

    comment = models.TextField(verbose_name=_("Comment"))

    class Meta:
        unique_together = ["rater", "agent"]

    def __str__(self):
        return f"{self.agent} rated at {self.rating}"
