from rest_framework import serializers

from core.models import Book, Author, Category, Rating


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    is_rated = serializers.SerializerMethodField('check_is_rated')

    class Meta:
        model = Book
        fields = '__all__'

    def check_is_rated(self, book):
        if 'user' in self.context:
            user = self.context['user']
            if user.is_authenticated:
                user_rated_book = user.rating_set.filter(book=book)
                return True if user_rated_book else False


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
