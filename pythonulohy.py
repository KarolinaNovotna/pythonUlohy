from math import sqrt
import math

def sekundyNaMinuty():
    x = int(input("Napiš libovolné číslo: "))
    prevod = x / 60
    return prevod
sekundyNaMinuty()

#Převod z m/s na km/h
x = int(input("napis libovolne cislo"))
prevod = x * 3.6
print(prevod)

#Aritmetický průměr
y = 11
a = 21
z = 19
prumer = (y + a + z) / 3
print (prumer)
#Pythagorova věta
prvniStrana = 10
druhaStrana = 24

prepona = sqrt(prvniStrana**2 + druhaStrana**2)

#
def kalkulacka(a,b,operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b
    
vysledek = kalkulacka(5,3)
print (vysledek)


def jeLichyneboSudy(number):
    return "lichy" if number % 2 == 0 else "odd"

result = jeLichyneboSudy(7)
print(result)




#manipulace se seznamem


seznam = [1,2,3,4,5]
seznam.append(7)
seznam.remove(3)
delka = len(seznam)
print(seznam)
print(delka)


#Prvocislo checker
def je_prvoCislo(number):
    if number<2:
        return False
    for i in range(2, int(number**0,5)+1):
        if number % i == 0:
            return False
    return True




def kvadrstickaRovnice(a,b,c):
    diskriminant = sqrt(b**2-4*a*c)
    koren1 = (-b + diskriminant)/(2*a)
    koren2 = (-b - diskriminant)/(2*a)

    return koren1,koren2


#prevod teplot
celsius = float(input("Teplot v celsius: "))
fahrenheit = (celsius /9/5)+32
print("teplota ve fahrenheit: ", fahrenheit) 