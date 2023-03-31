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
    up_first = lamda[i]**6 * (b_1_sio2+b_2_sio2+b_3_sio2+1)
    up_second = lamda[i]**4 * (a_3_sio2*b_1_sio2 + a_2_sio2*b_1_sio2 + a_1_sio2*b_2_sio2+a_3_sio2*b_2_sio2+a_1_sio2*b_3_sio2+a_2_sio2*b_3_sio2+a_1_sio2+a_2_sio2+a_3_sio2)
    up_three = lamda[i]**2 * (a_2_sio2*a_3_sio2*b_1_sio2 + a_1_sio2*a_3_sio2*b_2_sio2 + a_1_sio2*a_2_sio2*b_3_sio2+a_1_sio2*a_3_sio2+a_2_sio2*a_3_sio2+a_1_sio2*a_2_sio2)
    up_four = a_1_sio2*a_2_sio2*a_3_sio2
    down_one = lamda[i]**6
    down_two = lamda[i]**4 * (a_1_sio2+a_2_sio2+a_3_sio2)
    down_three = lamda[i]**2 * (a_1_sio2*a_2_sio2+a_1_sio2*a_3_sio2+a_2_sio2*a_3_sio2)
    down_four = a_1_sio2*a_2_sio2*a_3_sio2

    final_value = (up_first-up_second+up_three-up_four)/(down_one-down_two+down_three-down_four)
    n = pow(final_value,0.5)
    N_sio2.append(n)

print("this is the value of n for sio2")
print(N_sio2)

#for i in range(len(lamda)):
    #big_expression2 = ((lamda[i]**6 *(b_1_sio2+b_2_sio2+b_3_sio2+1))-((lamda[i]**4 * (a_3_sio2*b_1_)))+()/ )
    #big_expression = (b_1_sio2/(pow(lamda[i],2)-a_1_sio2)+b_2_sio2/(pow(lamda[i],2)-a_2_sio2)+b_3_sio2/(pow(lamda[i],2)-a_3_sio2)+1/pow(lamda[i],2))
    
    #n = lamda[i]*pow(big_expression,0.5)
   # N_sio2.append(n)
#print("this is the value of n for sio2")
#print(N_sio2)

for i in range(len(lamda)):
    der = (1/(-1)*N_sio2[i]) * (a_1_sio2*b_1_sio2*lamda[i]/(lamda[i]**2-a_1_sio2)**2 + a_2_sio2*b_2_sio2*lamda[i]/(lamda[i]**2-a_2_sio2)**2 +a_3_sio2*b_3_sio2*lamda[i]/(lamda[i]**2-a_3_sio2)**2)
    derivative_one_sio2.append(der)

#print(derivative_one_sio2)

for i in range(len(derivative_one_sio2)):
    second_der = (1/(-1)*N_sio2[i]) * ( (-3*a_1_sio2*b_1_sio2*lamda[i]**4 + 2*a_1_sio2**2 * b_1_sio2*lamda[i]**2 + a_1_sio2**3 * b_1_sio2)/(lamda[i]**2-a_1_sio2)**4    +   (-3*a_2_sio2*b_2_sio2*lamda[i]**4 + 2*a_2_sio2**2 * b_2_sio2*lamda[i]**2 + a_2_sio2**3 * b_2_sio2)/(lamda[i]**2-a_2_sio2)**4   +   (-3*a_3_sio2*b_3_sio2*lamda[i]**4 + 2*a_3_sio2**2 * b_3_sio2*lamda[i]**2 + a_3_sio2**3 * b_3_sio2)/(lamda[i]**2-a_3_sio2)**4   +    derivative_one_sio2[i]**2)
    derivative_two_sio2.append(second_der)

print("this is the value of second derivative of sio2")
print(derivative_two_sio2)



# this is for Geo2
b_1_geo2 = 0.7347008
b_2_geo2 = 0.4461191
b_3_geo2 = 0.8081698

a_1_geo2 = 0.005847345
a_2_geo2 = 0.01552717
a_3_geo2 = 97.93484

N_geo2 = []
derivative_one_geo2 = []
derivative_two_geo2 = []

for i in range(len(lamda)):
    up_first = lamda[i]**6 * (b_1_geo2+b_2_geo2+b_3_geo2+1)
    up_second = lamda[i]**4 * (a_3_geo2*b_1_geo2 + a_2_geo2*b_1_geo2 + a_1_geo2*b_2_geo2+a_3_geo2*b_2_geo2+a_1_geo2*b_3_geo2+a_2_geo2*b_3_geo2+a_1_geo2+a_2_geo2+a_3_geo2)
    up_three = lamda[i]**2 * (a_2_geo2*a_3_geo2*b_1_geo2 + a_1_geo2*a_3_geo2*b_2_geo2 + a_1_geo2*a_2_geo2*b_3_geo2+a_1_geo2*a_3_geo2+a_2_geo2*a_3_geo2+a_1_geo2*a_2_geo2)
    up_four = a_1_geo2*a_2_geo2*a_3_geo2
    down_one = lamda[i]**6
    down_two = lamda[i]**4 * (a_1_geo2+a_2_geo2+a_3_geo2)
    down_three = lamda[i]**2 * (a_1_geo2*a_2_geo2+a_1_geo2*a_3_geo2+a_2_geo2*a_3_geo2)
    down_four = a_1_geo2*a_2_geo2*a_3_geo2

    final_value = (up_first-up_second+up_three-up_four)/(down_one-down_two+down_three-down_four)
    n = pow(final_value,0.5)
    N_geo2.append(n)


print("this is the value of n for geo2")
print(N_geo2)

