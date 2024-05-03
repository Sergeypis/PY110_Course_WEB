

1. **Настройка `STATICFILES_DIRS`:** В файле `settings.py` вашего Django-проекта определите переменную `STATICFILES_DIRS`, которая будет содержать пути к каталогам, где хранятся ваши статические файлы.
    
    ```python
    # settings.py
    
    import os
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
    
    ```
    
    Здесь `"static"` - это имя каталога, в котором вы хотите хранить свои статические файлы.
    
2. **Обработка статических файлов в URL-путях:**
    
    В файле `urls.py` вашего Django-проекта убедитесь, что вы включили обработку статических файлов в URL-путях в режиме отладки:
    
    ```python
    # urls.py
    
    from django.conf import settings
    from django.conf.urls.static import static
    
    urlpatterns = [
        # Ваши URL-пути
    ]
    
    if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    ```
    
    Это обеспечивает обслуживание статических файлов в режиме отладки.