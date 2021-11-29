from django.urls import path
import bookmark.views
from .views import *
urlpatterns = [
    # path('', bookmark.views.bookmark_category, name='bookmark_category'),
    # path('<int:book_category_id>/bookmark_list/', 
    #      bookmark.views.bookmark_list, name='bookmark_list'),
    # path('bookmark_update/<int:pk>/',
    #      BookmarkUpdate.as_view(), name='bookmark_update'),
    # path('bookmark_delete/<int:pk>/',
    #      BookmarkDelete.as_view(), name='bookmark_delete'),
    # path('bookmark_create/', BookmarkCreate.as_view(), name='bookmark_create'),
    # path('bookmark_detail/<int:pk>/',
    #      BookmarkDetail.as_view(), name='bookmark_detail'),

    path('', bookmark.views.bookmark_category,
         name='bookmark_category'),  # 북마크 메인
    path('<int:book_category_id>/bookmark_list/', bookmark.views.bookmark_list,
         name='bookmark_list'),  # 북마크 리스트
    path('bookmark_create/', BookmarkCreate.as_view(),
         name='bookmark_create'),  # url 추가 확인
    path('bookmark_detail/<int:pk>/', BookmarkDetail.as_view(),
         name='bookmark_detail'),  # 북마크 추가
    path('bookmark_update/<int:pk>/', BookmarkUpdate.as_view(),
         name='bookmark_update'),  # 북마크 수정
    path('bookmark_delete/<int:pk>/', BookmarkDelete.as_view(),
         name='bookmark_delete'),  # 북마크 삭제 확인

]
