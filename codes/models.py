from django.db import models
from users.models import User


class Code(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_code')

    def __str__(self):
        return str(self.number)
    


Code()