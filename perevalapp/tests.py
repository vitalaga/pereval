import json
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Users
from .serializers import *


class CoordsApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.user_1 = Users.objects.create(
            email="Test1@mail.ru",
            name="Test1",
            fam="Test1",
            otc="Test1",
            phone="8-001-001-01-01"
        )
        self.user_2 = Users.objects.create(
            email="Test2@mail.ru",
            name="Test2",
            fam="Test2",
            otc="Test2",
            phone="8-002-002-02-02"
        )

    def test_get(self):
        url = reverse('user-list')
        response = self.client.get(url)
        serializer_data = UsersSerializer([self.user_1, self.user_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())
        self.assertEqual(len(serializer_data), 2)

    def test_get_detail(self):
        url = reverse('user-detail', args=(self.user_1.id,))
        response = self.client.get(url)
        serializer_data = UsersSerializer(self.user_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())

    def test_user_reuse(self):
        url = reverse('user-list')
        data = {
            'email': 'Test1@mail.ru',
            'name': 'Test1',
            'fam': 'Test1',
            'otc': 'Test1',
            'phone': '8-001-001-01-01'
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(2, Users.objects.all().count())

    def test_create(self):
        url = reverse('user-list')
        data = {
            'email': 'Test3@mail.ru',
            'name': 'Test3',
            'fam': 'Test3',
            'otc': 'Test3',
            'phone': '8-003-003-03-03'
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Users.objects.all().count())

class PerevalApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.pereval_1 = PerevalAdded.objects.create(
            user=Users.objects.create(
                email="Test1@mail.ru",
                name="Test1",
                fam="Test1",
                otc="Test1",
                phone="8-001-001-01-01"
            ),
            beauty_title="ПЕРЕВАЛ1",
            title="ПЕРЕВАЛ1",
            other_titles="ПЕРЕВАЛ1",
            connect='',
            coords=Coords.objects.create(
                latitude=49.000001,
                longitude=86.000001,
                height=3001
            ),
            level=Level.objects.create(
                winter='',
                summer='',
                autumn='',
                spring=''
            )
        )
        self.image_1_1 = Images.objects.create(
            image="https://pereval.ru/pereval1-1.jpg",
            title="pereval1-1",
            pereval=self.pereval_1
        )
        self.image_1_2 = Images.objects.create(
            image="https://pereval.ru/pereval1-2.jpg",
            title="pereval1-2",
            pereval=self.pereval_1
        )

        self.pereval_2 = PerevalAdded.objects.create(
            user=Users.objects.create(
                email="Test2@mail.ru",
                name="Test2",
                fam="Test2",
                otc="Test2",
                phone="8-002-002-02-02"
            ),
            beauty_title="ПЕРЕВАЛ2",
            title="ПЕРЕВАЛ2",
            other_titles="ПЕРЕВАЛ2",
            connect='',
            coords=Coords.objects.create(
                latitude=49.000002,
                longitude=86.000002,
                height=3002),
            level=Level.objects.create(
                winter='',
                summer='',
                autumn='',
                spring=''
            )
        )
        self.image_2_1 = Images.objects.create(
            image="https://pereval.ru/pereval2-1.jpg",
            title="pereval2-1",
            pereval=self.pereval_2
        )
        self.image_2_2 = Images.objects.create(
            image="https://pereval.ru/pereval2-2.jpg",
            title="pereval2-2",
            pereval=self.pereval_2
        )

        self.pereval_3 = PerevalAdded.objects.create(
            user=Users.objects.create(
                email="Test3@mail.ru",
                name="Test3",
                fam="Test3",
                otc="Test3",
                phone="8-003-003-03-03"
            ),
            beauty_title="ПЕРЕВАЛ3",
            title="ПЕРЕВАЛ3",
            other_titles="ПЕРЕВАЛ3",
            connect='',
            coords=Coords.objects.create(
                latitude=49.000003,
                longitude=86.000003,
                height=3003),
            level=Level.objects.create(
                winter='',
                summer='',
                autumn='',
                spring=''
            ),
            status='pending'
        )
        self.image_3_1 = Images.objects.create(
            image="https://pereval.ru/pereval3-1.jpg",
            title="pereval3-1",
            pereval=self.pereval_3
        )
        self.image_3_2 = Images.objects.create(
            image="https://pereval.ru/pereval3-2.jpg",
            title="pereval3-2",
            pereval=self.pereval_3
        )

    def test_get(self):
        url = reverse('pereval-list')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2, self.pereval_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())
        self.assertEqual(len(serializer_data), 3)

    def test_get_detail(self):
        url = reverse('pereval-detail', args=(self.pereval_1.id,))
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.json())

    def test_create_and_user_reuse(self):
        url = reverse('pereval-list')
        data = {
            'user': {
                'email': 'Test1@mail.ru',
                'name': 'Test1',
                'fam': 'Test1',
                'otc': 'Test1',
                'phone': '8-001-001-01-01'
            },
            'beauty_title': 'ПЕРЕВАЛ5',
            'title': 'ПЕРЕВАЛ5',
            'other_titles': 'ПЕРЕВАЛ5',
            'connect': '',
            'coords': {
                'latitude': 49.000005,
                'longitude': 86.000005,
                'height': 3005
            },
            'level': {
                'winter': '1A',
                'summer': '',
                'autumn': '1A',
                'spring': ''
            },
            'images': [
                {
                    'image': 'https://pereval.ru/pereval5-1.jpg',
                    'title': 'pereval5-1'
                },
                {
                    'image': 'https://pereval.ru/pereval5-2.jpg',
                    'title': 'pereval5-2'
                }
            ]
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(4, PerevalAdded.objects.all().count())
        self.assertEqual(3, Users.objects.all().count())

    def test_not_create(self):
        url = reverse('pereval-list')
        data = {
            'user': {
                'email': '',
                'name': '',
                'fam': '',
                'otc': '',
                'phone': ''
            },
            'beauty_title': '',
            'title': '',
            'other_titles': '',
            'connect': '',
            'coords': {
                'latitude': 49.000000,
                'longitude': 86.000000,
                'height': 3000
            },
            'level': {
                'winter': '',
                'summer': '',
                'autumn': '',
                'spring': ''
            },
            'images': [
                {
                    'image': '',
                    'title': ''
                },
                {
                    'image': '',
                    'title': ''
                }
            ]
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(3, PerevalAdded.objects.all().count())

    def test_update(self):
        url = reverse('pereval-detail', args=(self.pereval_1.id,))
        data = {
            'user': {
                'email': self.pereval_1.user.email,
                'name': self.pereval_1.user.name,
                'fam': self.pereval_1.user.fam,
                'otc': self.pereval_1.user.otc,
                'phone': self.pereval_1.user.phone
            },
            'beauty_title': self.pereval_1.beauty_title,
            'title': self.pereval_1.title,
            'other_titles': self.pereval_1.other_titles,
            'connect': 'Что-то соединяет',
            'coords': {
                'latitude': 49.444444,
                'longitude': 86.444444,
                'height': 3444
            },
            'level': {
                'winter': '1A',
                'summer': '1B',
                'autumn': '1C',
                'spring': '1D'
            },
            'images': [
                {
                    'image': 'https://pereval.ru/pereval1-1.jpg',
                    'title': 'pereval1-1'
                },
                {
                    'image': 'https://pereval.ru/pereval1-2.jpg',
                    'title': 'pereval1-2'
                }
            ],
            'status': 'pending'
        }
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.pereval_1.refresh_from_db()
        self.assertEqual(49.444444, self.pereval_1.coords.latitude)
        self.assertEqual(86.444444, self.pereval_1.coords.longitude)
        self.assertEqual(3444, self.pereval_1.coords.height)
        self.assertEqual('1A', self.pereval_1.level.winter)
        self.assertEqual('1B', self.pereval_1.level.summer)
        self.assertEqual('1C', self.pereval_1.level.autumn)
        self.assertEqual('1D', self.pereval_1.level.spring)
        self.assertEqual('pending', self.pereval_1.status)

    def test_update_not_status_new(self):
        url = reverse('pereval-detail', args=(self.pereval_3.id,))
        data = {
            'user': {
                'email': self.pereval_3.user.email,
                'name': self.pereval_3.user.name,
                'fam': self.pereval_3.user.fam,
                'otc': self.pereval_3.user.otc,
                'phone': self.pereval_3.user.phone
            },
            'beauty_title': self.pereval_3.beauty_title,
            'title': self.pereval_3.title,
            'other_titles': self.pereval_3.other_titles,
            'connect': '',
            'coords': {
                'latitude': 49.333333,
                'longitude': 86.333333,
                'height': 3333
            },
            'level': {
                'winter': '',
                'summer': '',
                'autumn': '',
                'spring': ''
            },
            'images': [
                {
                    'image': 'https://pereval.ru/pereval3-1.jpg',
                    'title': 'pereval3-1'
                },
                {
                    'image': 'https://pereval.ru/pereval3-2.jpg',
                    'title': 'pereval3-2'
                }
            ]
        }
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.pereval_1.refresh_from_db()
        self.assertEqual(49.000003, self.pereval_3.coords.latitude)
        self.assertEqual(86.000003, self.pereval_3.coords.longitude)
        self.assertEqual(3003, self.pereval_3.coords.height)

    def test_user_update(self):
        url = reverse('pereval-detail', args=(self.pereval_2.id,))
        data = {
            'user': {
                'email': 'Test2@mail.ru',
                'name': 'Test2',
                'fam': 'Test2',
                'otc': 'Test2',
                'phone': '8-002-002-02-02'
            },
            'beauty_title': 'ПЕРЕВАЛ2',
            'title': 'ПЕРЕВАЛ2',
            'other_titles': 'ПЕРЕВАЛ2',
            'connect': '',
            'coords': {
                'latitude': 49.000002,
                'longitude': 86.000002,
                'height': 3002
            },
            'level': {
                'winter': '',
                'summer': '',
                'autumn': '',
                'spring': ''
            },
            'images': [
                {
                    'image': 'https://pereval.ru/pereval2-1.jpg',
                    'title': 'pereval2-1'
                },
                {
                    'image': 'https://pereval.ru/pereval2-2.jpg',
                    'title': 'pereval2-2'
                }
            ]
        }
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.pereval_1.refresh_from_db()
        self.assertEqual('Test2@mail.ru', self.pereval_2.user.email)
        self.assertEqual('Test2', self.pereval_2.user.name)
        self.assertEqual('Test2', self.pereval_2.user.fam)
        self.assertEqual('Test2', self.pereval_2.user.otc)
        self.assertEqual('8-002-002-02-02', self.pereval_2.user.phone)


class PerevalSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.pereval_1 = PerevalAdded.objects.create(
            user=Users.objects.create(
                email="Test1@mail.ru",
                name="Test1",
                fam="Test1",
                otc="Test1",
                phone="8-001-001-01-01"
            ),
            beauty_title="ПЕРЕВАЛ1",
            title="ПЕРЕВАЛ1",
            other_titles="ПЕРЕВАЛ1",
            connect='',
            coords=Coords.objects.create(
                latitude=49.000001,
                longitude=86.000001,
                height=3001
            ),
            level=Level.objects.create(
                winter='',
                summer='',
                autumn='',
                spring=''
            )
        )
        self.image_1_1 = Images.objects.create(
            image="https://pereval.ru/pereval1-1.jpg",
            title="pereval1-1",
            pereval=self.pereval_1
        )
        self.image_1_2 = Images.objects.create(
            image="https://pereval.ru/pereval1-2.jpg",
            title="pereval1-2",
            pereval=self.pereval_1
        )

        self.pereval_2 = PerevalAdded.objects.create(
            user=Users.objects.create(
                email="Test2@mail.ru",
                name="Test2",
                fam="Test2",
                otc="Test2",
                phone="8-002-002-02-02"
            ),
            beauty_title="ПЕРЕВАЛ2",
            title="ПЕРЕВАЛ2",
            other_titles="ПЕРЕВАЛ2", connect='',
            coords=Coords.objects.create(
                latitude=49.000002,
                longitude=86.000002,
                height=3002),
            level=Level.objects.create(
                winter='',
                summer='',
                autumn='',
                spring=''
            )
        )
        self.image_2_1 = Images.objects.create(
            image="https://pereval.ru/pereval2-1.jpg",
            title="pereval2-1",
            pereval=self.pereval_2
        )
        self.image_2_2 = Images.objects.create(
            image="https://pereval.ru/pereval2-2.jpg",
            title="pereval2-2",
            pereval=self.pereval_2
        )

    def test_ok(self):
        data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        expected_data = [
            {
                'id': self.pereval_1.id,
                'user': {
                    'email': 'Test1@mail.ru',
                    'name': 'Test1',
                    'fam': 'Test1',
                    'otc': 'Test1',
                    'phone': '8-001-001-01-01'
                },
                'beauty_title': 'ПЕРЕВАЛ1',
                'title': 'ПЕРЕВАЛ1',
                'other_titles': 'ПЕРЕВАЛ1',
                'connect': '',
                'coords': {
                    'latitude': 49.000001,
                    'longitude': 86.000001,
                    'height': 3001
                },
                'level': {
                    'winter': '',
                    'summer': '',
                    'autumn': '',
                    'spring': ''
                },
                'images': [
                    {
                        'image': 'https://pereval.ru/pereval1-1.jpg',
                        'title': 'pereval1-1'
                    },
                    {
                        'image': 'https://pereval.ru/pereval1-2.jpg',
                        'title': 'pereval1-2'
                    }
                ],
                'status': 'new'
            },
            {
                'id': self.pereval_2.id,
                'user': {
                    'email': 'Test2@mail.ru',
                    'name': 'Test2',
                    'fam': 'Test2',
                    'otc': 'Test2',
                    'phone': '8-002-002-02-02'
                },
                'beauty_title': 'ПЕРЕВАЛ2',
                'title': 'ПЕРЕВАЛ2',
                'other_titles': 'ПЕРЕВАЛ2',
                'connect': '',
                'coords': {
                    'latitude': 49.000002,
                    'longitude': 86.000002,
                    'height': 3002
                },
                'level': {
                    'winter': '',
                    'summer': '',
                    'autumn': '',
                    'spring': ''
                },
                'images': [
                    {
                        'image': 'https://pereval.ru/pereval2-1.jpg',
                        'title': 'pereval2-1'
                    },
                    {
                        'image': 'https://pereval.ru/pereval2-2.jpg',
                        'title': 'pereval2-2'
                    }
                ],
                'status': 'new'
            }
        ]
        self.assertEqual(expected_data, data)
