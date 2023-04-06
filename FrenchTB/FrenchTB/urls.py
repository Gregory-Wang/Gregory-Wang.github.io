"""FrenchTB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ftb.views import main, backstage, authentication

urlpatterns = [
    path('admin/', admin.site.urls),

    # 主页
    path('index/', main.index, name='主页'),
    path('index_old/', main.index_old, name='主页'),

    # 登录注册
    path('login/', authentication.login, name='登录'),
    path('signup/', authentication.signup, name='注册'),
    path('logout/', authentication.logout),
    path('image/code/', authentication.image_code),

    # 后台管理

    # 词库管理
    path('backstage/term/', backstage.term),
    path('backstage/term/add/', backstage.term_add),

]
