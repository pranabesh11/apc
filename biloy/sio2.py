import matplotlib.pyplot as plt
import numpy as np


#lamda = [0.95,1.15,1.25,1.35,1.45,1.55,1.65]
lamda = [0.95,1.0,1.10,1.15,1.20,1.25,1.30,1.35,1.40,1.45,1.50,1.55,1.60,1.65]
#lamda = [0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9]




# this is for pure sio2.
N_p205 =[]
derivative_one_p205 = []
derivative_two_p205 = []

b_1_p205 =0.7058489#0.7347008#0.6910021#0.6961663   #0.7347008#0.7083952#0.7347008 #0.6910021 # #
b_2_p205 =0.4176021#0.4461191#0.4022430#0.4079426   #0.4461191 #0.4203993#0.4461191 #0.4022430 # #
b_3_p205 =0.8952753#0.8081698#0.9439644#0.8974794   #0.8081698#0.8663412#0.8081698 # # #

a_1_p205 =0.005202431#0.005847345#0.004981838#0.004679148  #0.005847345# 0.007290464#0.005847345 #0.004981838 # # 
a_2_p205 =0.01287730#0.01552717#0.01375664#0.01351206  #0.01552717#0.01050294#0.01552717 #0.01375664 # #
a_3_p205 =97.93401#97.93484#97.93353#97.93400  #97.93484#97.93428 #97.93484 #97.93353 # #

for i in range(len(lamda)):
    big_expression = (b_1_p205/(lamda[i]**2-a_1_p205)+b_2_p205/(lamda[i]**2-a_2_p205)+b_3_p205/(lamda[i]**2-a_3_p205)+1/lamda[i]**2)
    n = lamda[i]*(big_expression**0.5)
    N_p205.append(n)
print("this is the value of n for p205")
print(N_p205)

for i in range(len(lamda)):
    der = (1/((-1)*N_p205[i])) * ((a_1_p205*b_1_p205*lamda[i]/(lamda[i]**2-a_1_p205)**2) + (a_2_p205*b_2_p205*lamda[i]/(lamda[i]**2-a_2_p205)**2) + (a_3_p205*b_3_p205*lamda[i]/(lamda[i]**2-a_3_p205)**2))
    derivative_one_p205.append(der)

print("this is the value of first derivative of p205")
print(derivative_one_p205)

for i in range(len(derivative_one_p205)):
    #second_der = (1/N_p205[i]) * ( (-3*a_1_p205*b_1_p205*lamda[i]**4 + 2*a_1_p205**2 * b_1_p205*lamda[i]**2 + a_1_p205**3 * b_1_p205)/(lamda[i]**2-a_1_p205)**4    +   (-3*a_2_p205*b_2_p205*lamda[i]**4 + 2*a_2_p205**2 * b_2_p205*lamda[i]**2 + a_2_p205**3 * b_2_p205)/(lamda[i]**2-a_2_p205)**4   +   (-3*a_3_p205*b_3_p205*lamda[i]**4 + 2*a_3_p205**2 * b_3_p205*lamda[i]**2 + a_3_p205**3 * b_3_p205)/(lamda[i]**2-a_3_p205)**4   +    derivative_one_p205[i]**2)
    f_part = (1/lamda[i])*derivative_one_p205[i]
    s_part = (1/N_p205[i])*(derivative_one_p205[i]**2)
    t_part = (4*lamda[i]**2/N_p205[i])*((a_1_p205*b_1_p205/(lamda[i]**2-a_1_p205)**3) + (a_2_p205*b_2_p205/(lamda[i]**2-a_2_p205)**3) + (a_3_p205*b_3_p205/(lamda[i]**2-a_3_p205)**3))
    second_der = f_part-s_part+t_part 
    derivative_two_p205.append(second_der)

print("this is the value of second derivative of p205")
print(derivative_two_p205)

plt.plot(lamda, derivative_two_p205, color ='Magenta',markersize = 12,label ='PURE p205')

plt.xlabel('value of lamda') 
plt.ylabel('this is d^2n/d_lamda^2 value')
plt.title('this is a graph of PURE p205 optical fiber materials ----- SECOND DERIVATIVE')
plt.legend()
plt.show() 