from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 200)
    shortPost = models.CharField(max_length = 400)
    post = models.TextField()
    date = models.DateTimeField()
    autor = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='telecomNews/images', blank=True)

    def __str__(self):
        return self.title
