from django.db import models
from datetime import datetime

# Aqui definimos nossos modelos de dados usando o sistema ORM do Django.

class Room(models.Model):
    name = models.CharField(max_length=1000)
    # Modelo de sala de chat. Armazena informações sobre as salas.

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    # Modelo de mensagem. Armazena informações sobre as mensagens trocadas nas salas.

# O sistema ORM traduz esses modelos em tabelas de banco de dados.
# Cada campo nos modelos corresponde a uma coluna na tabela correspondente.
# Por exemplo, a classe Room define uma tabela de salas com uma coluna 'name'.
# A classe Message define uma tabela de mensagens com colunas 'value', 'date', 'user' e 'room'.
