import matplotlib.pyplot as plt
import numpy as np

derivative_value_ABCY = []
derivative_value_ZBLAN = []
lamda = [0.95,1.0,1.10,1.15,1.20,1.25,1.30,1.35,1.40,1.45,1.50,1.55,1.60,1.65]
#lamda = [-0.5,0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9]

A_ABCY = 7.67742 * pow(10,-6)
B_ABCY = 2.16195 * pow(10,-3)
D_ABCY = -1.28304 * pow(10,-3)
E_ABCY = -5.35487 * pow(10,-6)

for i in range(len(lamda)):
    derivative_of_n = (20 * A_ABCY * pow(lamda[i],-6))  + (6*B_ABCY*pow(lamda[i],-4)) +(2*D_ABCY) +(12*E_ABCY*pow(lamda[i],2))
    # here appending all dn/d lamda value to the blanck list
    derivative_value_ABCY.append(derivative_of_n)

A_ZBLAN = 93.67070 * pow(10,-6)
B_ZBLAN = 2.94329 * pow(10,-3)
D_ZBLAN = -1.25045 * pow(10,-3)
E_ZBLAN = -4.01026 * pow(10,-6)

for i in range(len(lamda)):
    derivative_of_n = (20 * A_ZBLAN * pow(lamda[i],-6))  + (6*B_ZBLAN*pow(lamda[i],-4)) +(2*D_ZBLAN) +(12*E_ZBLAN*pow(lamda[i],2))
    # here appending all dn/d lamda value to the blanck list
    derivative_value_ZBLAN.append(derivative_of_n)

print(derivative_value_ABCY)
print(derivative_value_ZBLAN)


plt.plot(lamda, derivative_value_ABCY, color ='Magenta',markersize = 12,label ='ABCY')
plt.plot(lamda, derivative_value_ZBLAN, color ='Cyan',markersize = 12,label ='ZBLAN')
plt.xlabel('value of lamda') 
plt.ylabel('this is d^2n/dy^2 value')
plt.title('this is a graph of ABCY AND ZBLAN optical fiber material')
plt.legend()
plt.show()