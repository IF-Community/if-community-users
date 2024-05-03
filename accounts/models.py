from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_name = models.CharField("Nome de Perfil", max_length=100)
    profile_bio = models.TextField("Biografia do Perfil", max_length=255, null=True, blank=True)
    profile_photo = models.ImageField("Foto de Perfil", upload_to="perfil_photos/", null=True)
    profile_background = models.ImageField("Fundo do Perfil", upload_to="profile_backgrounds/", null=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis" 

    def __str__(self) -> str:
        return f'{self.profile_name}'

