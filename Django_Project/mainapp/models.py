from django.db import models


class Person(models.Model):
    create_at = models.DateTimeField(auto_created=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=False)
    email = models.CharField(max_length=50)

    def __repr__(self):
        return f'< Person {self.first_name} {self.last_name}>'
