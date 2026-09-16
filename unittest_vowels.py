import unittest
from count_utils import count_vowels

class CountVowels(unittest.TestCase):

    #Teste com uma String vazia.
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)
    #Teste usando um valor numérico como entrada, caso a entrada cause um TypeError, está correto.
    def test_number(self):
        with self.assertRaises(TypeError):
            count_vowels(0)
    #Teste se não há vogais.
    def test_no_vowels(self):
        self.assertEqual(count_vowels("wxyz"), 0)

    # Teste se símbolos são ignorados sem interferir na contagem das vogais.
    def test_symbols(self):
        self.assertEqual(count_vowels("a!e@i#o$u%"), 5)

    # Teste com letras maiúsculas e minúsculas.
    def test_upper_lower_case(self):
        self.assertEqual(count_vowels("OpenAI"), 4)

    # Teste com uma frase próxima de uma entrada real da aplicação.
    def test_sentence(self):
        self.assertEqual(count_vowels("aeiouaeiouaeiou"), 15)

if __name__ == '__main__':
    unittest.main()
    
#ou: 'python3 -m unittest unittest_vowels.py -v' no terminal para exibir cada teste separadamente.
#'python3 -m coverage run -m unittest unittest_vowels.py' e depois 'python3 -m coverage report' para exibir a porcentagem de cobertura no trabalho.
