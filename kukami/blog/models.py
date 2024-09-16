from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.tag_name
    
class Post(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    publication_date =  models.DateField(_("Publication Date"),default=timezone.now())
    tags = models.ManyToManyField(Tag, blank=True, related_name="post_tags")
    
    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    name= models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True, related_name="post_comment")
    
    def __str__(self) -> str:
        return self.name
