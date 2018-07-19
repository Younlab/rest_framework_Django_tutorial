import json
import random

from django.test import TestCase
from rest_framework import status

from rest_framework.renderers import JSONRenderer
from rest_framework.test import APITestCase

from snippets.models import Snippet


class SnippetListTest(APITestCase):
    def test_status_code(self):
        """
        요청 결과의 HTTP상태코드가 200인지 확인
        :return:
        """
        response = self.client.get('/snippets/django_view/snippets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_snippet_list_count(self):
        """
        Snippet List 를 요청시 DB에 있는 자료수와 같은 갯수가 리턴되는지 확인
            response (self.client.get 요청한 결과)에 온 데이터의 길이와
            django Orm 을 이용한 querySet의 갯수가 같은지 확인
        :return:
        """
        for i in range(random.randint(10, 100)):
            Snippet.objects.create(code=f'a={i}')
        response = self.client.get('/snippets/django_view/snippets/')
        orm = Snippet.objects.all()
        data = json.loads(response.content)
        # response 로 받은 json데이터의 길이와
        # Snippet 테이블의 자료수가 같은지
        print(len(orm))
        print(len(data))
        self.assertEqual(len(data), Snippet.objects.count())

    def test_snippet_list_order_by_created_descending(self):
        """
        Snippet List의 결과가 생성일자 내림차순인지 확인
        :return:
        """
        for i in range(random.randint(10, 100)):
            Snippet.objects.create(code=f'a={i}')
        response = self.client.get('/snippets/django_view/snippets/')
        data = json.loads(response.content)
        # response에 전달된 JSON string을 파싱은 python객체를 순홰ㅣ하며 'pk'값만 꺼냄
        # Snippet.objects.order_by('-created') Queryset 을 순회하며 각 Snippet인스턴스의 pk값만 꺼냄
        self.assertEqual(
            # JSON으로 전달받은 데이터에서 pk만 꺼낸 리스트
            [item['pk'] for item in data],
            # DB에서 created역순으로 pk값만 가져온QuerySet으로 만든 리스트
            list(Snippet.objects.order_by('-created').values_list('pk', flat=True))
        )

class SnippetCreateTest(APITestCase):
    def test_snippet_create_status_code(self):
        """
        201이 돌아오는지
        :return:
        """
        pass

    def test_snippet_create_save_db(self):
        """
        요청 후 실제 DB에 저장되었는지 (모든 필드값이 정상적으로 저장되는지)
        :return:
        """
        pass

    def test_snippet_create_missnig_code_raise_exception(self):
        """
        'code' 데이터가 주어지지 않을경우 적절한 Exception 이 발생하는지
        :return:
        """
        pass