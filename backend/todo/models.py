from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=300)
    creatable = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Board List"
        verbose_name_plural = "Board Lists"

    def __str__(self):
        return self.title


class Card(models.Model):
    board_list = models.ForeignKey("todo.Board", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=(('pending', 'Pending'), ('draft', 'Draft'), ('wait', 'Wait'), ('done', 'Done')), default='draft')
    labels = models.TextField(blank=True)

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"

    def __str__(self):
        return f"{self.board_list.title} - {self.title}"
