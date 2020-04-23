from django.db import models
from django.contrib.auth import get_user_model


class Track(models.Model):
    title = models.CharField('Titulo',max_length=50)
    description = models.TextField('Descriçao',blank=True)
    url = models.URLField()
    created_at = models.DateTimeField('Criado',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado', auto_now=True)
    posted_at = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, related_name='likes', on_delete=models.CASCADE)


