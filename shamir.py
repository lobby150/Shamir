# p = liczba pierwsza duza, n = liczba udzialow, s = sekret z zakresu p-1
import random


def isPrime(num):
    prime = True
    if num > 1:
        for i in range(2, num // 2):
            if num % i == 0:
                prime = False
                break
    if prime == True:
        return num
    else:
        return False

def sigma(a,x,t):
    wynik = 0
    for i in range(1, t-1):
        wynik = wynik + (a[i] *x ** i)
    return wynik






p = 0
for i in range(1230, 2000):
    if isPrime(i) != False:
        p = i
        break
s=random.randrange(1,p)
print("Wartosc liczby pierwszej: " + str(p))

print("Wartosc ustalonego sekretu: " + str(s))

n = 10
print("Calkowita liczba udzialow: " + str(n))

t = random.randrange(4,n)

print("Wymagana liczba udzialow: " + str(t))




aTab=[s]
sTab = [s]
for i in range(1, t):
    aTab.append(random.randrange(10,100))
print(aTab)
for i in range(1,n):
    sTab.append((s + sigma(aTab,i,t))%p)
print("Stab" + str(sTab))

def wydobycie_sekretu(t, tab):
    sigma = 0
    for i in range(1,t):
        iloczyn  = 1
        for j in range(1,t):
            if(i!=j):
                iloczyn = iloczyn * (-1*j)/(i-j)
        sigma = (sigma + tab[i] * iloczyn)%p
    return sigma


print("Sekret to: " + str(round(wydobycie_sekretu(t,sTab))))