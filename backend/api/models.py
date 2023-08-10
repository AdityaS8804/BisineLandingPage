from django.db import models

# Create your models here.


class WishList(models.Model):
    email_id = models.EmailField(unique=True)
    def __str__(self):
        return f'{self.email_id}'
