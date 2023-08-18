from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Aqui definimos as funções de visualização (views) para nosso aplicativo de chat.

def home(request):
    return render(request, 'chat/home.html')
    # Renderiza a página inicial do chat (home.html).

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chat/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })
    # Renderiza a página de uma sala de chat específica (room.html) com informações relevantes,
    # como o nome do usuário, o nome da sala e detalhes da sala.

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)
    # Manipula a submissão de um formulário para entrar em uma sala de chat.
    # Verifica se a sala existe. Se existir, redireciona para a página da sala.
    # Caso contrário, cria uma nova sala, a salva e redireciona para a página da sala.

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')
    # Manipula uma solicitação AJAX POST para enviar uma mensagem.
    # Cria uma nova mensagem com o conteúdo, o nome do usuário e o ID da sala especificados.
    # Retorna uma resposta indicando que a mensagem foi enviada com sucesso.

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room__icontains=room_details.id)

    return JsonResponse({
        'messages': list(messages.values())
    })
    # Manipula uma solicitação AJAX GET para obter as mensagens de uma sala de chat específica.
    # Recupera as mensagens associadas à sala e retorna uma resposta JSON com as mensagens.
