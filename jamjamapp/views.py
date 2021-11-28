from django.contrib.messages.api import success
from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Blog, Bookmark, Comment, Hashtag, Eat_C, Look_C, Play_C, Big_Region, Small_Region, Profile, Bucket, Post, Event
from .forms import CreateForm, CommentForm, Eat_CForm, Look_CForm, Play_CForm, Big_RegionForm, Small_RegionForm, PostForm, ProfileForm, BucketForm, PostForm, UserForm, EventForm
from django.views.generic.list import ListView
# from datetime import date, datetime, timedelta
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
import datetime #다이어리용
import calendar#다이어리용
from .calendar import Calendar #다이어리용
from django.utils.safestring import mark_safe #다이어리용
from django import template
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator # 커뮤니티 페이징

# Create your views here.


def layout1(request):
    return render(request, 'layout1.html')


def layout2(request):
    return render(request, 'layout2.html')


def login(request):
    return render(request, 'login/login.html')


def main(request):
    return render(request, 'main.html')
# ------frontend 개발-------

# 임시 메인페이지


def layout(request):
    blogs = Blog.objects
    hashtag = Hashtag.objects
    return render(request, 'layout.html', {'blogs': blogs, 'hashtag': hashtag})

# 커뮤니티 첫 페이지


def community(request):
   # 입력 파라미터
   page = request.GET.get('page', '1')  # 페이지

   # 조회
   blogs = Blog.objects.order_by('-Write_day')

   # 페이징처리
   paginator = Paginator(blogs, 5)  # 페이지당 10개씩 보여주기
   page_obj = paginator.get_page(page)

   context = {'blogs': page_obj}
   return render(request, 'community/community.html', context)
#    # 입력 파라미터
#    page = request.GET.get('page', '1')  # 페이지
   
#    # 조회
#    question_list = Blog.objects.order_by('-create_date')

#    # 페이징처리
#    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
#    page_obj = paginator.get_page(page)

#    context = {'question_list': page_obj}
#    context = {'question_list': question_list}


# 커뮤니티 Write

def commu_write(request):
    return render(request, 'community/commu_write.html')


def commu_new(request, blog=None):
    if request.method == 'POST':
        blog = Blog()
        blog.Title = request.POST['Title']
        blog.Content = request.POST['Content']
        blog.Write_day = timezone.now()
        blog.save()
        return redirect('community')
    else:
        return render(request, 'commu_new.html', {'blog':blog})

# 커뮤니티 C


# def commu_C(request, blog=None):
#     hashtag = Hashtag.objects
#     if request.method == "POST":
#         form = CreateForm(request.POST, request.FILES, instance=blog)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.Write_day = timezone.datetime.now()
#             blog.save()
#             form.save_m2m()
#             return redirect('layout')
#     else:
#         form = CreateForm(instance=blog)
#         return render(request, 'community/commu_write.html', {'form': form, 'hashtag': hashtag})


# 커뮤니티 게시글 자세히 보기 페이지 + 댓글(프론트)

def commu_detail(request, id):
    blog = get_object_or_404(Blog, id = id)
    default_view_count = blog.view_count
    blog.view_count = default_view_count + 1
    blog.save()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = blog
            comment.pub_date = timezone.datetime.now()
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('commu_detail', id)
    else:
        form = CommentForm()
        return render(request, 'community/commu_detail.html', {'blog':blog, 'form':form})


# 커뮤니티 게시글 자세히 보기 페이지 + 댓글(백)


# def commu_detail(request, id):
#     blog = get_object_or_404(Blog, id=id)
#     default_view_count = blog.view_count
#     blog.view_count = default_view_count + 1
#     blog.save()
#     # 여기서부터 댓글
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post_id = blog
#             comment.text = form.cleaned_data['text']
#             comment.save()
#         return redirect('commu_detail', id)
#     else:
#         form = CommentForm()
#     return render(request, 'community/commu_detail.html', {'blog': blog, 'form': form})


# 커뮤니티 수정

