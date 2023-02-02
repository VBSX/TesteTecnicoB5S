
# /**
#  * The function must expect an array of integers and sort it in ascending order
#  * Ex: Input: [5,1,0,7,3,3] - Output: [0,1,3,3,5,7]
#  *
#  * A função deverá receber um array de inteiros como parâmetro e deverá retornar o mesmo array ordenado em ordem crescente.
#  * Ex: Input: [5,1,0,7,3,3] - Output: [0,1,3,3,5,7]
#  *
#  * @param array $array - Array a ser ordenado
#  * @return array
#  */

def arraySort(array):
    output = []
   
    for number in array:
        
        if number == 0:
            output.append(number)
            
    for number in array:
        
        if number == 1:
            output.append(number)
                  
    for number in array:
        
        if number == 2:
            output.append(number)
        
    for number in array:
        
        if number == 3:
            output.append(number)
    for number in array:
        
        if number == 4:
            output.append(number)
            
    for number in array:
        
        if number == 5:
            output.append(number)
            
    for number in array:
        
        if number == 6:
            output.append(number)
              
    for number in array:
        
        if number == 7:
            output.append(number)
            
    for number in array:
        
        if number == 8:
            output.append(number)
            
    for number in array:
        
        if number == 9:
            output.append(number)
                 
    return output
            
            
array = [5,0,9,8,7,4,1,4]
print(arraySort(array))