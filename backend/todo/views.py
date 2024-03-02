from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from todo.models import *
from todo.serializers import *
from django.shortcuts import get_object_or_404 as getor404, redirect
from datetime import datetime
from django.urls import reverse


def index(request):
    # Use reverse para obter o caminho da URL de administração
    admin_url = reverse('admin:index')

    # Redirecione para a URL de administração
    return redirect(admin_url)


class BoardListView(APIView):
    def get(self, request, format=None):
        boards = Board.objects.all()
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateBoardView(APIView):
    def post(self, request, format=None):
        serializer = CreateBoardSerializer(data=request.data)
        if serializer.is_valid():
            has_board = Board.objects.filter(done=True).count()
            board = Board(
                title=serializer.validated_data.get('title'),
                creatable=serializer.validated_data.get('creatable'),
                done=serializer.validated_data.get('done'),
            )
            board.save()
            board_serializer = BoardListSerializer(board, many=False)
            return Response(board_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardListView(APIView):
    def get(self, request, format=None):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateCardView(APIView):
    def post(self, request, id, format=None):
        board = getor404(Board, pk=id)
        serializer = CreateCardSerializer(data=request.data)
        if serializer.is_valid():
            card = Card(
                board_list=board,
                title=serializer.validated_data.get('title'),
                content=serializer.validated_data.get('content'),
                created=datetime.now(),
                status=serializer.validated_data.get('status'),
                labels=serializer.validated_data.get('labels'),
            )
            card.save()
            card_serializer = CardSerializer(card, many=False)
            return Response(card_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
