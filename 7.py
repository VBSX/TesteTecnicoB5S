
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
    h = []
    unique_numbers = []
    repeated_number = []
    h.append(array[0])
    for number in array:
        if number in h:
            repeated_number.append(number)
            
        else:
            unique_numbers.append(number)
        h.append(number)
    return unique_numbers[0]

array = [2,2,3,1,1,6]
print(firstNonRepeatedValue(array))