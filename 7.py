
# /**
#  * The function must expect an array of integers and return the first non-repeated value.
#  * Ex: input: [2,2,3,1,1,6] - output: 3
#  *
#  * A função irá receber um array de inteiros e retornar o primeiro elemento não repetido.
#  * Ex: input: [2,2,3,1,1,6] - output: 3
#  *
#  * @param array $array - Array contendo inteiros
#  * @return int
#  */

def firstNonRepeatedValue(array):
    for number in array:
        
array = [2,2,3,1,1,6]
print(firstNonRepeatedValue(array))