for i in range(len(lamda)):
    der = (1/(-1)*N_geo2[i]) * (a_1_geo2*b_1_geo2*lamda[i]/(lamda[i]**2-a_1_geo2)**2 + a_2_geo2*b_2_geo2*lamda[i]/(lamda[i]**2-a_2_geo2)**2 +a_3_geo2*b_3_geo2*lamda[i]/(lamda[i]**2-a_3_geo2)**2)
    derivative_one_geo2.append(der)

for i in range(len(derivative_one_geo2)):
    second_der = (1/(-1)*N_geo2[i]) * ( (-3*a_1_geo2*b_1_geo2*lamda[i]**4 + 2*a_1_geo2**2 * b_1_geo2*lamda[i]**2 + a_1_geo2**3 * b_1_geo2)/(lamda[i]**2-a_1_geo2)**4    +   (-3*a_2_geo2*b_2_geo2*lamda[i]**4 + 2*a_2_geo2**2 * b_2_geo2*lamda[i]**2 + a_2_geo2**3 * b_2_geo2)/(lamda[i]**2-a_2_geo2)**4   +   (-3*a_3_geo2*b_3_geo2*lamda[i]**4 + 2*a_3_geo2**2 * b_3_geo2*lamda[i]**2 + a_3_geo2**3 * b_3_geo2)/(lamda[i]**2-a_3_geo2)**4   +    derivative_one_geo2[i]**2)
    derivative_two_geo2.append(second_der)

print("this is the value of second derivative of geo2")
print(derivative_two_geo2)


# this is for b2o3

b_1_b2o3 = 0.6910021
b_2_b2o3 = 0.4022430
b_3_b2o3 = 0.9439644

a_1_b2o3 = 0.004981838
a_2_b2o3 = 0.01375664
a_3_b2o3 = 97.93353

N_b2o3 = []
derivative_one_b2o3 = []
derivative_two_b2o3 = []

for i in range(len(lamda)):
    up_first = lamda[i]**6 * (b_1_b2o3+b_2_b2o3+b_3_b2o3+1)
    up_second = lamda[i]**4 * (a_3_b2o3*b_1_b2o3 + a_2_b2o3*b_1_b2o3 + a_1_b2o3*b_2_b2o3+a_3_b2o3*b_2_b2o3+a_1_b2o3*b_3_b2o3+a_2_b2o3*b_3_b2o3+a_1_b2o3+a_2_b2o3+a_3_b2o3)
    up_three = lamda[i]**2 * (a_2_b2o3*a_3_b2o3*b_1_b2o3 + a_1_b2o3*a_3_b2o3*b_2_b2o3 + a_1_b2o3*a_2_b2o3*b_3_b2o3+a_1_b2o3*a_3_b2o3+a_2_b2o3*a_3_b2o3+a_1_b2o3*a_2_b2o3)
    up_four = a_1_b2o3*a_2_b2o3*a_3_b2o3
    down_one = lamda[i]**6
    down_two = lamda[i]**4 * (a_1_b2o3+a_2_b2o3+a_3_b2o3)
    down_three = lamda[i]**2 * (a_1_b2o3*a_2_b2o3+a_1_b2o3*a_3_b2o3+a_2_b2o3*a_3_b2o3)
    down_four = a_1_b2o3*a_2_b2o3*a_3_b2o3

    final_value = (up_first-up_second+up_three-up_four)/(down_one-down_two+down_three-down_four)
    n = pow(final_value,0.5)
    N_b2o3.append(n)

print("this is the value of n for b2o3")
print(N_b2o3)

for i in range(len(lamda)):
    der = (1/(-1)*N_b2o3[i]) * (a_1_b2o3*b_1_b2o3*lamda[i]/(lamda[i]**2-a_1_b2o3)**2 + a_2_b2o3*b_2_b2o3*lamda[i]/(lamda[i]**2-a_2_b2o3)**2 +a_3_b2o3*b_3_b2o3*lamda[i]/(lamda[i]**2-a_3_b2o3)**2)
    derivative_one_b2o3.append(der)

for i in range(len(derivative_one_b2o3)):
    second_der = (1/(-1)*N_b2o3[i]) * ( (-3*a_1_b2o3*b_1_b2o3*lamda[i]**4 + 2*a_1_b2o3**2 * b_1_b2o3*lamda[i]**2 + a_1_b2o3**3 * b_1_b2o3)/(lamda[i]**2-a_1_b2o3)**4    +   (-3*a_2_b2o3*b_2_b2o3*lamda[i]**4 + 2*a_2_b2o3**2 * b_2_b2o3*lamda[i]**2 + a_2_b2o3**3 * b_2_b2o3)/(lamda[i]**2-a_2_b2o3)**4   +   (-3*a_3_b2o3*b_3_b2o3*lamda[i]**4 + 2*a_3_b2o3**2 * b_3_b2o3*lamda[i]**2 + a_3_b2o3**3 * b_3_b2o3)/(lamda[i]**2-a_3_b2o3)**4   +    derivative_one_b2o3[i]**2)
    derivative_two_b2o3.append(second_der)

print("this is the value of second derivative of b2o3")
print(derivative_two_b2o3)



plt.plot(lamda, derivative_two_sio2, color ='Magenta',markersize = 12,label ='PURE SIO2')
plt.plot(lamda, derivative_two_geo2, color ='red',markersize = 12,label ='Geo2')
plt.plot(lamda, derivative_two_b2o3, color ='green',markersize = 12,label ='B2O3')

plt.xlabel('value of lamda') 
plt.ylabel('this is d^2n/d_lamda^2 value')
plt.title('this is a graph of PURE SIO2 , GEO2 , B2O3 optical fiber materials ----- SECOND DERIVATIVE')
plt.legend()
plt.show()