# /**
#  * The function should work like an ATM machine. it will recive an integer value representing the amount that will be withdrown and an array containing the avaliable bank notes.
#  * Your function will have to return an array informing the minimum amount of bank notes as possible for the withdrown. Consider that the amount of each note are infinity.
#  *
#  * A função será utilizada em um sistema de caixa.
#  * Ela receberá um valor inteiro, representando o valor a ser sacado e um array contendo quais tipos de cédulas ela tem disponível.
#  * O array de cédulas disponiveis indica quais valores de cédulas existirão no caixa, a quantidade das mesmas é ilimitada. No caso do input [2,5,50], o caixa terá quantidades ilimitadas de notas de 2, 5 e 50 para devolver ao cliente.
#  * A função deverá retornar o mínimo de cédulas necessarias possivel para o saque em formato de um array, cuja chave seja o valor da cédula e o valor a quantidade daquela cédula que será sacada.
#  *
#  * Ex: input: 150 & [5, 50, 100] 	- output: ["100"=>1, "50"=>1].
#  * Ex: input: 150 e [2, 5, 10] 		- output: ["10"=>15].
#  *
#  * @param int   $valor
#  * @param array $cedulas
#  *
#  * @return array
#  */



def atmMachine(value,bankNotes):
    lenght_notes = len(bankNotes)
    for i in range(lenght_notes):
        
        
       
       
   
   
bank_notes = [2,5,10]
values = 150
print(atmMachine(values,bank_notes))