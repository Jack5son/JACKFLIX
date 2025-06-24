from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


# Create your models here.
class Filme(models.Model):
    nome = models.CharField('Título do filme', max_length=150)
    ano_lancamento = models.PositiveIntegerField(
        'Ano de Lançamento',
        validators=[
            MinValueValidator(1895), 
            MaxValueValidator(datetime.date.today().year + 5)
        ],
        default=datetime.date.today().year
    )
    idGenero = models.ForeignKey('genero.Genero', verbose_name="Gênero", on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
