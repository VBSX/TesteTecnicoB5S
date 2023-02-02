
# /**
#  * The function should expect a string and return it backwards.
#  * Ex: input: "foo" - output: "oof"
#  *
#  * A função deverá receber uma string e retornar a mesma invertida.
#  * Ex: input: "bar" - output: "rab"
#  *
#  * @param string $string
#  * @return string
#  */

def reverseString(string):
    return string[::-1]

string = input('Coloque uma palavra: ')
print(reverseString(string))