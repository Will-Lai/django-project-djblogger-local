from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    options = (("draft", "Draft"), ("published", "Published"))
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    # usable url string, link for the individual post
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()
    # automaticall add with current time
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    # default as "draft" mode
    status = models.CharField(max_length=10, choices=options, default="draft")

    class Meta:
        # descending order
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
