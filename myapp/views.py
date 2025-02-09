from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact3
from .models import Nav

# Create
def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = Contact3.objects.create(name=name, email=email, password=password)
            request.session['user_name'] = user.name  # Сохраняем имя в сессии
            return redirect('index')  # Перенаправление на главную страницу

    return render(request, 'create_item.html')


def link_item(request):
    error_message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = Contact3.objects.filter(name=name, password=password).first()

        if user:
            request.session['user_name'] = user.name  # Обновляем имя в сессии
            return redirect('index')  # Перенаправление на главную
        else:
            error_message = "Неправильное имя или пароль"

    return render(request, 'link_item.html', {'error_message': error_message})

def logout_view(request):
    request.session.flush()  # Очистка сессии
    return redirect('index')  # Перенаправление на главную





# Добавляем обработчик для index.html
def index(request):
    navs = Nav.objects.all()
    return render(request, 'index.html', {'navs' : navs})  
# Update
def update_item(request, item_id):
    item = get_object_or_404(Contact3, id=item_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('confirm_password')
        item.name = name
        item.email = email
        item.password = password
        item.password1 = password1
        item.save()
        return redirect('link_item')

    return render(request, 'update_item.html', {'item': item})


# Delete


from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact3

# Функция для просмотра данных
def view_data(request):
    users = Contact3.objects.all()  # Получаем все записи из БД
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")

        if name and password:
            # Проверяем, есть ли пользователь в базе
            user, created = Contact3.objects.get_or_create(name=name, defaults={"password": password})
            
            if not created:
                # Если пользователь существует, обновляем пароль
                user.password = password
                user.save()

    return render(request, "view_data.html", {"users": users})

# Функция для обновления данных
def update_data(request, user_id):
    user = get_object_or_404(Contact3, id=user_id)
    if request.method == "POST":
        user.name = request.POST.get("name")
        user.password = request.POST.get("password")
        user.save()
        return redirect("view_data")

    return render(request, "update_data.html", {"user": user})

# Функция для удаления данных
def delete_data(request, user_id):
    user = get_object_or_404(Contact3, id=user_id)
    user.delete()
    return redirect("view_data")

def base(request):
    items = Contact3.objects.all()  
    return render(request, 'base.html', {'items': items})  