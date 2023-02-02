
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
    number_multple_of_3 = 0
    a = [0,1,0,0,0]
    for lines in dat:
        # line = dat.readline()
        # number_of_zeros = len(line)
        
         
        
        number_of_zeros = lines.count(0)
        print(number_of_zeros,'zeros')
        
        
        modulus = number_of_zeros % 3
        print(modulus)
        if modulus == 0:
            number_multple_of_3 += 1
     
        
        
    print(number_multple_of_3,'resutlado')
        
    
fileHandler()