print("Qual o nome do heroi?")
nome = input()
print("Quanto de experiencia o heroi tem?")
xp = int(input())
rank = str
if(xp <= 1000):
    rank = "Ferro"
elif(xp <= 2000):
    rank = "Bronze"
elif(xp <= 5000):
    rank = "Prata"
elif(xp <= 7000):
    rank = "Ouro"
elif(xp <= 8000):
    rank = "Platina"
elif(xp <= 9000):
    rank = "Ascendente"
elif(xp <= 10000):
    rank = "Imortal"
else:
    rank = "Radiante"

print(f"O heroi de nome {nome} está no nivel de {rank}")