import email
from django.db import models

# Create your models here.
class FlutterAppDj(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    class Meta:
        db_table = "flutterappdj"
        