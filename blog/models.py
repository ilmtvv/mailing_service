from django.db import models

class BlogUnit(models.Model):
    title = models.CharField(max_length=11, default='')
    body = models.TextField()
    img = models.ImageField(upload_to='images/blog', blank=True, null=True)
    views = models.IntegerField(default=0)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{ self.title }'

    class Meta:
        verbose_name = 'BlogUnit'
        verbose_name_plural = 'BlogUnits'
