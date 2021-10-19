#main.py desafio 1 e 3
from Pessoa import *

def hello():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: ")
    cidade = input("Digite sua cidade: ")
    estado = input("Digite seu Estado: ")
    return nome, idade, sexo, cidade, estado


print(hello())

pessoa = Pessoa(input("Digite seu nome: "), int(input("Digite sua idade: " )), input("Digite seu sexo: "),
input("Digite sua cidade: "), input("Digite seu Estado: "))

print(pessoa.Nome)