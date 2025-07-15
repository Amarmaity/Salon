from django.db import models

# Create your models here.
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator, MaxValueValidator

class Customer(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=128,
                                validators=[MinLengthValidator(4), MaxValueValidator(10)])
    def save(self, *args, **kwargs):
        # Hash password before saving if it's not already hashed
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
