def inverter_string(s):
    
    caracteres = list(s)
    
    inicio = 0
    fim = len(caracteres) - 1
    
    while inicio < fim:
        caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
        
        inicio += 1
        fim -= 1
    
    return ''.join(caracteres)


string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)
