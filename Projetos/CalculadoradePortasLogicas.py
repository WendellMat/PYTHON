import ttg

#Instruções 

print("\nInstruções para utilização da calculadora:")
print("Utilize letras  maiúsculas para as variáveis")
print("Troque o 'e','^' ou '*' por: and")
print("Troque o 'ou','v' ou '+' por: or")
print("Troque o 'não','~' ou '-' por: not")
print("Troque o 'não e' por: nand")
print("Troque o 'não ou' por: nor")
print("Troque o 'ou exclusivo' por: xor")
print("Troque o 'não ou exclusivo' por: nxor")
print("\nFUNCIONA MUITO BEM COM ATÉ 5 VARIÁVEIS, MAIS DO QUE ISSO ELE APRESENTA ERROS, MAS SINTA-SE A VONTADE PARA TESTAR")

# Defina sua expressão lógica
expressao = input("\nDigite a expressão que você deseja: ")
quantvar = int(input("Quantas variáveis existem na expressão? " ))

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
elementos = alfabeto[0:quantvar]

# Crie um objeto TruthTable com a expressão lógica
tabela_verdade = ttg.Truths(elementos, [expressao])

# Imprima a tabela verdade
print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("!!!!                                                          !!!!")
print("!!!!  LEMBRE-SE DE ESCREVER OS RESULTADOS DE BAIXO PARA CIMA  !!!!")
print("!!!!                                                          !!!!")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(tabela_verdade)