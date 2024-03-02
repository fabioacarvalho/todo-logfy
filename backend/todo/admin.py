from django.contrib import admin
from todo.models import *


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creatable', 'done', 'created_at',)
    list_filter = ('id', 'title', 'creatable', 'done', 'created_at',)
    search_fields = ('id', 'title', 'creatable', 'done', 'created_at',)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'board_list', 'title', 'content', 'user', 'created', 'status', 'labels',)
    list_filter = ('id', 'board_list', 'title', 'content', 'user', 'created', 'status', 'labels',)
    search_fields = ('id', 'board_list', 'title', 'content', 'user', 'created', 'status', 'labels',)
