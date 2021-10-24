from django.db import models
from django.db.models.fields import TextField

class clinicaAurifono(models.Model):
    STATUS = (
        ('fazer', 'Fazer'),
        ('pronto', 'Pronto')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=6,
        # select
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title