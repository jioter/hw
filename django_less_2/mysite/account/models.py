from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.user.username


# using proxy
# class Author(User):
#     class Meta:
#         proxy = True
#
#         def __str__(self):
#             return ...