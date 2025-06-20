from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=1000, null=True, blank=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nome}"