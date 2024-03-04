from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueValidator

from catalog.models import Book


class CustomSlugRelatedField(serializers.SlugRelatedField):
    def __init__(self, *args, additional_field=None, **kwargs):
        self.additional_field = additional_field
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        representation = super().to_representation(value)
        if self.additional_field:
            additional_value = getattr(value, self.additional_field)
            representation = f"{additional_value} {representation}"
        return representation


class BookListSerializer(serializers.ModelSerializer):
    language = serializers.CharField()
    genre = serializers.CharField()
    author = CustomSlugRelatedField(
        many=True,
        read_only=True,
        slug_field="last_name",
        additional_field="first_name"
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'genre', 'language', 'description', 'inprint', 'publication_year', 'ISBN', 'author']


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)  # не обязательное поле

    title = serializers.CharField(
        max_length=200,
        validators=([UniqueValidator(queryset=Book.objects.all())])
    )

    class Meta:
        model = Book
        fields = ["id", "title", "description"]


class BookUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)  # не обязательное поле

    class Meta:
        model = Book
        fields = ["id", "title", "description"]


class BookDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id"]
