1:安装Django

    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple Django

2:开始第一个project

    django-admin startproject metagenomics

3:默认项目的文件介绍

    metagenomics
    ├── manage.py   【项目启动】
    └── metagenomics
        ├── __init__.py
        ├── asgi.py     【接受网络请求】
        ├── settings.py 【项目配置，常修改】
        ├── urls.py     【URL和函数的对应关系，常修改】
        └── wsgi.py     【接受网络请求】

4:创建APP

    python3 manage.py startapp bioinformatic

    ├── bioinformatic
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py   【对数据库操作】
    │   ├── tests.py
    │   └── views.py     【函数】
    ├── manage.py
    └── metagenomics
        ├── __init__.py
        ├── __pycache__
        ├── asgi.py
        ├── settings.py
        ├── urls.py             【URL->函数】
        └── wsgi.py

5.快速上手

5-1:确保APP注册，编辑[setting.py],黑色部分为添加项

INSTALLED_APPS = [
'django.contrib.admin',

'django.contrib.auth',

'django.contrib.contenttypes',

'django.contrib.sessions',

'django.contrib.messages',

'django.contrib.staticfiles',

**'bioinformatics.apps.BioinformaticConfig'**

]
    
5-2:编写URL和视图函数对应关系[urls.py]
from bioinformatic import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    # www.xxx.com/index
    path('index/', views.index),
]

5-3:编写视图函数[views.py]

6.启动项目

    python3 manage.py runserver 

7.templates模版（返回html）

    7-1:在bioinformatic(APP)下创建templates目录，在目录里添加html文件
    
8.静态文件包括

    图片
    CSS
    js
