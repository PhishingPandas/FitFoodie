from django.db import models
from datetime import date
# Create your models here.

class Accounts(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=60)

    class Meta:
        db_table = "accounts"
    
class Nutrients(models.Model):
    fid = models.AutoField(primary_key=True,default=1)
    fname=models.CharField(max_length=100)
    u_id=models.ForeignKey(Accounts,on_delete=models.CASCADE,null=False,default=1)
    fat=models.FloatField()
    carbohydrates=models.FloatField()
    cholesterol=models.FloatField()
    protein=models.FloatField()
    sodium=models.FloatField()
    date = models.DateField(("Date"), auto_now=True)

    class Meta:
        db_table = "nutrients"

