# -*- coding: utf-8 -*-
"""Introdução a Programação - 06/09/21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sz321EGOfISDEscazddrbC7A8iTEqBVR
"""

import requests
import json

#Requisição da cotação atual do dólar
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")


#Valor do dólar em real, mas ainda em string
cotacoes = cotacoes.json()
cotacao_d = cotacoes ['USDBRL']['bid']
cotacao_d = float(cotacao_d)

#Convertendo string para float e deixando apenas com duas unidades após a casa decimal
cotacao_d = round(cotacao_d, 2)

#variáveis constantes
dolar = cotacao_d
produtoPerfume = 100
produtoCamisaPolo = 20
produtoTenisNike = 25

#Enquanto a variável check for diferente de "sim", ele pedirá para que haja novamente a entrada da porcentagem de lucros desejada
lucroDesejado = "0"
check = "0"
while check != "sim":
  #Entrada
  lucroDesejado = int(input("Digite a porcentagem de lucro que você deseja obter, com base nos valores dos produtos(apenas números): "))
  print('\n')
  #Confirmação de entrada
  check = input("Você digitou o valor {0}%. Certo? Responda apenas com Sim ou Não: ".format(lucroDesejado)).lower()
  print('\n')

#Conversão dos preços dos produtos para real
perfumeReal = produtoPerfume * dolar
camisaPoloReal = produtoCamisaPolo * dolar
tenisNikeReal = produtoTenisNike * dolar

#Colocando a porcentagem de lucro que o dono deseja
perfumeRealFinal = perfumeReal * (1 + (lucroDesejado/100))
camisaPoloRealFinal = camisaPoloReal * (1 + (lucroDesejado/100))
tenisNikeRealFinal = tenisNikeReal * (1 + (lucroDesejado/100))

#Apresentação de valores em real sem a adição de lucros
print("Valores dos produtos em real, sem adição de lucros:")
print("Perfume: R${0}".format(round(perfumeReal,2)))
print("Camisa Polo: R${0}".format(round(camisaPoloReal,2)))
print("Tênis Nike: R${0}".format(round(tenisNikeReal,2)))
print('\n')

#Apresentação de valores em real com a adição de lucros
print("Valores dos produtos em real, com adição de lucros:")
print("Perfume: R${0}".format(round(perfumeRealFinal,2)))
print("Camisa Polo: R${0}".format(round(camisaPoloRealFinal,2)))
print("Tênis Nike: R${0}".format(round(tenisNikeRealFinal,2)))
print('\n')
print("O dólar hoje está custando R${}".format(dolar))
