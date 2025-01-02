from apps.common.models import TimeStampedUUIDModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
User = get_user_model()


class Gender(models.TextChoices):
    MALE = 'Male', _('Male')
    FEMALE = 'Female', _('Female')
    OTHER = 'Other', _('Other')


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

    phone_number = PhoneNumberField(verbose_name=_('Phone Number'), max_length=30, default='+918055088300')

    about_me = models.TextField(verbose_name=_('About Me'), default='Say Something About Yourself')

    license = models.CharField(verbose_name=_('Real Estate License'), max_length=20, blank=True, null=True)

    profile_photo = models.ImageField(verbose_name='Profile Photo', default=r'.\profile_default.png')
    gender = models.CharField(verbose_name=_('Gender'), choices=Gender.choices, default=Gender.MALE, max_length=20)

    country = CountryField(verbose_name=_('Country'), default='IN', blank=False, null=False)

    city = models.CharField(verbose_name=_('City'), max_length=180, default='Pune', blank=False, null=False)

    is_buyer = models.BooleanField(verbose_name=_('Buyer'), default=False,
                                   help_text=_('Are You Looking To Buy a Property?'))

    is_seller = models.BooleanField(verbose_name=_('Seller'), default=False,
                                    help_text=_('Are You Looking To Sell a Property'))

    is_agent = models.BooleanField(verbose_name=_('Agent'), default=False, help_text=_('Are You an Agent'))
    top_agent = models.BooleanField(verbose_name=_('Top Agent'), default=False)

    rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    num_reviews = models.IntegerField(verbose_name='Number of Reviews', default=0, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
