import matplotlib.pyplot as plt
import numpy as np

lamda = [0.95,1.15,1.25,1.35,1.45,1.55,1.65]
#lamda = [0.95,1.0,1.10,1.15,1.20,1.25,1.30,1.35,1.40,1.45,1.50,1.55,1.60,1.65]
#lamda = [0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9]


# this is for pure hbl.
N_hbl =[]
derivative_one_hbl = []
derivative_two_hbl = []

a_hbl = -28.61020 * pow(10,-6)
b_hbl = 3.11470 *pow(10,-3)
c_hbl = 1.50294
d_hbl = -1.17821 * pow(10,-3)
e_hbl = -2.64123 * pow(10,-6)




for i in range(len(lamda)):
    n =  a_hbl*lamda[i]**-4 + b_hbl*lamda[i]**-2 + c_hbl + d_hbl*lamda[i]**2 + e_hbl*lamda[i]**4
    N_hbl.append(n)
print("this is the value of n for sio2")
print(N_hbl)


for i in range(len(lamda)):
    der = -4 * a_hbl * lamda[i] ** -5 - 2*b_hbl*lamda[i]**-3 + 2*d_hbl* lamda[i] + 4* e_hbl * lamda[i]**3
    derivative_one_hbl.append(der)

print(derivative_one_hbl)


for i in range(len(derivative_one_hbl)):
    second_der = 20*a_hbl*lamda[i]**-6 + 6*b_hbl*lamda[i]**-4 +2 *d_hbl + 12 * e_hbl * lamda[i]**2
    derivative_two_hbl.append(second_der)

print("this is the value of second derivative of hbl")
print(derivative_two_hbl)


plt.plot(lamda, derivative_two_hbl, color ='Magenta',markersize = 12,label ='PURE SIO2')


plt.xlabel('value of lamda') 
plt.ylabel('this is d^2n/d_lamda^2 value')
plt.title('this is a graph of PURE HBL optical fiber materials ----- SECOND DERIVATIVE')
plt.legend()
plt.show()