def commu_edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'community/commu_edit.html', {'blog':edit_blog})


def commu_update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.Title = request.POST['Title']
    update_blog.Content = request.POST['Content']
    update_blog.Write_day = timezone.now()
    update_blog.save()
    return redirect('commu_detail', update_blog.id)

# @login_required
# def commu_edit(request, id):
#     blog = get_object_or_404(Blog, id=id)
#     if request.method == "POST":
#         form = CreateForm(request.POST, instance=blog)
#         if form.is_valid():
#             form.save(commit=False)
#             form.save()
#             return redirect('commu_detail', id)
#     else:
#         form = CreateForm(instance=blog)
#     return render(request, 'community/commu_edit.html', {'form': form})

# @login_required
# def commu_edit(request, pk):
#    notice = Blog.objects.get(id=pk)
#
#    if request.method == "POST":
#        if(notice.Writer == request.user):
#            form = CreateForm(request.POST, instance=notice)
#            if form.is_valid():
#                notice = form.save(commit = False)
#                notice.save()
#                messages.success(request, "수정되었습니다.")
#                return redirect('/detail/'+str(pk))
#    else:
#        notice = Blog.objects.get(id=pk)
#        if notice.Writer == request.user:
#            form = CreateForm(instance=notice)
#            context = {
#                'form': form,
#                'edit': '수정하기',
#            }
#            return render(request, "community/commu_edit.html", context)
#        else:
#            messages.error(request, "본인 게시글이 아닙니다.")
#            return redirect('/detail/'+str(pk))


# 게시글 삭제(백)

def commu_delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('community')


# 댓글 삭제


def comment_remove(request, pk, id):

    if request.method == 'POST':

        print('comment_remove')

        Comment.objects.get(pk=pk).delete()
    
    return redirect('commu_detail', id)

# 좋아요


def commu_like(request, pk):
    if not request.user.is_active:
        return HttpResponse('First SignIn please')

    blog = get_object_or_404(Blog, pk=pk)
    user = request.user

    if blog.Blog_likes.filter(id=user.id).exists():
        blog.Blog_likes.remove(user)
    else:
        blog.Blog_likes.add(user)

    return redirect('commu_detail', pk)


#다이어리 페이지
def calendar_view(request):
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)

    cal = Calendar(today.year, today.month)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'diary_events.html', context)

#현재 달력을 보고 있는 시점의 시간을 반환
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()

#현재 달력의 이전 달 URL 반환
def prev_month(day):
    first = day.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

#현재 달력의 다음 달 URL 반환
def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

#새로운 Event의 등록 혹은 수정
def event(request, event_id=None):
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('calendar')
    return render(request, 'diary_input.html', {'form': form})


register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg


@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))


# course 메인


def course(request):
    return render(request, 'course/course.html')

# course 디테일


def course_detail(request):
    return render(request, 'course/course_detail.html')

# course_eat 전체 목록


def course_eat(request):
    eat_Cs = Eat_C.objects
    return render(request, 'course/course_eat.html', {'eat_Cs': eat_Cs})

# course_eat_write


def course_eat_write(request):
    return render(request, 'course/course_eat_C.html')

# course_eat_C


def course_eat_C(request, eat_C=None):
    big_region = Big_Region.objects
    small_region = Small_Region.objects
    if request.method == "POST":
        form = Eat_CForm(request.POST, request.FILES, instance=eat_C)
        if form.is_valid():
            eat_C = form.save(commit=False)
            eat_C.Write_day = timezone.datetime.now()
            eat_C.save()
            form.save_m2m()
            return redirect('course_eat')
    else:
        form = Eat_CForm(instance=eat_C)
        return render(request, 'course/course_eat_C.html', {'form': form, 'big_region': big_region, 'small_region': small_region})

# course_look 전체 목록


def course_look(request):
    look_Cs = Look_C.objects
    return render(request, 'course/course_look.html', {'look_Cs': look_Cs})

# course_look_write


def course_look_write(request):
    return render(request, 'course/course_eat_C.html')

