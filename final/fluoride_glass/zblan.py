import matplotlib.pyplot as plt
import numpy as np




#lamda = [0.95,1.15,1.25,1.35,1.45,1.55,1.65]
lamda = [0.95,1.0,1.10,1.15,1.20,1.25,1.30,1.35,1.40,1.45,1.50,1.55,1.60,1.65]
#lamda = [0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9]



# this is for pure ZBLAN.
N_ZBLAN =[]
derivative_one_ZBLAN = []
derivative_two_ZBLAN = []

a_ZBLAN = 93.67070 * pow(10,-6)
b_ZBLAN =2.94329 *pow(10,-3)
c_ZBLAN =1.49136
d_ZBLAN =-1.25045 *pow(10,-3)
e_ZBLAN =-4.01026 * pow(10,-6)




for i in range(len(lamda)):
    n =  a_ZBLAN*lamda[i]**-4 + b_ZBLAN*lamda[i]**-2 + c_ZBLAN + d_ZBLAN*lamda[i]**2 + e_ZBLAN*lamda[i]**4
    N_ZBLAN.append(n)
print("this is the value of n for ZBLAN")
print(N_ZBLAN)


for i in range(len(lamda)):
    der = -4 * a_ZBLAN * lamda[i] ** -5 - 2*b_ZBLAN*lamda[i]**-3 + 2*d_ZBLAN* lamda[i] + 4* e_ZBLAN * lamda[i]**3
    derivative_one_ZBLAN.append(der)

print(derivative_one_ZBLAN)


for i in range(len(derivative_one_ZBLAN)):
    second_der = 20*a_ZBLAN*lamda[i]**-6 + 6*b_ZBLAN*lamda[i]**-4 +2 *d_ZBLAN + 12 * e_ZBLAN * lamda[i]**2
    derivative_two_ZBLAN.append(second_der)

print("this is the value of second derivative of ZBLAN")
print(derivative_two_ZBLAN)


plt.plot(lamda, derivative_two_ZBLAN, color ='red',markersize = 12,label ='ZBLAN')


plt.xlabel('value of lamda') 
plt.ylabel('this is d^2n/d_lamda^2 value')
plt.title('this is a graph of ABCY && ZBLAN optical fiber materials ----- SECOND DERIVATIVE')
plt.legend()
plt.show()