
# /**
#  * The function must return the full credit card number. The card number is a multiple of 123457 and the Luhn check digit is valid.
#  * The Card Number must have the following pattern: 543210******1234
#  *
#  * Descubra o número do cartão de crédito abaixo sabendo que o mesmo é um multiplo de 123457 e o digito de luhn é válido.
#  * O Número do cartão deve ter o seguinte padrão: 543210******1234
#  *
#  * @return string
#  */



def creditCardNumber():
    card_number_length = 16
    card_number = 543210
    card_number_to_find = [0,0,0,0,0,0]
    card_number_final = 1234
    
    credit_finder = False
    # while credit_finder == False:
    for length in range(0,6):
        
        for number in range(0,10):
            
            card_number_to_find[length]=number
            
    print(card_number_to_find)
                
                

creditCardNumber()