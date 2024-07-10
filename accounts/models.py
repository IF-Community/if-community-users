from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile_name = models.CharField("Nome de Perfil", max_length=100)
    profile_bio = models.TextField("Biografia do Perfil", max_length=255, null=True, blank=True)
    profile_photo = models.ImageField("Foto de Perfil", upload_to="perfil_photos/", blank=True, null=True)
    profile_background = models.ImageField("Fundo do Perfil", upload_to="profile_backgrounds/", blank=True, null=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis" 

    def __str__(self) -> str:
        return f'{self.profile_name}'

class Report(models.Model):

    class Category(models.TextChoices):
        SPAM = 'SP', 'Spam'
        OFFENSIVE_CONTENT = 'OC', 'Conteúdo Ofensivo'
        HARASSMENT_BULLYING = 'HB', 'Assédio ou Bullying'
        IMPERSONATION = 'IM', 'Impersonação'
        INAPPROPRIATE_CONTENT = 'IC', 'Conteúdo Inapropriado'
        MISINFORMATION = 'MI', 'Informações Falsas'
        COPYRIGHT_VIOLATION = 'CV', 'Violação de Direitos Autorais'
        SECURITY_PRIVACY = 'SY', 'Segurança e Privacidade'
        ILLEGAL_ACTIVITY = 'IA', 'Conduta Ilegal'
        HATE_SPEECH = 'HS', 'Discurso de Ódio e Discriminação'
        CHILD_ABUSE = 'CA', 'Abuso Infantil'
        OTHER = 'OT', 'Outros'

    reported_by = models.ForeignKey(
        get_user_model(),
        related_name='reports_made',
        on_delete=models.CASCADE
    )
    reported_user = models.ForeignKey(
        get_user_model(),
         related_name='reports_received',
        on_delete=models.CASCADE
    )
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.OTHER,
    )
    description = models.TextField(
        verbose_name="Descrição do report",
        blank=True,
        max_length=255
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports" 

    def __str__(self) -> str:
        return f'Reporte de {self.reported_by} sobre {self.reported_user} - {self.get_category_display()}'