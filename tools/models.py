import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .constants import STATUS_CHOICES

User = get_user_model()


def upload_to_aws_s3(instance, filename):
    """
    Upload images in media/tools/ dir in s3 bucket
    """
    return 'tools/' + filename


class Picture(models.Model):
    """
    Purpose: This model will be used by other models for adding images
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    image_alt_text = models.CharField('Alt Text for image', max_length=50)
    image = models.ImageField("Picture", upload_to=upload_to_aws_s3, null=True, blank=True, help_text=_('Add Image'))
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.image.name)


class Tool(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name of Tool', max_length=50)
    description = models.TextField(verbose_name='Description')
    quantity = models.IntegerField(verbose_name='Quantity', help_text='How many of these you have ?', null=True,
                                   blank=True)
    cost_per_hour = models.DecimalField(verbose_name='Cost per hour in INR.', null=True, max_digits=10, decimal_places=2)
    status = models.CharField('Status', choices=STATUS_CHOICES, max_length=40,
                              help_text=_('Is this tool available right now or not ?'), null=True, blank=True)
    images = models.ManyToManyField(Picture, help_text=_('Images of this tool.'), blank=True)
    rating = models.DecimalField(default=0.0, max_digits=10, decimal_places=1)
    total_users_rated = models.IntegerField(default=0,)
    total_stars = models.IntegerField(default=0,)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    # address fields
    state = models.CharField('State', max_length=100, null=True, blank=True)
    city = models.CharField('City', max_length=100, null=True, blank=True)
    town = models.CharField('Town/village/locality', max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tool-detail', kwargs={'pk': self.id})

    def get_reviews_url(self):
        return reverse('reviews-list', kwargs={'tool_id': self.id})
