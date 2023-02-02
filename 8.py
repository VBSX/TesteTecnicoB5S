import time
# /**
#  * Your function need to read the file data.dat and return how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2.
#  *
#  * A função deverá ler o arquivo data.dat e retornar o número de linhas que atende pelo menos uma das condições abaixo:
#  * 1 - A quantidade de números zeros na linha é um multiplo de 3
#  * 2 - A quantidade de números 1 é um multiplo de 2
#  *
#  * @return int
#  */
def fileHandler():
    dat = open('data.dat')
    number_multiple = 0
    for lines in dat:
        number_of_zeros = lines.count('0')
        number_of_one = lines.count('1')  
           
        modulus_of_3 = number_of_zeros % 3
        modulus_of_2 = number_of_one % 2

        if modulus_of_3 == 0:
            number_multiple += 1
            
        elif modulus_of_2 == 0:
            number_multiple +=1      
    return number_multiple
        
    
print(fileHandler())