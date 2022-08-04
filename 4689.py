#Entradas
num_digitos = int(input())
if num_digitos > 1000:
    print("ERRO")
    exit()
S1 = str(input()).strip()
len_S1 = len(S1) #num_digitos S1
S2 = str(input()).strip()
len_S2 = len(S2) #num_digitos S2
operadores = ["AND", "OR", "XOR", "NAND", "NOR", "MOR"]
#Operação
S3 = str(input()).strip()
#Processamento
#-1 leitura dos dados
operatorios = S3.split(" ")
num_operatorios = len(operatorios)
#-2 Verificações e Erros
##Numero de operadores e Verificação das entradas
###S1 e S2 verificações
if (len_S1 == num_digitos) and (len_S2 == num_digitos):
    pass
else:
    print("ERRO")
    exit()
###Operadores e Operatorios
if (num_operatorios % 2) != 0:
    for a in range(0, num_operatorios, 2):
        if operatorios[a] == "S1" or operatorios[a] == "S2":
            pass
        else:
            print("ERRO")
            exit()
    for a in range(1, num_operatorios, 2):
        erro = True
        for b in operadores:
            if operatorios[a] == b:
                erro = False
                break
        if erro:
          print("ERRO")
          exit()
else:
    print("ERRO")
    exit()
for a in S1:
    if a == "0":
        pass
    elif a == "1":
        pass
    else:
        print("ERRO")
        exit()
for a in S2:
    if a == "0":
        pass
    elif a == "1":
        pass
    else:
        print("ERRO")
        exit()
#Algoritmo de leitura
count_operadores_logicos = 0
for a in range(1, num_operatorios, 2):
    count_operadores_logicos += 1
vetor_entrada = ["S1", "S2"]
vetor_entrada2 = [S1, S2]
vetor_calculado = ["", "", ""]
controlador = 0
entrada = ""
entrada2 = ""
contador = 0
for a in range(0, num_operatorios, 2):
    for b in range(2):
        if operatorios[a] == vetor_entrada[b]:
            vetor_calculado[contador] = vetor_entrada2[b]
            contador += 1
while controlador < count_operadores_logicos:
    ###Entradas
    if controlador < 1:
        entrada = vetor_calculado[0]
        entrada2 = vetor_calculado[1]
    saida_intermediaria = ""
    for a in range(1, num_operatorios, 2):
        for b in operadores:
            ## Qual operador, AND, OR...?
            if operatorios[a] == b:
                for c in range(num_digitos):
                ##AND ok
                    if b == "AND":
                        if (entrada[c] == "1") and (entrada2[c] == "1"):
                            saida_intermediaria += "1"
                        else:
                            saida_intermediaria += "0"
                ##OR ok
                    if b == "OR":
                        if (entrada[c] == "0") and (entrada2[c] == "0"):
                            saida_intermediaria += "0"
                        else:
                            saida_intermediaria += "1"
                ##XOR OK
                    if b == "XOR":
                        if entrada[c] == entrada2[c]:
                            saida_intermediaria += "0"
                        else:
                            saida_intermediaria += "1"
                ##NAND OK
                    if b == "NAND":
                        if entrada[c] == "1" and entrada2[c] == "1":
                            saida_intermediaria += "0"
                        else:
                            saida_intermediaria += "1"
                ##NOR OK
                    if b == "NOR":
                        if entrada[c] == "0" and entrada2[c] == "0":
                            saida_intermediaria += "1"
                        else:
                            saida_intermediaria += "0"
                ##MOR ok
                    if b == "MOR":
                        if entrada[c] == "1" and entrada2[c] == "0":
                            saida_intermediaria += "0"
                        else:
                            saida_intermediaria += "1"
        if controlador < count_operadores_logicos:
            entrada = saida_intermediaria
            saida_intermediaria = ""
            controlador += 1
            if controlador < 2:
                entrada2 = vetor_calculado[controlador + 1]
print(f"{entrada}")