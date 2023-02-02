# /**
#  * The function should recive an array with at least 3 itens and return the arithmetic average of all the itens.
#  * If the recived array contains less then 3 itens, the function should return the boolean false.
#  * Ex: input: [4,6,8] 	- output 6
#  * Ex: input: [1,2] 	- output false
#  *
#  * A função deverá receber um array com pelo menos 3 itens e retornar a média simples de todos os itens do array.
#  * Caso o array recebido possua menos que 3 itens, deverá ser retornado o boleano false.
#  * Ex: input: [4,6,8] 	- output 6
#  * Ex: input: [1,2] 	- output false
#  *
#  * @param array $notas
#  * @return int|bool
#  */



def arithmeticAverage(integers):
    sum_integers = 0
    itens_in_array = len(integers)
    
    if itens_in_array == 3:
        for int_array in integers:
        
            sum_integers = int_array + sum_integers
        
        average = int(sum_integers / 3)
            
        return average
    
    else:
        return False

array = []

first_number = int(input('coloque um número: '))

second_number = int(input('Coloque um segundo número: '))

third_number = int(input('Coloque mais um número: '))

array.append(first_number)
array.append(second_number)
array.append(third_number)

print(arithmeticAverage(array))
    