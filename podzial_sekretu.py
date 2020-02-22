#10 udzialow, rozmiar przestrzeni liczbowej to 100
import random
k = 1000

s = 345 #sekret
s1 = random.randrange(0,k-1)
s2 = random.randrange(0,k-1)
s3= random.randrange(0,k-1)
s4 = random.randrange(0,k-1)
s5 = random.randrange(0,k-1)
s6 = random.randrange(0,k-1)
s7 = random.randrange(0,k-1)
s8 = random.randrange(0,k-1)
s9 = (s-s1 - s2 - s3 - s4 - s5 - s6 - s7- s8)%k

print("Sekret to: " + str(s) )
print("Udzial 1: " + str(s1) + " Udzial 2: " + str(s2) + " Udzial 3: " + str(s3) + " Udzial 4: " + str(s4) + " Udzial 5: " + str(s6) + " Udzial 7: " + str(s7) +" Udzial 8: "  + str(s8) + " Udzial 9: " + str(s9))

sekret = (s1 +s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9)%k
print("Sekret po obliczeniach to: " + str(sekret))


