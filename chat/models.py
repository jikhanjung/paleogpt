from django.db import models

# Create your models here.
class CollectionCache(models.Model):
    zotero_user_id = models.CharField(max_length=100, blank=True, null=True)
    key = models.CharField(max_length=100,primary_key=True)
    version = models.IntegerField(default=0)
    data = models.TextField(null=True)
    parent = models.ForeignKey('self', null=True,on_delete=models.CASCADE,related_name='children')
    last_updated = models.DateTimeField(auto_now=True)

class ItemCache(models.Model):
    zotero_user_id = models.CharField(max_length=100, blank=True, null=True)
    key = models.CharField(max_length=100,primary_key=True)
    version = models.IntegerField(default=0)
    data = models.TextField(null=True)
    parent = models.ForeignKey('self', null=True,on_delete=models.CASCADE,related_name='children')
    last_updated = models.DateTimeField(auto_now=True)
    #collection = ForeignKeyField(CollectionCache, null=True,backref='items')

class CollectionItemRel(models.Model):
    zotero_user_id = models.CharField(max_length=100, blank=True, null=True)
    collection = models.ForeignKey(CollectionCache, on_delete=models.CASCADE,related_name='items')
    item = models.ForeignKey(ItemCache, on_delete=models.CASCADE,related_name='collections')

class LastVersion(models.Model):
    zotero_user_id = models.CharField(max_length=100, blank=True, null=True)
    version = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
