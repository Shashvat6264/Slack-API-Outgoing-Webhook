from django.db import models

# Create your models here.
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)
    