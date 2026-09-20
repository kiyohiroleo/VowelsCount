# VowelsCount

Aplicação simples em Python que conta as vogais de um texto. O projeto contém uma
função de contagem em `count_utils.py`, uma interface web em Flask em `app.py` e
testes unitários em `unittest_vowels.py`.

O projeto foi utilizado na Trilha B - Aplicação + Testes Unitários da disciplina de
Teste e Validação de Sistemas.

## Tecnologias

- Python 3
- Flask
- `unittest`
- Coverage.py

## Executando a aplicação

Instale o Flask:

```bash
python -m pip install flask
```

Inicie a aplicação:

```bash
python app.py
```

Depois, acesse `http://localhost:5000` no navegador.

## Executando os testes

Na pasta do projeto, execute:

```bash
python -m unittest unittest_vowels.py -v
```

## Casos de teste

| Caso | Entrada | Resultado esperado | Objetivo |
| --- | --- | ---: | --- |
| String vazia | `""` | `0` | Verificar o valor limite sem caracteres. |
| Valor numérico | `0` | `TypeError` | Rejeitar uma entrada que não seja texto. |
| Texto sem vogais | `"wxyz"` | `0` | Verificar uma classe válida sem ocorrências. |
| Vogais e símbolos | `"a!e@i#o$u%"` | `5` | Confirmar que símbolos não alteram a contagem. |
| Maiúsculas e minúsculas | `"OpenAI"` | `4` | Confirmar que a contagem não diferencia maiúsculas de minúsculas. |
| Sequência de vogais | `"aeiouaeiouaeiou"` | `15` | Confirmar a contagem de uma sequência formada apenas por vogais. |
| Valor nulo | `None` | `TypeError` | Rejeitar outra entrada que não seja texto. |
| Vogais acentuadas | `"áéíóú"` | `0` | Documentar que a função considera apenas as vogais sem acento (`aeiou`). |
| Vogais repetidas | `"banana"` | `3` | Confirmar que cada ocorrência repetida é contabilizada. |

Os casos exercitam os fluxos da função `count_vowels`: validação do tipo da entrada,
normalização de maiúsculas e minúsculas, seleção dos caracteres que pertencem ao
conjunto `aeiou` e retorno da soma. Entradas válidas, inválidas e valores de limite
são usados para verificar os principais caminhos da implementação.

## Cobertura

Instale a ferramenta de cobertura:

```bash
python -m pip install coverage
```

Execute a suíte medindo especificamente o módulo que contém a funcionalidade:

```bash
python -m coverage run --source=count_utils -m unittest unittest_vowels.py
python -m coverage report -m
```

Resultado obtido após a execução dos nove testes:

```text
Name             Stmts   Miss  Cover
------------------------------------
count_utils.py       4      0   100%
------------------------------------
TOTAL                4      0   100%
```

A cobertura de 100% do módulo testado supera o mínimo de 80% exigido pela Trilha B.