# course_look_C


def course_look_C(request, look_C=None):
    big_region = Big_Region.objects
    small_region = Small_Region.objects
    if request.method == "POST":
        form = Look_CForm(request.POST, request.FILES, instance=look_C)
        if form.is_valid():
            look_C = form.save(commit=False)
            look_C.Write_day = timezone.datetime.now()
            look_C.save()
            look_C.save_m2m()
            return redirect('course/course_look')
    else:
        form = Look_CForm(instance=look_C)
        return render(request, 'course/course_look_C.html', {'form': form, 'big_region': big_region, 'small_region': small_region})

# course_play 전체 목록


def course_play(request):
    play_Cs = Play_C.objects
    return render(request, 'course/course_play.html', {'play_Cs': play_Cs})

# course_play_write


def course_play_write(request):
    return render(request, 'course/course_play_C.html')

# course_play_C


def course_play_C(request, play_C=None):
    big_region = Big_Region.objects
    small_region = Small_Region.objects
    if request.method == "POST":
        form = Play_CForm(request.POST, request.FILES, instance=play_C)
        if form.is_valid():
            play_C = form.save(commit=False)
            play_C.Write_day = timezone.datetime.now()
            play_C.save()
            play_C.save_m2m()
            return redirect('course/course_play')
    else:
        form = Play_CForm(instance=play_C)
        return render(request, 'course/course_play_C.html', {'form': form, 'big_region': big_region, 'small_region': small_region})

# course_eat 게시글 자세히 보기 페이지 + 댓글


def course_eat_detail(request, id):
    eat_C = get_object_or_404(Eat_C, id=id)
    default_view_count = eat_C.view_count
    eat_C.view_count = default_view_count + 1
    eat_C.save()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = eat_C
            comment.text = form.cleaned_data['text']
            comment.save()
        return redirect('course_eat_detail', id)
    else:
        form = CommentForm()
        return render(request, 'course/course_eat_detail.html', {'eat_C': eat_C, 'form': form})


# course_eat_U


def course_eat_U(request, id):
    eat_C = get_object_or_404(Eat_C, id=id)
    if request.method == "POST":
        form = Eat_CForm(request.POST, instance=eat_C)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('course_eat_detail', id)
    else:
        form = Eat_CForm(instance=eat_C)
    return render(request, 'course/course_eat_U.html', {'form': form})

# course_eat 삭제


def course_eat_delete(request, id):
    delete_eat_C = get_object_or_404(Eat_C, id=id)
    delete_eat_C.delete()
    return redirect('course_eat')

# course_eat 좋아요


def course_eat_like(request, pk):
    # if not request.user.is_active:
    #    return HttpResponse('First SignIn please')

    eat_C = get_object_or_404(Eat_C, pk=pk)
    user = request.user

    if eat_C.Eat_likes.filter(id=user.id).exists():
        eat_C.Eat_likes.remove(user)
    else:
        eat_C.Eat_likes.add(user)

    return redirect('course_eat_detail', pk)

# course_look 게시글 자세히 보기 페이지


def course_look_detail(request, id):
    look_C = get_object_or_404(Look_C, id=id)
    default_view_count = look_C.view_count
    look_C.view_count = default_view_count + 1
    look_C.save()
    return render(request, 'course/course_look_detail', {'look_C': look_C})

# course_look_U


def course_look_U(request, id):
    look_C = get_object_or_404(Look_C, id=id)
    if request.method == "POST":
        form = Look_CForm(request.POST, instance=look_C)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('course_look_detail', id)
    else:
        form = Look_CForm(instance=look_C)
    return render(request, 'course/course_look_U.html', {'form': form})

# course_look 삭제


def course_look_delete(request, id):
    delete_look_C = get_object_or_404(Look_C, id=id)
    delete_look_C.delete()
    return redirect('course/course_look_R')

# course_look 좋아요


