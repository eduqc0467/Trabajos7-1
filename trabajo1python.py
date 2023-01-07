#El programa esta programado para saber si es un numero divisible por 3 y 5
num=input("Ingrese numero")
sum=0
ult=int(num)%10
tam=len(num)
for i in range(tam):
    sum=sum+int(num[i])
div3=sum%3
if div3==0:
    print("EL numero es divisible por 3")
div5=ult%5
if ult==5 or ult==0 :
    print ("El numero es divisible por 5")
