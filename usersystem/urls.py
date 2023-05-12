from django.contrib import admin
from django.urls import path

from .views import *
app_name = 'user'
urlpatterns = [
    path('test/', render_test,name="render_test"),
    path('user-form/', user_form_test,name="user_form_test"),
    path('user-list/', user_list,name="user_list"),
    path('', render_base,name="render_base"),
    path('register_theo/', register_theo,name='register_theo'),
    path('login_theo/', login_theo,name='login_theo'),
    path('mateus/1', render_login,name="render_login"),
    path('mateus/', render_register,name="render_register"),
]

from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
