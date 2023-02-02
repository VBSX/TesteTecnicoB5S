
# The function should recive an integer between 1 and 12 (inclusive) and return the corresponding string value. If the informed integger is not between 1 and 12, the function should return 'Unknown Month'
# Ex: input: 1 - output: "January"
# Ex: input: 13 - output: "Unknown Month"

# A função recebe um inteiro entre 1 e 12 e retorna o mês correspondente por extenso. Caso o mês informado não esteja entre 1 e 12, deverá ser retornado "Mes Inexistente"
# Ex: input: 1 	- output: "Janeiro"
# Ex: input: 13 	- output: "Mês Desconhecido"

# @param int $month
# @return string




def correspondingMonth(month):
    if month == '1':
        return 'Janeiro'
    
    elif month == '2':
        return 'Fevereiro'
    
    elif month == '3':
        return 'Março'
    
    elif month == '4':
        return 'Abril'
    
    elif month == '5':
        return 'Maio'
    
    elif month == '6':
        return 'Junho'
    
    elif month == '7':
        return 'Julho'
    
    elif month == '8':
        return 'Agosto'
    
    elif month == '9':
        return 'Setembro'
    
    elif month == '10':
        return 'Outubro'

    elif month == '11':
        return 'Novembro'
    
    elif month == '12':
        return 'Dezembro'
    
    else:
        return 'Mes Inexistente'
    
    
numero_do_mes = input('Coloque o número de um mês: ')

print('\n',correspondingMonth(numero_do_mes),'\n')

