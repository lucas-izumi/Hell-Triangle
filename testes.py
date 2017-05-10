from helltriangle import *
import unittest

class UnidadeTestes(unittest.TestCase):
    def setUp(self):
        self.numLinhas = 4
        self.exemplo = [[6], [3,5], [9, 7, 1], [4, 6, 8, 4]]

    # Testa para qualquer caso em que o numero de linhas informado
    # seja maior que o numero de linhas do triangulo.
    def test_numero_linhas_maior_triangulo(self):
        with self.assertRaises(ErroLinhaMaiorTriangulo) as context_manager:
            HellTriangle(self.numLinhas*2, self.exemplo)

        error = context_manager.exception
        self.assertEqual(error.error, 'Numero de linhas informado nao corresponde ao numero de linhas do triangulo')

    # Utiliza o exemplo do pdf e testa se o caminho escolhido é o correto
    # exibindo o máximo total
    def test_sucesso(self):
        resultado = HellTriangle(self.numLinhas, self.exemplo)
        self.assertEqual(resultado, 26)

    # Testa se o numero de linhas informado é menor ou igual a zero
    def test_linhas_invalidas(self):
        with self.assertRaises(ErroLinhasInvalidas) as context_manager:
            HellTriangle(-1, self.exemplo)

        error = context_manager.exception
        self.assertEqual(error.error, 'Numero de linhas invalido. Insira um valor de linhas maior que zero')

    # Testa se o triangulo possui uma configuração valida
    # (Cada linha deve possuir um elemento a mais que a linha anterior)
    def test_triangulo_valido(self):
        with self.assertRaises(ErroTrianguloInvalido) as context_manager:
            HellTriangle(self.numLinhas, [[6], [3], [9, 7, 1], [4, 6, 8]])

        error = context_manager.exception
        self.assertEqual(error.error, 'Triangulo invalido. Encerrando execução')

if __name__ == '__main__':
    unittest.main()
