from rest_framework import serializers
from .models import Users, Coords, Level, PerevalAdded, Images


class UsersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    fam = serializers.CharField(source='last_name')
    otc = serializers.CharField(source='surname')
    email = serializers.CharField()
    phone = serializers.CharField()

    class Meta:
        model = Users
        fields = ('email', 'fam', 'name', 'otc', 'phone')
        verbose_name = 'Пользователь'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'
        verbose_name = 'Координаты'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('image', 'title')
        verbose_name = 'Изображение'


class PerevalSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = PerevalAdded
        exclude = ('id', 'status')


class PerevalSubmitDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = '__all__'


class PerevalSubmitDataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ('fam', 'email', 'phone')


class PerevalSubmitDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


