from rest_framework import serializers
from .models import Users, Coords, Level, PerevalAdded, Images
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'fam', 'otc', 'email', 'phone')

    def save(self, **kwargs):
        self.is_valid()
        users = Users.objects.filter(email=self.validated_data.get('email'))
        if users.exists():
            return users.first()
        else:
            return Users.objects.create(
                name=self.validated_data.get('name'),
                fam=self.validated_data.get('fam'),
                otc=self.validated_data.get('otc'),
                email=self.validated_data.get('email'),
                phone=self.validated_data.get('phone'),
            )


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height',)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring',)


class ImagesSerializer(serializers.ModelSerializer):
    data = serializers.URLField()

    class Meta:
        model = Images
        fields = ('data', 'title')


class PerevalSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)

    class Meta:
        model = PerevalAdded
        depth = 1
        fields = (
            'id', 'user', 'beauty_title', 'title', 'other_titles', 'connect', 'coords', 'level', 'images', 'status'
        )

    def create(self, validated_data, **kwargs):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        pass_user = Users.objects.filter(email=user['email'])
        if pass_user.exists():
            user_serializer = UsersSerializer(data=user)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
        else:
            user = Users.objects.create(**user)

        coords = Coords.objects.create(**coords)
        level = Level.objects.create(**level)
        pereval = PerevalAdded.objects.create(**validated_data, user=user, coords=coords, level=level, status='new')

        for image in images:
            data = image.pop('data')
            title = image.pop('title')
            Images.objects.create(data=data, pereval=pereval, title=title)

        return pereval

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            validating_user_fields = [
                instance_user.name != data_user['name'],
                instance_user.fam != data_user['fam'],
                instance_user.otc != data_user['otc'],
                instance_user.phone != data_user['phone'],
                instance_user.email != data_user['email'],
                ]
            if data_user is not None and any(validating_user_fields):
                raise serializers.ValidationError({'Отклонено': 'Нельзя изменять данные пользователя'})
        return data




