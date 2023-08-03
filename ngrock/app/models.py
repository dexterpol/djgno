from django.db import models




class Nota(models.Model):
    funcionario = models.CharField(max_length=100)
    valor_material = models.DecimalField(max_digits=1000, decimal_places=2 )
    descricao = models.CharField(max_length=100 , default="material")
    data_criacao = models.DateTimeField(auto_now_add=True)

    # Adicione outros campos, se necessário

    def __str__(self):
        return f'{self.funcionario} - R${self.valor_material}'
