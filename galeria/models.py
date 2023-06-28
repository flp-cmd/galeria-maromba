from django.db import models


class Exercicios(models.Model):
    
    CATEGORIAS = [
        ('PEITO', 'Peito'),
        ('COSTAS', 'Costas'),
        ('BICEPS', 'Biceps'),
        ('TRICEPS', 'Triceps'),
        ('PERNAS', 'Pernas'),
        
    ]
    
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=5000)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS, default='')
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=False)
    
