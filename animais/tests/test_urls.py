from django.test import TestCase, RequestFactory
from django.urls import reverse # identifica qual url está sendo utilizada
from animais.views import index


class AnimaisURLSTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_utiliza_view_index(self):
        """ Teste se a home da aplicação utiliza a função index """
        request = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)
