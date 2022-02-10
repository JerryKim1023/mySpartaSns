#user/models.py
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
from django.shortcuts import render, redirect


class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    # username = models.CharField(max_length=20, null=False)
    # password = models.CharField(max_length=256, null=False)
    # 상태정보
    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followee')


    # 생성일
    # created_at = models.DateTimeField(auto_now_add=True)
    # 수정일
    # updated_at = models.DateTimeField(auto_now=True)

# user/views.py

@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        # user_list.html 을 user_list 와 함께 보여줄거라는 의미
        return render(request, 'user/user_list.html', {'user_list': user_list})


@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    if me in click_user.followee.all():
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect('/user')