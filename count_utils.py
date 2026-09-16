def count_vowels(s):
    #Checa se é uma string.
    if not isinstance(s, str):
        #TypeError, caso não seja.
        raise TypeError("Expected a String")
    #Transforma a string em letras minúsculas e checa se as vogais está presente.
    return sum(1 for c in s.lower() if c in "aeiou")