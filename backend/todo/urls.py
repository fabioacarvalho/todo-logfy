from django.contrib import admin
from django.urls import path
from todo.views import *


urlpatterns = [
    path('board/', BoardListView.as_view(), name='board'),
    path('cards/', CardListView.as_view(), name='card'),
    path('cards/<int:id>/card/', CreateCardView.as_view(), name='card_create'),
    path('boards/board-create/', CreateBoardView.as_view(), name='board_create'),
]
