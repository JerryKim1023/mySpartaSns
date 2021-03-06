# tweet/models.py
from django.db import models
from user.models import UserModel
from taggit.managers import TaggableManager

# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"

# ForeignKey는 타입이 아니라 다른 데이터베이스에서 모델을 가져오겠다는 의미
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 댓글 모델 만드는 부분
class TweetComment(models.Model):
    class Meta:
        db_table = "comment"

    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
