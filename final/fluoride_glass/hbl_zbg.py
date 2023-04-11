import matplotlib.pyplot as plt
import numpy as np

#lamda = [0.95,1.15,1.25,1.35,1.45,1.55,1.65]
lamda = [0.95,1.0,1.10,1.15,1.20,1.25,1.30,1.35,1.40,1.45,1.50,1.55,1.60,1.65,1.70,1.75]
#lamda = [0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9]


# this is for pure HBL.
N_HBL =[]
derivative_one_HBL = []
derivative_two_HBL = []

a_HBL =-28.61020 * pow(10,-6)
b_HBL =3.11470 *pow(10,-3)
c_HBL =1.50294
d_HBL =-1.17821 * pow(10,-3)
e_HBL =-2.64123 * pow(10,-6)




for i in range(len(lamda)):
    n =  a_HBL*lamda[i]**-4 + b_HBL*lamda[i]**-2 + c_HBL + d_HBL*lamda[i]**2 + e_HBL*lamda[i]**4
    N_HBL.append(n)
print("this is the value of n for HBL")
print(N_HBL)


for i in range(len(lamda)):
    der = -4 * a_HBL * lamda[i] ** -5 - 2*b_HBL*lamda[i]**-3 + 2*d_HBL* lamda[i] + 4* e_HBL * lamda[i]**3
    derivative_one_HBL.append(der)

print(derivative_one_HBL)


for i in range(len(derivative_one_HBL)):
    second_der = 20*a_HBL*lamda[i]**-6 + 6*b_HBL*lamda[i]**-4 +2 *d_HBL + 12 * e_HBL * lamda[i]**2
    derivative_two_HBL.append(second_der)

print("this is the value of second derivative of HBL")
print(derivative_two_HBL)







# this is for pure ZBG.
N_ZBG =[]
derivative_one_ZBG = []
derivative_two_ZBG = []

a_ZBG =93.67070 * pow(10,-6)
b_ZBG =2.94329 *pow(10,-3)
c_ZBG =1.51236
d_ZBG =-1.25045 * pow(10,-3)
e_ZBG =-4.01026 * pow(10,-6)




for i in range(len(lamda)):
    n =  a_ZBG*lamda[i]**-4 + b_ZBG*lamda[i]**-2 + c_ZBG + d_ZBG*lamda[i]**2 + e_ZBG*lamda[i]**4
    N_ZBG.append(n)
print("this is the value of n for ZBG")
print(N_ZBG)


for i in range(len(lamda)):
    der = -4 * a_ZBG * lamda[i] ** -5 - 2*b_ZBG*lamda[i]**-3 + 2*d_ZBG* lamda[i] + 4* e_ZBG * lamda[i]**3
    derivative_one_ZBG.append(der)

print(derivative_one_ZBG)


for i in range(len(derivative_one_ZBG)):
    second_der = 20*a_ZBG*lamda[i]**-6 + 6*b_ZBG*lamda[i]**-4 +2 *d_ZBG + 12 * e_ZBG * lamda[i]**2
    derivative_two_ZBG.append(second_der)

print("this is the value of second derivative of ZBG")
print(derivative_two_ZBG)




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




#plt.plot(lamda, derivative_two_HBL, color ='Magenta',markersize = 12,label ='HBL')
plt.plot(lamda, derivative_two_ZBG, color ='black',markersize = 12,label ='ZBG')
plt.plot(lamda, derivative_two_ZBLAN, color ='red',markersize = 12,label ='ZBLAN')



plt.xlabel('value of lamda') 
plt.ylabel('this is d^2n/d_lamda^2 value')
plt.title('this is a graph of HBL optical fiber materials ----- SECOND DERIVATIVE')
plt.legend()
plt.show()