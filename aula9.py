# Total = preço × quantidade
# Desconto = total × 0.10
# Valor final = total - desconto
quantidade = int(input("Quantos produtos?:> "))
preco = float(input("Qual é o preço?:> "))
total = preco * quantidade
if total >= 200:
    desconto = total * 0.20
elif total >= 100:
    desconto = total * 0.10
else:
    desconto = 0
valor_final = total - desconto
print("-="*10)
print("Total:", total, "R$")
print("Desconto:", desconto, "R$")
print("Valor Final:", valor_final, "R$")
