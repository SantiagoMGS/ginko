from django.db import models


class actionModel(models.Model):
    action_id = models.AutoField(primary_key=True, null=False, unique=True)
    module_id = models.IntegerField()
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    active = models.IntegerField()
    class Meta:
        db_table = 'hk_action'
