def eDivisibile(num1, num2):
    ciao = False
    if(num1 % num2 == 0):
        ciao = True
    return ciao

def MCD(num1,num2):
    
    vettore = []
    if(num2>num1):
        #inverte in modo tale che num1 sia maggiore di num2
        num3 = num1
        num1 = num2
        num2 = num3
       
    while(1):
        n = num1 % num2 
        if(n==0):
            break
        vettore.append(n)
        num1 = n
        num2 = num1
    
    return vettore[-1]

def mcm(num1,num2):
    return (num1*num2)/MCD(num1,num2)
    




n1 = int(input("inserire un numero: "))
n2 = int(input("inserire un altro numero: "))
print(f"il minimo comune multiplo è {mcm(n1,n2)}")
print(f"il massimo comun divisore è {MCD(n1,n2)}")