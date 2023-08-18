from django.urls import path
from . import views

# Definimos os padrões de URL para o aplicativo de chat.

urlpatterns = [
    path('', views.home, name="home"),
    # Padrão de URL vazio (''): Mapeia para a função de visualização 'home'.
    # Isso renderizará a página inicial do chat (home.html).

    path('<str:room>/', views.room, name='room'),
    # Padrão de URL com um parâmetro de sala ('<str:room>/'): Mapeia para a função de visualização 'room'.
    # Isso permite acessar uma sala de chat específica.
    # O parâmetro 'room' é capturado a partir da URL e passado para a função de visualização.

    path('checkview', views.checkview, name='checkview'),
    # Padrão de URL 'checkview': Mapeia para a função de visualização 'checkview'.
    # Essa função lida com a submissão de um formulário para entrar em uma sala de chat.

    path('send', views.send, name='send'),
    # Padrão de URL 'send': Mapeia para a função de visualização 'send'.
    # Essa função lida com o envio de mensagens através de uma solicitação AJAX POST.

    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    # Padrão de URL 'getMessages/<str:room>/': Mapeia para a função de visualização 'getMessages'.
    # Essa função lida com a obtenção de mensagens de uma sala de chat específica através de uma solicitação AJAX GET.
]
