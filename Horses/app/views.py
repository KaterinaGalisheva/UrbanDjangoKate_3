from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import *


# функция для компановки всего вместе с базами данных
# отображение базы данных на отдельной странице
def database(request):
    # подключение моделей из базы данных и сохранение
    Buyers = Buyer.objects.all()
    Horses = Horse.objects.all()

    context = {
        'Buyers':Buyers,
        'Horses':Horses
    }

    return render(request, 'database.html', context)



# функции для отображения рядовых страниц
def primary(request):
    return render(request, 'primary.html')

def store(request):
    # Получаем количество элементов на странице, по умолчанию 2
    items_per_page = int(request.GET.get('items_per_page', 2))
    # достается список игр
    horses = Horse.objects.all().order_by('id')
    # что размещается на страницах и в каком количестве
    paginator = Paginator(horses, items_per_page)
    # для перемещения
    page_number = request.GET.get('page')
    # страница как объект, передался номер страницы
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj, 
        'request': request
    }
    return render(request, 'store.html', context)


# функции для регистрации пользователей      
def sign_up(request):
    users = Buyer.objects.all()
    info = {}
    context = {
        'info':info,
        'users':users
     }
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration.html', context)
            if int(age) < 18:
                info['error'] = 'Вы несовершеннолетний'
                return render(request, 'registration.html', context)
            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Такой пользователь уже существует'
                return render(request, 'registration.html', context)
            else:
                Buyer.objects.create(name=username, age=age)
                return HttpResponse("Регистрация прошла успешно!")
                
    else:
        form = RegistrationForm()     
    return render(request, 'registration.html', context)



