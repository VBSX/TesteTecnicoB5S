# /**
#  * The function must replace all the vowels with '?' and return the result string
#  * Ex: input: 'Foo' - output: 'F??'
#  *
#  * A função deverá receber uma string e substituir todas as vogais da mesma pelo sinal '?'
#  * Ex: input: 'Bar' - output: 'B?r'
#  *
#  * @param string $string
#  * @return string
#  */


def replaceWowels(string):
    vowels = ['a','e','i','o','u']
    loop = True
    output_string = ''
    for char_of_string in string:
        
        for vow in vowels:
            if char_of_string == vow:
                output_string += '?'
                loop = False
                
                break
        
        if loop:    
            output_string +=char_of_string
        loop = True                  
    return output_string

string = input('Coloque uma palavra: ')
print(replaceWowels(string))