from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Book, Category
from core.serializers import BookSerializer, CategorySerializer, RatingSerializer


class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class SingleBookView(APIView):
    def get(self, request, book_slug):
        practice = Book.objects.get(slug=book_slug)
        serializer = BookSerializer(practice, context={'user': request.user})
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


class RatingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.data['user'] = request.user.id

        rating_serializer = RatingSerializer(data=request.data)

        if rating_serializer.is_valid():
            rating_serializer.save()
            return Response(rating_serializer.data)

        return Response(rating_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
