soma = 0
quantidade = 0

while True:
    n = int(input("Digite aqui um número inteiro:"))
    if n==0:
        break
    soma = soma + n
    quantidade = quantidade + 1
    print("Quantidade de números digitados:", quantidade)
    print("Soma: ", soma)
    print("Média: %10.2f" % (soma/quantidade))
    


    
    

