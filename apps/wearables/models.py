from django.db import models

class Wearable(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WearableData(models.Model):
    wearable = models.ForeignKey(Wearable, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    data_type = models.CharField(max_length=50)
    value = models.FloatField()

    def __str__(self):
        return f"{self.data_type} data from {self.wearable.name} at {self.timestamp}"