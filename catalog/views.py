from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from catalog.models import Book
from catalog.permissions import BookCreatePermission
from catalog.serializers import BookDetailSerializer, BookListSerializer, BookCreateSerializer, BookUpdateSerializer, \
    BookDestroySerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = [IsAuthenticated]


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated]


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer
    permission_classes = [IsAuthenticated, BookCreatePermission]


class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDestroySerializer
    permission_classes = [IsAuthenticated, BookCreatePermission]
