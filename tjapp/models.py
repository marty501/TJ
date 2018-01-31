from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Company(models.Model):
    Name = models.CharField(max_length=50)
    WebUrl = models.URLField(max_length=250, null=True)
    WebUrlContactUs = models.URLField(max_length=250, blank=True, default='')
    CustomerServicePhone = models.CharField(max_length=25, blank=True, default='')

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.Name)


class Station(models.Model):
    DEFAULT_PK = 1
    Name = models.CharField(max_length=100)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.Name)


class Journey(models.Model):
    Company = models.ForeignKey(Company, related_name='company_journeys')
    User = models.ForeignKey(User, related_name='user_journey')
    DepartureStation = models.ForeignKey(Station, related_name='journey_station_dep', default=Station.DEFAULT_PK)
    ArrivalStation = models.ForeignKey(Station, related_name='journey_station_arr', default=Station.DEFAULT_PK)
    DelayAtDepartureStationMins = models.PositiveSmallIntegerField()
    IsCancelled = models.BooleanField()
    ScheduledDepartureTime = models.TimeField();
    ActualArrivalTime = models.TimeField(blank=True, null=True)
    Notes = models.CharField(max_length=250, blank=True, default='')
    IsVerified = models.BooleanField()

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Dep:%s Arr:%s DELAY: %d' % (
            self.DepartureStation.Name, self.ArrivalStation.Name, self.DelayAtDepartureStationMins)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    objects = models.Manager() # The default manager
    published = PublishedManager() # Our published manager - used in the post_list view

    def get_absolute_url(self):
        return reverse('tjapp:post_detail', args=[self.publish.year,
                                                  self.publish.strftime('%m'),
                                                  self.publish.strftime('%d'),
                                                  self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

# Create your models here.
