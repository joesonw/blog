from django.db import models

class Article_class(models.Model):
    cid         = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name
    
class Article(models.Model):
    tid         = models.AutoField(primary_key=True)
    title       = models.CharField(max_length=60)
    content     = models.TextField()
    author      = models.CharField(max_length=20)
    time_stamp  = models.DateTimeField()
    comments    = models.IntegerField()
    aclass      = models.ForeignKey(Article_class)
    img         = models.CharField(max_length=256, default="/resources/images/img.png")
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-time_stamp']

class Comment(models.Model):
    cid         = models.AutoField(primary_key=True)
    content     = models.TextField(max_length=200)
    time_stamp  = models.DateTimeField()
    author      = models.CharField(max_length=20)
    ip          = models.CharField(max_length=15)
    email       = models.EmailField()
    tid         = models.IntegerField()
    class Meta:
        ordering = ['time_stamp']


