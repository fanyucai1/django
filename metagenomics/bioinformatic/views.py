from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("欢迎使用")

def users(request):
    return HttpResponse("用户列表")

def user_list(requests):
    #返回html
    #需创建templates目录，根据app的注册顺序进行查找
    return render(requests,"user_list.html")