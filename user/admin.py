from django.contrib import admin

# Register your models here.
# 장고에서 어드민 툴을 사용하겠다
from django.contrib import admin
# 우리가 생성한 모델을 가져오기
from .models import UserModel

# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다