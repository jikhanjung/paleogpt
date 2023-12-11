from django.db import models

# Create your models here.
class CollectionCache(models.Model):
    key = models.CharField(max_length=100,primary_key=True)
    version = models.IntegerField(default=0)
    data = models.TextField(null=True)
    parent = models.ForeignKey('self', null=True,on_delete=models.CASCADE,related_name='children')

class ItemCache(models.Model):
    key = models.CharField(max_length=100,primary_key=True)
    version = models.IntegerField(default=0)
    data = models.TextField(null=True)
    parent = models.ForeignKey('self', null=True,on_delete=models.CASCADE,related_name='children')
    #collection = ForeignKeyField(CollectionCache, null=True,backref='items')

class CollectionItemRel(models.Model):
    collection = models.ForeignKey(CollectionCache, on_delete=models.CASCADE,related_name='items')
    item = models.ForeignKey(ItemCache, on_delete=models.CASCADE,related_name='collections')

class LastVersion(models.Model):
    version = models.IntegerField(default=0)
