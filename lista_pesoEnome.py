lista= []
temp=[]
mai=meno=0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(lista)==0:
        mai=meno= temp[1]
    else:
        if temp[1]>mai:
            mai=temp[1]
        if temp[1]<meno:
            meno=temp[1]
    
    lista.append(temp[:])
    temp.clear()
    opcao=str(input('Quer continuar? [S/N] '))
    if opcao in'Nn':
        break
    
print(f'=='*25)

#print(f'Os dados foram {lista}')

#Quantidade de cadastros
print(f'A quantidade de cadastros que foram feitos foi de: {len(lista)} pessoas')

#maior e menor peso
print(f'O maior peso é de: {mai}kg e o menor peso é de: {meno}kg')

print('=='*25) 
#As pessoas com maior peso(lista)
print('As pessoas com maior pesos são:')  
for p in lista:
    if p[1]==mai:
        print(f'{p[0]}')
print('=='*25) 
#As pessoas com menores peso(lista) 
print('As pessoas com menores pesos são:')  
for p in lista:
    if p[1]==meno:
        print(f'{p[0]}')
        
   
