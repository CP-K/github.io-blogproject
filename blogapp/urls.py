from django.urls import path
from . import views

#URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name='blogapp'

#URLパターンを登録するためのリスト
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path(
        'blog-detail/<int:pk>/',
        views.BlogDetail.as_view(),
        name='blog_detail'
    ),

    #placeカテゴリの一覧ページのURLパターン
    path(
        'place-list/',
        views.PlaceView.as_view(),
        name='place_list'
    ),

    #hobbyカテゴリの一覧ページのURLパターン
    path(
        'hobby-list/',
        views.HobbyView.as_view(),
        name='hobby_list'
    ),

    #bookカテゴリの一覧ページのURLパターン
    path(
        'book-list/',
        views.BookView.as_view(),
        name='book_list'
    ),

    #問い合わせページのURLパターン
    path(
        'contact/',
        views.ContactView.as_view(),
        name='contact'
    ),
]

