import unittest
from count_utils import count_vowels

class CountVowels(unittest.TestCase):

    #Teste usando um valor numérico como entrada.
    def test_number(self):
        with self.assertRaises(TypeError):
            count_vowels(0)
    # Teste usando None como entrada.
    def test_none(self):
        with self.assertRaises(TypeError):
            count_vowels(None)
    #Teste com uma String vazia.
    def test_empty_string(self):
         self.assertEqual(count_vowels(""), 0)
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

    # Teste que apenas as vogais sem acento são contabilizadas.
    def test_accented_vowels(self):
        self.assertEqual(count_vowels("áéíóú"), 0)

    # Teste se vogais repetidas são contabilizadas individualmente.
    def test_repeated_vowels(self):
        self.assertEqual(count_vowels("banana"), 3)

if __name__ == '__main__':
    unittest.main()
