import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_listar_alunos(self):
        response = self.app.get('/alunos')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_cadastrar_aluno(self):
        novo_aluno = {
            'aluno_id': 1,
            'nome': 'João Silva',
            'endereco': 'Rua A',
            'cidade': 'Cidade B',
            'estado': 'Estado C',
            'cep': '12345-678',
            'pais': 'Brasil',
            'telefone': '123456789'
        }
        response = self.app.post('/alunos', data=json.dumps(novo_aluno), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('aluno_id', response.json)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()