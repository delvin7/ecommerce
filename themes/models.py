from django.db import models

class sitesettings(models.Model):
    caption=models.TextField()
    banner=models.ImageField(upload_to='media/')

    def __str__(self):
        return self.site_name   
