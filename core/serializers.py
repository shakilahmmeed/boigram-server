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
    avg_rating = serializers.SerializerMethodField('get_avg_rating')

    class Meta:
        model = Book
        fields = '__all__'

    def check_is_rated(self, book):
        if 'user' in self.context:
            user = self.context['user']
            if user.is_authenticated:
                user_rated_book = user.rating_set.filter(book=book)
                return True if user_rated_book else False

    def get_avg_rating(self, book):
        ratings = book.rating_set.all()

        if ratings.count():
            rating_count = 0
            for rating in ratings:
                rating_count += rating.rating
            avg_rating = rating_count / ratings.count()
            return avg_rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