def course_look_like(request, pk):
    if not request.user.is_active:
        return HttpResponse('First SignIn please')

    look_C = get_object_or_404(Look_C, pk=pk)
    user = request.user

    if look_C.Look_likes.filter(id=user.id).exists():
        look_C.Look_likes.remove(user)
    else:
        look_C.Look_likes.add(user)

    return redirect('course_look_detail', pk)

# course_play 게시글 자세히 보기 페이지


def course_play_detail(request, id):
    play_C = get_object_or_404(Play_C, id=id)
    default_view_count = play_C.view_count
    play_C.view_count = default_view_count + 1
    play_C.save()
    return render(request, 'course/course_play', {'play_C': play_C})

# course_play_U


def course_play_U(request, id):
    play_C = get_object_or_404(Play_C, id=id)
    if request.method == "POST":
        form = Play_CForm(request.POST, instance=play_C)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('course_play_detail', id)
    else:
        form = Play_CForm(instance=play_C)
    return render(request, 'course/course_play_U.html', {'form': form})

# course_play 삭제


def course_play_delete(request, id):
    delete_play_C = get_object_or_404(Play_C, id=id)
    delete_play_C.delete()
    return redirect('course/course_play_R')

# course_play 좋아요


def course_play_like(request, pk):
    if not request.user.is_active:
        return HttpResponse('First SignIn please')

    play_C = get_object_or_404(Play_C, pk=pk)
    user = request.user

    if play_C.play_likes.filter(id=user.id).exists():
        play_C.play_likes.remove(user)
    else:
        play_C.play_likes.add(user)

    return redirect('course_play_detail', pk)


# course_eat 첫 페이지
def course_eat_R(request, small_region_id):
    small_region = get_object_or_404(Small_Region, pk=small_region_id)
    eat_Cs = Eat_C.objects
    return render(request, 'course/course_eat_R.html', {'eat_Cs': eat_Cs, 'small_region': small_region})

# course_look 첫 페이지


def course_look_R(request, small_region_id):
    small_region = get_object_or_404(Small_Region, pk=small_region_id)
    look_Cs = Look_C.objects
    return render(request, 'course/course_look_R.html', {'look_Cs': look_Cs, 'small_region': small_region})

# course_play 첫 페이지


def course_play_R(request, small_region_id):
    small_region = get_object_or_404(Small_Region, pk=small_region_id)
    play_Cs = Play_C.objects
    return render(request, 'course/course_play_R.html', {'play_Cs': play_Cs, 'small_region': small_region})

# class BookmarkList(ListView):
#    model = Bookmark
#
# class BookmarkCreate(CreateView):
#    model = Bookmark
#    fields = ['book_site_name', 'book_url', 'book_contents']
#    template_name_suffix = '_bookcreate'
#    success_url = '/'
#
# class BookmarkUpdate(UpdateView):
#    model = Bookmark
#    fields = ['book_site_name', 'book_url', 'book_contents']
#    template_name_suffix = '_bookupdate'
#    success_url = '/'
#
# class BookmarkDelete(DetailView):
#    model = Bookmark
#    template_name_suffix = '_bookdelete'
#    success_url = '/'
#
# class BookmarkDetail(DetailView):
#    model = Bookmark
#    template_name_suffix = '_bookdetail'


# ------민정이 개발-------

# day_detail
def day_detail(request):
    posts = Post.objects
    return render(request, 'day_detail.html', {'posts': posts})

# 마이페이지


def mypage(request):
    return render(request, 'mypage/mypage.html')

# 프로필


def profile(request):
    profiles = Profile.objects
    return render(request, 'mypage/profile.html', {'profiles': profiles})

# 버킷리스트


def bucketlist(request):
    buckets = Bucket.objects
    return render(request, 'bucketlist.html', {'buckets': buckets})


def diary(request):
    return render(request, 'diary.html')

# 다이어리 작성


def diary_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('layout')
    else:
        form = PostForm
        return render(request, 'diary.html', {'form': form})

# 버킷리스트 작성


