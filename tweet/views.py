from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect
from .models import TweetModel,TweetComment
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    # 사용자가 로그인 되어있는지 여부 확인
    user = request.user.is_authenticated
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html',{'tweet':all_tweet})
        else:
            return redirect('/sign-in')

    elif request.method == 'POST':
        # user 까지만 적으면 지금 로그인 되어있는 사용자의 전체정보를 가져옴.
        user = request.user
        content = request.POST.get('my-content', '')
        tags = request.POST.get('tag', '').split(',')
        if content == '':
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html', {'error': '글은 공백일 수 없습니다.','tweet':all_tweet})
        else:
            my_tweet = TweetModel.objects.create(author=user, content=content)
            # my_tweet.author = user
            # # home.html에 있는 name이 my-content인 친구를 가져와서 저장
            # my_tweet.content = request.POST.get('my-content','')
            for tag in tags:
                tag = tag.strip()
                if tag != '':  # 태그를 작성하지 않았을 경우에 저장하지 않기 위해서
                    my_tweet.tags.add(tag)
            my_tweet.save()
            return redirect('/tweet')

@login_required
def delete_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')


# detail_tweet / write_comment / delete_comment
@login_required
def detail_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)                            #생성된 역순으로 가져오기
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
    # 댓글 모델 가져오기 /                                tweet이라는 변수에 내가 가져온 모델이 들어감.
    return render(request, 'tweet/tweet_detail.html',{'tweet':my_tweet, 'comment':tweet_comment})

@login_required
def write_comment(request, id):
    if request.method == 'POST':
        # 아래 요청하는 html에서 폼태그의 액션의 주소로, 포스트 방법으로 name이 comment 인 인풋값을 가져옴 없을 경우 뒤의 빈값을 전달해줌
        comment = request.POST.get('comment', '')
        current_tweet = TweetModel.objects.get(id=id)

        TC = TweetComment()
        TC.comment = comment
        TC.author = request.user
        TC.tweet = current_tweet
        TC.save()

    return redirect('/tweet/'+str(id))


def delete_comment(request, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect('/tweet'+str(current_tweet))

class TagCloudTV(TemplateView):
    template_name = 'taggit/tag_cloud_view.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/tag_with_post.html'
    model = TweetModel

    def get_queryset(self):
        return TweetModel.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context