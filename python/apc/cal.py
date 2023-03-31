# this is for ABCY material
# these are the value of constants.
# i am importing matplotlib and numpy library
import matplotlib.pyplot as plt
import numpy as np



# taking two lists one is blank because i want to append the value of dn/d lamda
# another one has lamda value.
derivative_value = [] 
# lamda = [0.85,0.90,0.95,1.0,1.5,1.10,1.15,1.20,1.25,1.30,1.35,1.40,1.45,1.50,1.55,1.60,1.61,1.62,1.63,1.64,1.65] 
lamda = [0.95,1.15,1.25,1.35,1.45,1.55,1.65] 

# here i am assigning all constant value for later use
A = 7.67742 * pow(10,-6)
B = 2.16195 * pow(10,-3)
D = -1.28304 * pow(10,-3)
E = -5.35487 * pow(10,-6)

# now let's calculate dn/dY y = lamda.

#here value of lamda will varry
# this is a for loop run the size of the lamda list return dn/d lamda value.
for i in range(len(lamda)):
    derivative_of_n = (-4 * A * pow(lamda[i],-5))  - (2*B*pow(lamda[i],-3)) +(2*D*pow(lamda[i],1)) +(4*E*pow(lamda[i],3))
    # here appending all dn/d lamda value to the blanck list
    derivative_value.append(derivative_of_n)



# this is basic ploting program

plt.plot(lamda, derivative_value, color ='orange',markersize = 12,label ='ABCY')
plt.xlabel('value of lamda') 
plt.ylabel('this is dn/dy value')
plt.title('this is a graph of ABCY optical fiber material')
plt.legend()
plt.show()