from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
# 회원가입 기능
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '')

        if password != password2:
            # 패스워드가 같지 않다고 알람
            return render(request, 'user/signup.html', {'error':'패스워드를 확인 해 주세요!'})
        else:
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error': '사용자 이름과 비밀번호는 필수 값 입니다'})

            exist_user = get_user_model().objects.filter(username=username)
            # filter 는 뒤의 ()의 조건으로 가져오겠다는 뜻임 /
            # 데이터가 무조건 있어야하는 get과 달리 필터는 있으나 없으나 실햄됨.
            # exist_user = UserModel.objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html', {'error': '사용자가 존재합니다'})
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                # new_user = UserModel()
                # new_user.username = username
                # new_user.password = password
                # new_user.bio = bio
                # new_user.save()
                return redirect('/sign-in')


# 로그인 기능
def sign_in_view(request):
    if request.method == 'POST':
        # 아래 유저네임과 패스워드는 연결 된 html 파일 내부에 'name:  ' 과 같아야 함
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')



        me = auth.authenticate(request, username=username, password=password)
        # 주황색은 유저모델에 있는 유저네임 값이고, 옆에는 디비와 일치하는 사용자 이름
        # me = UserModel.objects.get(username=username)
        if me is not None:
            auth.login(request, me)
            # request.session['user'] = me.username
            return redirect('/')
        else:
            return render(request, 'user/signin.html', {'error': '유저이름 혹은 패스워드를 확인 해 주세요'})


        return HttpResponse(me.username)
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            redirect('/')
        else:
            return render(request, 'user/signin.html')

@login_required
def logout(request):
    auth.logout(request)
    print('로그아웃 이상무')
    return redirect('/')

@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(username=request.user.username)
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
