from collections import deque

fila = deque([]) #R2 - Que os números sejam armazenados em fila
def enfileirar(): #R6 - Criar uma função para enfileirar 
    while True:
        valor = int(input('>>>'))
        if valor > 0: #R1 - Leia apenas números maiores que zero
            fila.append(valor) #R2 - Que os números sejam armazenados em fila
            capacidade = fila.__len__() #R3 - A fila deve ter um limite de quantidade
            if capacidade < 5: #R3 - A fila deve ter um limite de quantidade
                print('Escolha aceita')
            else:
                print('Fila cheia')
                break
        else: #R4 - A fila não deve aceitar números negativos ou nulos
            print('Escolha inválida, digite um número maior que 0(zero).')

def desenfileirar(): #R7 - Criar uma função para desenfileirar
    print('Tecle ENTER para desenfileirar apenas os números PARES.')
    iniciar = str(input('>>>'))
    print('Os números pares são: ', end=' ')
    for x in fila: #R5 - É preciso ter uma funcionalidade para desenfileirar exibindo apenas os números pares
        if x % 2 == 0:
            print('|',x,'|', end=' ')