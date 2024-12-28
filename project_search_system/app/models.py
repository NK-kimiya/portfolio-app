from django.db import models

class GitProject(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    
    subheading1 = models.CharField(max_length=200,blank=True)
    url1 = models.URLField(blank=True)
    
    subheading2 = models.CharField(max_length=200,blank=True)
    url2 = models.URLField(blank=True)
    
    subheading3 = models.CharField(max_length=200,blank=True)
    url3 = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
