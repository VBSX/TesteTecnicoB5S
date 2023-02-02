
# /**
#  * The function should expect an array containing integers greater than zero and return the amount of even values contained in it.
#  * Ex: input: [1,2,3,4,5] - output: 2
#  *
#  * Recebe um array de inteiros maiores que zero e retorna a quantidade de números pares existentes no array
#  * Ex: input: [1,2,3,4,5] - output: 2
#  *
#  * @param array $array
#  * @return int
#  */

def oddOrEven(number):
    odd = 0
    for itens_in_array in number:
        modulus = itens_in_array % 2
        if modulus == 0:
            odd += 1

    
    return odd
        
array = []

for number in  range(0,4):
    
    array.append(int(input('coloque um numero: ')))


print(oddOrEven(array))