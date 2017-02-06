# Madelung constant for NaCl
# Crystal composed of 2N ions have U_tot = N*U_i

from numpy import*
import matplotlib.pyplot as plt
N = linspace(1,50, num=50)
print N
L=len(N)
print L


#r(i,j) = a*p(i,j)

alpha = [0]
a = 1
index = 1

while index < len(N):
    if index %2 == 0:
        i = -1
    else: 
        i = 1
    alpha.append((2*i*a)/N[index])
    index = index + 1
    
    #print index
    
    
    
l = len(alpha)
#print l 


alphas = []


for f in range(len(alpha)):
    alphas.append(sum(alpha[0:f]))
    
p = len(alphas)
#print p
#print alpha

#plt.plot(N, alphas, "r--")
plt.xlabel('Enhet celler', fontsize=20)
plt.ylabel('Madelung konstant', fontsize=20)
plt.title('Madelung konstant som funksjon av kyrstall storrelse', fontsize=18)


#plt.show()


#1D
# R0 = seperation distance between atoms in lattice
# R0 = ((p**2*(abs(alphas[index]))*e**2)/landa)**(1./3)
p = 0.321e-11 # m parameter of repulsive energi
landa = 1e3 # eV
e = 1.60219 # CGS 

R0 = []
index = 0


for d in range(len(alphas)):
    R0.append(((p**2*(abs(alphas[index]))*e**2)/landa)**(1./3))
    index = index + 1
    
    print R0
    
  
plt.plot(N, R0, "g-")
#plt.yscale('log')
plt.xlabel('Enhet celler')
plt.ylabel('interatomsk avstanden')
plt.title('Inter atomks avstanden som funksjon av kyrstall storrelse')
plt.show()