def bucket_create(request):
    if request.method == "POST":
        form = BucketForm(request.POST)
        if form.is_valid():
            bucket = form.save(commit=False)
            bucket.save()
            return redirect('layout')
    else:
        form = BucketForm
        return render(request, 'bucketlist_write.html', {'form': form})

# 다이어리 디테일


def diary_detail(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_id = post
            post.text = form.cleaned_data['text']
            post.save()
            return redirect('day_detail_write', id)
    else:
        form = PostForm()
        return render(request, 'day_detail_detail.html', {'post': post, 'form': form})

# 버킷리스트 디테일


def bucket_detail(request, id):
    bucket = get_object_or_404(Bucket, id=id)
    if request.method == 'POST':
        form = BucketForm(request.POST)
        if form.is_valid():
            bucket = form.save(commit=False)
            bucket.post_id = bucket
            bucket.text = form.cleaned_data['text']
            bucket.save()
            return redirect('layout', id)
    else:
        form = BucketForm()
        return render(request, 'bucketlist_detail.html', {'bucket': bucket, 'form': form})


# 데이디테일 수정

def diary_edit(request):
    return render(request, 'diary_edit.html')

# 데이디테일 수정


# def diary_edit(request, id):
#     post = get_object_or_404(Post, id=id)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save(commit=False)
#             form.save()
#             return redirect('layout')
#     else:
#         form = PostForm(instance=post)
#         return render(request, 'diary_edit.html', {'form': form})

# 버킷리스트 수정


def bucket_edit(request, id):
    bucket = get_object_or_404(Bucket, id=id)
    if request.method == "POST":
        form = BucketForm(request.POST, instance=bucket)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('layout')
    else:
        form = BucketForm(instance=bucket)
        return render(request, 'bucketlist_edit.html', {'form': form})

# 프로필 수정


def profile_edit(request):
    return render(request, 'mypage/profile_edit.html')

# 연인 연결 페이지


def connection(request):
    return render(request, 'mypage/connection.html')

# 구매 목록 확인


def purchaselist(request):
    return render(request, 'mypage/purchaselist.html')


# 프로필 (비번)수정(프로필 수정이랑 다른거야?)


def p_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('layout')
    else:
        form = ProfileForm(instance=post)
        return render(request, 'profile_edit.html', {'form': form})

# 다이어리 삭제


def diary_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('layout')

# 버킷리스트 삭제


def bucket_delete(request, id):
    delete_bucket = get_object_or_404(Bucket, id=id)
    delete_bucket.delete()
    return redirect('layout')

# 샵 메인


def shop(request):
    return render(request, 'shop/shop.html')

# 폰트/배경 샵


def theme(request):
    return render(request, 'shop/theme.html')


# 기능 샵

def option(request):
    return render(request, 'shop/option.html')

# 아이템 자세히 보기


def purchase_example(request):
    return render(request, 'mypage/purchase_example.html')


# 잼구매 샵


def jampay(request):
    return render(request, 'shop/jampay.html')

# 결제 확인


def pay(request):
    return render(request, 'shop/pay.html')

# 최종 결제


def finalpay(request):
    return render(request, 'shop/finalpay.html')

# 결제 완료


def completepay(request):
    return render(request, 'shop/completepay.html')

# ------예찬이 개발-------

# 로그인


def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        olduser = authenticate(email=email, password=password)

        if olduser is not None:
            auth.login(request, olduser)
            return redirect('main')
        else:
            messages.error(request, '회원정보가 일치하지 않습니다. 다시 시도해주세요.')
            return redirect('login')
    else:
        return render(request, 'login/login.html')


# 회원가입


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            first_password = form.cleaned_data.get('password1')
            user = auth.authenticate(email=email, password=first_password)
            auth.login(request, user)
            return redirect('main')
        else:
            context['signupform'] = form
    else:
        form = UserForm()
        context['signupform'] = form
    return render(request, 'login/signup.html', {"form": form})

# 로그인


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login/login.html')

# 로그아웃


def signout(request):
    auth.logout(request)
    return redirect('login')
# ------광현이 개발-------
