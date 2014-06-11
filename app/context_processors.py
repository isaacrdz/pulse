from random import choice
frases = ['leonidas esta sentado', 'freddy se fue', 'christian esta arriba']

def ejemplo(request):
    return {'frase': choice(frases)}

from django.core.urlresolvers import reverse

def menu(request):
    menu = {'menu': [
        {'name': 'Home', 'url': reverse('home')},
        {'name': 'Add', 'url': reverse('add')},
        {'name': 'Acerca de', 'url': reverse('about')},
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu
