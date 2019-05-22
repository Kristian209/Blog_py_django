from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
    user                      = models.ForeignKey(User,default=1)
    title                     = models.CharField(max_length=120, unique=True)
    content                   = models.TextField()
    image                     = models.TextField(null=True, blank=True, help_text='Image url')
    publish_date              = models.DateField(null=True)
    timestamp                 = models.DateTimeField(auto_now_add = True)
    updated                   = models.DateTimeField(auto_now = True)

    def __str__(self):
       return self.title

    def get_absolute_url(self):
        return reverse("post-detail",kwargs={"id": self.id})

    class Meta:
        verbose_name          = "Blog post"
        verbose_name_plural   = "Blog posts"
        ordering              = ["-publish_date","-pk"]
