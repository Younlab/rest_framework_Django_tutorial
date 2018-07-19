import json
import random

from django.test import TestCase
from rest_framework import status
from rest_framework.parsers import JSONParser
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
        snippets = Snippet.objects.order_by('-created')

        # response에 전달된 JSON string을 파싱은 python객체를 순홰ㅣ하며 'pk'값만 꺼냄
        data_pk_list = []
        for item in data:
            data_pk_list.append(item['pk'])

        # Snippet.objects.order_by('-created') Queryset 을 순회하며 각 Snippet인스턴스의 pk값만 꺼냄
        snippets_pk_list = []
        for item in snippets:
            snippets_pk_list.append(item.pk)

        self.assertEqual(data_pk_list, snippets_pk_list)