"""jamjamproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import jamjamapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jamjamapp.views.login, name='login'),  # 로그인(첫화면)
    path('main/', jamjamapp.views.main, name='main'),  # 메인
    path('layout/', jamjamapp.views.layout, name='layout'),  # 백메인
    path('calendar/', jamjamapp.views.calendar_view, name="calendar"),#일정
    path('event/new/', jamjamapp.views.event, name="new"),#일정 생성
    path('event/edit/<int:event_id>', jamjamapp.views.event, name="edit"),#일정 수정
    path('community/', jamjamapp.views.community, name='community'),  # 커뮤니티 메인
    path('course/', jamjamapp.views.course, name='course'),  # 코스 메인
    path('course_detail/', jamjamapp.views.course_detail, name='course_detail'),  # 코스 디테일
    path('shop/', jamjamapp.views.shop, name='shop'),  # 샵 메인
    path('theme/', jamjamapp.views.theme, name='theme'),  # 폰트/배경 샵
    path('option/', jamjamapp.views.option, name='option'),  # 기능 샵
    path('jampay/', jamjamapp.views.jampay, name='jampay'),  # 잼 구매 샵
    path('mypage/', jamjamapp.views.mypage, name='mypage'),  # 마이페이지
    path('commu_detail/<str:id>/', jamjamapp.views.commu_detail, name='commu_detail'),  # 커뮤니티 게시글 자세히 보기(프론트)
    path('commu_edit/<str:id>/', jamjamapp.views.commu_edit, name='commu_edit'),
    path('commu_update/<str:id>/', jamjamapp.views.commu_update, name='commu_update'),  # 게시글 수정
    #path('community_search/<int:hashtag_id>/', jamjamapp.views.community, name='community'),  # 게시글 각 카테고리 페이지(해시태그로 치면 search)
    path('commu_write/', jamjamapp.views.commu_write, name='commu_write'),
    path('commu_write/commu_new/', jamjamapp.views.commu_new, name='commu_new'),
    path('commu_delete/<str:id>/', jamjamapp.views.commu_delete, name='commu_delete'),  # 게시글 삭제
    path('commu_like/<int:pk>', jamjamapp.views.commu_like, name='commu_like'),
    path('course_eat/', jamjamapp.views.course_eat,
         name='course_eat'),  # course_eat 전체글 보기
    path('course_eat_detail/<str:id>/', jamjamapp.views.course_eat_detail,
         name='course_eat_detail'),  # eat 게시글 자세히 보기
    path('course_eat_R/<int:small_region_id>/',
         jamjamapp.views.course_eat_R, name='course_eat_R'),  # eat search
    path('course_eat_write/course_eat_C/', jamjamapp.views.course_eat_C,
         name='course_eat_C'),  # eat 게시글 C
    path('course_eat_U/<str:id>/', jamjamapp.views.course_eat_U,
         name='course_eat_U'),  # eat 게시글 수정
    path('course_eat_delete/<str:id>/', jamjamapp.views.course_eat_delete,
         name='course_eat_delete'),  # eat 게시글 삭제
    path('course_eat_like/<int:pk>', jamjamapp.views.course_eat_like,
         name='course_eat_like'),  # eat 게시글 좋아요
    path('course_look/', jamjamapp.views.course_look,
         name='course_look'),  # course_eat 전체글 보기
    path('course_look_detail/<str:id>/', jamjamapp.views.course_look_detail,
         name='course_look_detail'),  # look 게시글 자세히 보기
    path('course_look_R/<int:small_region_id>/',
         jamjamapp.views.course_look_R, name='course_look_R'),  # look search
    path('course_look_write/course_look_C/',
         jamjamapp.views.course_look_C, name='course_look_C'),  # look 게시글 C
    path('course_look_U/<str:id>/', jamjamapp.views.course_look_U,
         name='course_look_U'),  # look 게시글 수정
    path('course_look_delete/<str:id>/', jamjamapp.views.course_look_delete,
         name='course_look_delete'),  # look 게시글 삭제
    path('course_look_like/<int:pk>', jamjamapp.views.course_look_like,
         name='course_look_like'),  # look 게시글 좋아요
    path('course_play/', jamjamapp.views.course_play,
         name='course_play'),  # course_eat 전체글 보기
    path('course_play_detail/<str:id>/', jamjamapp.views.course_play_detail,
         name='course_play_detail'),  # play 커뮤니티 게시글 자세히 보기
    path('course_play_R/<int:small_region_id>/',
         jamjamapp.views.course_play_R, name='course_play_R'),  # play search
    path('course_play_write/course_play_C/',
         jamjamapp.views.course_play_C, name='course_play_C'),  # play 게시글 C
    path('course_play_U/<str:id>/', jamjamapp.views.course_play_U,
         name='course_play_U'),  # play 게시글 수정
    path('course_play_delete/<str:id>/', jamjamapp.views.course_play_delete,
         name='course_play_delete'),  # play 게시글 삭제
    path('course_play_like/<int:pk>', jamjamapp.views.course_play_like,
         name='course_play_like'),  # play 게시글 좋아요
    path('bookmark/', include('bookmark.urls')),#북마크앱 url
    # ------민정 개발-------
    path('pay/', jamjamapp.views.pay, name='pay'),  # 결제 확인
    path('completepay/', jamjamapp.views.completepay, name='completepay'),  # 결제완료
    path('finalpay/', jamjamapp.views.finalpay, name='finalpay'),  # 진짜 결제
    path('day_detail/', jamjamapp.views.day_detail,
         name='day_detail'),  # 데이디테일 페이지
    path('diary/diary_create', jamjamapp.views.diary_create,
         name='diary_create'),  # 데이디테일 작성
    path('bucketlist_write/bucket_create/',
         jamjamapp.views.bucket_create, name='bucket_create'),  # 버킷리스트 작성
    path('diary_detail/<str:id>/', jamjamapp.views.diary_detail,
         name='diary_detail'),  # 데이디테일 디테일 페이지
    path('diary/diary_edit/', jamjamapp.views.diary_edit,
         name='diary_edit'),  # 데이디테일 수정(프론트)
    #     path('diary_edit/<str:id>/', jamjamapp.views.diary_edit,
    #          name='diary_edit'),  # 데이디테일 수정(백)
    path('profile_edit/', jamjamapp.views.profile_edit,
         name='profile_edit'),  # 프로필 수정(프론트)
    path('p_edit/<str:id>/', jamjamapp.views.p_edit, name='p_edit'),  # 프로필 수정(백)
    path('connection', jamjamapp.views.connection, name='connection'),  # 연인 연결
    path('purchaselist', jamjamapp.views.purchaselist,
         name='purchaselist'),  # 구매 목록 확인
    path('purchase_example/', jamjamapp.views.purchase_example,  # 아이템 자세히 보기
         name='purchase_example'),
    path('diary_delete/<str:id>/', jamjamapp.views.diary_delete,
         name='diary_delete'),  # 데이디테일 삭제
    path('profile/', jamjamapp.views.profile, name='profile'),  # 프로필 페이지
    path('bucketlist/', jamjamapp.views.bucketlist,
         name='bucketlist'),  # 버킷리스트 페이지
    path('bucket_edit/<str:id>', jamjamapp.views.bucket_edit,
         name='bucket_edit'),  # 버킷리스트 수정
    path('bucket_delete/<str:id>/', jamjamapp.views.bucket_delete,
         name='bucket_delete'),  # 버킷리스트 삭제
    path('bucket_detail/<str:id>/', jamjamapp.views.bucket_detail,
         name='bucket_detail'),  # 버킷리스트 디테일
    # ------예찬 개발-------
    path('login/', jamjamapp.views.signin, name='signin'),
    path('signup/', jamjamapp.views.signup, name='signup'),
    path('signout/', jamjamapp.views.signout, name='signout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
