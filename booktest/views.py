from io import BytesIO

from PIL import ImageDraw, ImageFont
from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def index(request):
    print("hero--------1")
    hero = HeroInfo.objects.all()
    print("hero--------", hero)
    context = {'hero': hero}
    return render(request, 'booktest/index.html', context)


def show(request, id):
    context = {'id': id}
    print("不该进来")
    return render(request, "booktest/show.html", context)


def showrec(request, p1, p2):
    context = {'p1': p1, 'p2': p2}
    print(p1)
    print(p2)
    return render(request, "booktest/show1.html", context)

#用于联系模板的继承
def index2(request):
    return render(request,'booktest/index2.html')


def user1(request):
    context = {"uname":"水务ing"}
    return render(request,'booktest/user1.html',context)

def user2(request):
    return render(request, 'booktest/user2.html')

def htmlTest(request):
    context = {'t1': "<h1>123</h1>"}
    return render(request, 'booktest/htmlTest.html',context)

def verifycode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('consola.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    from io import StringIO
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    print("-------------------------------------")
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


#csrf

def csrf1(request):
    return render(request, 'booktest/csrf1.html')
def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)