num = int(input('Digite um numero entre 0 e 9999: '))
milhar = int((num/1000)%10)
centena = int((num/100)%10)
dezena = int((num/10)%10)
unidade = int(num%10)
print(f'milhar: {milhar}\ncentena: {centena}\ndezena: {dezena}\nunidade: {unidade}')
#print(f'A casa dos milhares do seu numero é : {num[0]} \n a das centenas é : {num[1]} \n a das dezenas é {num[2]}, \n e a das unidades: {num[3]} ')
