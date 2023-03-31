import matplotlib.pyplot as plt
import numpy as np


#lamda = [0.95,1.15,1.25,1.35,1.45,1.55,1.65]
lamda = [0.95,1.0,1.10,1.15,1.20,1.25,1.30,1.35,1.40,1.45,1.50,1.55,1.60,1.65]
#lamda = [0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9]




# this is for pure sio2.
N_sio2 =[]
derivative_one_sio2 = []
derivative_two_sio2 = []

b_1_sio2 = 0.6961663
b_2_sio2 = 0.4079426
b_3_sio2 = 0.8974794

a_1_sio2 = 0.004679148
a_2_sio2 = 0.01351206
a_3_sio2 = 97.93400

for i in range(len(lamda)):
    big_expression = (b_1_sio2/(lamda[i]**2-a_1_sio2)+b_2_sio2/(lamda[i]**2-a_2_sio2)+b_3_sio2/(lamda[i]**2-a_3_sio2)+1/lamda[i]**2)
    n = lamda[i]*(big_expression**0.5)
    N_sio2.append(n)
print("this is the value of n for sio2")
print(N_sio2)

for i in range(len(lamda)):
    der = (1/(-1)*N_sio2[i]) * ((a_1_sio2*b_1_sio2*lamda[i]/(lamda[i]**2-a_1_sio2)**2) + (a_2_sio2*b_2_sio2*lamda[i]/(lamda[i]**2-a_2_sio2)**2) + (a_3_sio2*b_3_sio2*lamda[i]/(lamda[i]**2-a_3_sio2)**2))
    derivative_one_sio2.append(der)

print("this is the value of first derivative of sio2")
print(derivative_one_sio2)

for i in range(len(derivative_one_sio2)):
    #second_der = (1/N_sio2[i]) * ( (-3*a_1_sio2*b_1_sio2*lamda[i]**4 + 2*a_1_sio2**2 * b_1_sio2*lamda[i]**2 + a_1_sio2**3 * b_1_sio2)/(lamda[i]**2-a_1_sio2)**4    +   (-3*a_2_sio2*b_2_sio2*lamda[i]**4 + 2*a_2_sio2**2 * b_2_sio2*lamda[i]**2 + a_2_sio2**3 * b_2_sio2)/(lamda[i]**2-a_2_sio2)**4   +   (-3*a_3_sio2*b_3_sio2*lamda[i]**4 + 2*a_3_sio2**2 * b_3_sio2*lamda[i]**2 + a_3_sio2**3 * b_3_sio2)/(lamda[i]**2-a_3_sio2)**4   +    derivative_one_sio2[i]**2)
    f_part = (1/lamda[i])*derivative_one_sio2[i]
    s_part = (1/N_sio2[i])*(derivative_one_sio2[i]**2)
    t_part = (4*lamda[i]**2/N_sio2[i])*((a_1_sio2*b_1_sio2/(lamda[i]**2-a_1_sio2)**3) + (a_2_sio2*b_2_sio2/(lamda[i]**2-a_2_sio2)**3) + (a_3_sio2*b_3_sio2/(lamda[i]**2-a_3_sio2)**3))
    second_der = f_part-s_part+t_part 
    derivative_two_sio2.append(second_der)

print("this is the value of second derivative of sio2")
print(derivative_two_sio2)

plt.plot(lamda, derivative_two_sio2, color ='Magenta',markersize = 12,label ='PURE SIO2')

plt.xlabel('value of lamda') 
plt.ylabel('this is d^2n/d_lamda^2 value')
plt.title('this is a graph of PURE SIO2 optical fiber materials ----- SECOND DERIVATIVE')
plt.legend()
plt.show()