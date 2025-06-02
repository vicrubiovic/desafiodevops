import unittest
from app import app
import werkzeug

# Patch temporário para adicionar o atributo '__version__' em
werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
    # Criação do cliente de teste
        cls.client = app.test_client()

    #teste para verificar se os valores estão diferentes 
    def teste_home_Not_Found(self):
        response = self.client.get('/')
        self.assertNotEqual(response.status_code, 404) 
        self.assertNotEqual(response.json, {"error": "Not Found"})  
    
    #teste para verificar se o retorno dos itens esta certo.
    def test_items(self): 
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"items": ["item1", "item2", "item3"]})
    
    #teste para verificar o funcionamento do token e depois vai verificar se o token é uma string
    def teste_login_token_tipo(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)
        self.assertIsInstance(response.json['access_token'], str)



if __name__ == '__main__':unittest.main()