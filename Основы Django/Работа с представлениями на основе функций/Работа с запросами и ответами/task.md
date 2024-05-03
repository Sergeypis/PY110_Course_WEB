

Веб-разработка часто включает в себя создание и отправку HTML-страниц в ответ на запросы от клиентов. Django предоставляет удобные инструменты для работы с HTML-ответами в представлениях.

### Извлечение метода запроса

Когда клиент отправляет запрос на сервер, это могут быть различные HTTP-методы, такими как GET, POST и другие. В Django вы можете легко извлечь метод запроса из объекта `request`, что позволяет вам определить, какой тип операции выполняется.

```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse(f'Это {request.method}-запрос')

```

### Создание HTML-страницы

Django предоставляет удобные инструменты для создания HTML-страниц прямо в представлении. Это делается с использованием `HttpResponse`.

Пример создания HTML-страницы с использованием `HttpResponse`:

```python
from django.http import HttpResponse

def my_view(request):
    html_content = '<html><body><h1>Hello, World</h1></body></html>'
    return HttpResponse(html_content)

```

## JSON ответы

JSON (JavaScript Object Notation) - это формат обмена данными, который широко используется в веб-разработке для передачи данных между клиентом и сервером. В Django, вы можете легко формировать JSON-ответы в представлениях.

### Формирование JSON-ответов

Для создания JSON-ответа в Django, вы можете использовать класс `JsonResponse` из модуля `django.http`.

```python
from django.http import JsonResponse

def json_view(request):
    data = {'key': 'value'}
    return JsonResponse(data)

```

В этом примере `data` - это словарь Python, который Django автоматически преобразует в JSON. Ответ будет иметь правильный заголовок `Content-Type: application/json`.

JSON-ответы особенно полезны, когда вам нужно обмениваться данными с фронтендом вашего веб-приложения.