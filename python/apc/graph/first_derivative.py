import matplotlib.pyplot as plt
import numpy as np

derivative_value_ABCY = []
derivative_value_ZBLAN = []
lamda = [0.95,1.15,1.25,1.35,1.45,1.55,1.65]
#lamda = [0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9]

A_ABCY = 7.67742 * pow(10,-6)
B_ABCY = 2.16195 * pow(10,-3)
D_ABCY = -1.28304 * pow(10,-3)
E_ABCY = -5.35487 * pow(10,-6)

for i in range(len(lamda)):
    derivative_of_n = (-4 * A_ABCY * pow(lamda[i],-5))  - (2*B_ABCY*pow(lamda[i],-3)) +(2*D_ABCY*pow(lamda[i],1)) +(4*E_ABCY*pow(lamda[i],3))
    # here appending all dn/d lamda value to the blanck list
    derivative_value_ABCY.append(derivative_of_n)

A_ZBLAN = 93.67070 * pow(10,-6)
B_ZBLAN = 2.94329 * pow(10,-3)
D_ZBLAN = -1.25045 * pow(10,-3)
E_ZBLAN = -4.01026 * pow(10,-6)

for i in range(len(lamda)):
    derivative_of_n = (-4 * A_ZBLAN * pow(lamda[i],-5))  - (2*B_ZBLAN*pow(lamda[i],-3)) +(2*D_ZBLAN*pow(lamda[i],1)) +(4*E_ZBLAN*pow(lamda[i],3))
    # here appending all dn/d lamda value to the blanck list
    derivative_value_ZBLAN.append(derivative_of_n)

plt.plot(lamda, derivative_value_ABCY, color ='Magenta',markersize = 12,label ='ABCY')
plt.plot(lamda, derivative_value_ZBLAN, color ='Cyan',markersize = 12,label ='ZBLAN')
plt.xlabel('value of lamda') 
plt.ylabel('this is dn/d_lamda value')
plt.title('this is a graph of ABCY AND ZBLAN optical fiber materials')
plt.legend()
plt.show()