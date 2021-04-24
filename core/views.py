from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Book, Category
from core.serializers import BookSerializer, CategorySerializer


class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class SingleBookView(APIView):
    def get(self, request, book_slug):
        practice = Book.objects.get(slug=book_slug)
        serializer = BookSerializer(practice)
        return Response(serializer.data)


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class SearchView(APIView):
    def get(self, request):
        query = request.GET.get('q')
        books = Book.objects.filter(title__icontains=query)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
