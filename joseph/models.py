from django.db import models


# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=200, null=False)
    Email_address = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, )
    date_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return str(self.name)
