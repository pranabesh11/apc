import matplotlib.pyplot as plt
import numpy as np


#lamda = [0.95,1.15,1.25,1.35,1.45,1.55,1.65]
lamda = [0.95,1.0,1.10,1.15,1.20,1.25,1.30,1.35,1.40,1.45,1.50,1.55,1.60,1.65]
#lamda = [0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9]




# this is for pure sio2.
N_sio2 =[]
derivative_one_sio2 = []
derivative_two_sio2 = []

b_1_sio2 =0.6961663#0.7058489#0.7347008#0.6910021#   #0.7347008#0.7083952#0.7347008 #0.6910021 # #
b_2_sio2 =0.4079426#0.4176021#0.4461191#0.4022430#   #0.4461191 #0.4203993#0.4461191 #0.4022430 # #
b_3_sio2 =0.8974794#0.8952753#0.8081698#0.9439644#   #0.8081698#0.8663412#0.8081698 # # #

a_1_sio2 =0.004679148#0.005202431#0.005847345#0.004981838#0.004679148  #0.005847345# 0.007290464#0.005847345 #0.004981838 # # 
a_2_sio2 =0.01351206#0.01287730#0.01552717#0.01375664#  #0.01552717#0.01050294#0.01552717 #0.01375664 # #
a_3_sio2 =97.93400#97.93401#97.93484#97.93353#  #97.93484#97.93428 #97.93484 #97.93353 # #

for i in range(len(lamda)):
    big_expression = (b_1_sio2/(lamda[i]**2-a_1_sio2)+b_2_sio2/(lamda[i]**2-a_2_sio2)+b_3_sio2/(lamda[i]**2-a_3_sio2)+1/lamda[i]**2)
    n = lamda[i]*(big_expression**0.5)
    N_sio2.append(n)
print("this is the value of n for sio2")
print(N_sio2)

for i in range(len(lamda)):
    der = (1/((-1)*N_sio2[i])) * ((a_1_sio2*b_1_sio2*lamda[i]/(lamda[i]**2-a_1_sio2)**2) + (a_2_sio2*b_2_sio2*lamda[i]/(lamda[i]**2-a_2_sio2)**2) + (a_3_sio2*b_3_sio2*lamda[i]/(lamda[i]**2-a_3_sio2)**2))
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







# this is for pure b2o3(5.2).
N_b2o3 =[]
derivative_one_b2o3 = []
derivative_two_b2o3 = []

b_1_b2o3 =0.6910021#0.6961663#0.7058489#0.7347008##   #0.7347008#0.7083952#0.7347008 #0.6910021 # #
b_2_b2o3 =0.4022430#0.4079426#0.4176021#0.4461191##   #0.4461191 #0.4203993#0.4461191 #0.4022430 # #
b_3_b2o3 =0.9439644#0.8974794#0.8952753#0.8081698##   #0.8081698#0.8663412#0.8081698 # # #

a_1_b2o3 =0.004981838#0.004679148#0.005202431#0.005847345##0.004679148  #0.005847345# 0.007290464#0.005847345 #0.004981838 # # 
a_2_b2o3 =0.01375664#0.01351206#0.01287730#0.01552717##  #0.01552717#0.01050294#0.01552717 #0.01375664 # #
a_3_b2o3 =97.93353#97.93400#97.93401#97.93484##  #97.93484#97.93428 #97.93484 #97.93353 # #

for i in range(len(lamda)):
    big_expression = (b_1_b2o3/(lamda[i]**2-a_1_b2o3)+b_2_b2o3/(lamda[i]**2-a_2_b2o3)+b_3_b2o3/(lamda[i]**2-a_3_b2o3)+1/lamda[i]**2)
    n = lamda[i]*(big_expression**0.5)
    N_b2o3.append(n)
print("this is the value of n for b2o3")
print(N_b2o3)

for i in range(len(lamda)):
    der = (1/((-1)*N_b2o3[i])) * ((a_1_b2o3*b_1_b2o3*lamda[i]/(lamda[i]**2-a_1_b2o3)**2) + (a_2_b2o3*b_2_b2o3*lamda[i]/(lamda[i]**2-a_2_b2o3)**2) + (a_3_b2o3*b_3_b2o3*lamda[i]/(lamda[i]**2-a_3_b2o3)**2))
    derivative_one_b2o3.append(der)

print("this is the value of first derivative of b2o3")
print(derivative_one_b2o3)

for i in range(len(derivative_one_b2o3)):
    #second_der = (1/N_b2o3[i]) * ( (-3*a_1_b2o3*b_1_b2o3*lamda[i]**4 + 2*a_1_b2o3**2 * b_1_b2o3*lamda[i]**2 + a_1_b2o3**3 * b_1_b2o3)/(lamda[i]**2-a_1_b2o3)**4    +   (-3*a_2_b2o3*b_2_b2o3*lamda[i]**4 + 2*a_2_b2o3**2 * b_2_b2o3*lamda[i]**2 + a_2_b2o3**3 * b_2_b2o3)/(lamda[i]**2-a_2_b2o3)**4   +   (-3*a_3_b2o3*b_3_b2o3*lamda[i]**4 + 2*a_3_b2o3**2 * b_3_b2o3*lamda[i]**2 + a_3_b2o3**3 * b_3_b2o3)/(lamda[i]**2-a_3_b2o3)**4   +    derivative_one_b2o3[i]**2)
    f_part = (1/lamda[i])*derivative_one_b2o3[i]
    s_part = (1/N_b2o3[i])*(derivative_one_b2o3[i]**2)
    t_part = (4*lamda[i]**2/N_b2o3[i])*((a_1_b2o3*b_1_b2o3/(lamda[i]**2-a_1_b2o3)**3) + (a_2_b2o3*b_2_b2o3/(lamda[i]**2-a_2_b2o3)**3) + (a_3_b2o3*b_3_b2o3/(lamda[i]**2-a_3_b2o3)**3))
    second_der = f_part-s_part+t_part 
    derivative_two_b2o3.append(second_der)

print("this is the value of second derivative of b2o3")
print(derivative_two_b2o3)

   





 # this is for pure geo2(19.3).
N_geo2_19_3 =[]
derivative_one_geo2_19_3 = []
derivative_two_geo2_19_3 = []

b_1_geo2_19_3 =0.7347008#0.6910021#0.6961663#0.7058489###   #0.7347008#0.7083952#0.7347008 #0.6910021 # #
b_2_geo2_19_3 =0.4461191#0.4022430#0.4079426#0.4176021###   #0.4461191 #0.4203993#0.4461191 #0.4022430 # #
b_3_geo2_19_3 =0.8081698#0.9439644#0.8974794#0.8952753###   #0.8081698#0.8663412#0.8081698 # # #

a_1_geo2_19_3 =0.005847345#0.004981838#0.004679148#0.005202431###0.004679148  #0.005847345# 0.007290464#0.005847345 #0.004981838 # # 
a_2_geo2_19_3 =0.01552717#0.01375664#0.01351206#0.01287730###  #0.01552717#0.01050294#0.01552717 #0.01375664 # #
a_3_geo2_19_3 =97.93484#97.93353#97.93400#97.93401#97.93484##  ##97.93428 #97.93484 #97.93353 # #

for i in range(len(lamda)):
    big_expression = (b_1_geo2_19_3/(lamda[i]**2-a_1_geo2_19_3)+b_2_geo2_19_3/(lamda[i]**2-a_2_geo2_19_3)+b_3_geo2_19_3/(lamda[i]**2-a_3_geo2_19_3)+1/lamda[i]**2)
    n = lamda[i]*(big_expression**0.5)
    N_geo2_19_3.append(n)
print("this is the value of n for geo2_19_3")
print(N_geo2_19_3)

for i in range(len(lamda)):
    der = (1/((-1)*N_geo2_19_3[i])) * ((a_1_geo2_19_3*b_1_geo2_19_3*lamda[i]/(lamda[i]**2-a_1_geo2_19_3)**2) + (a_2_geo2_19_3*b_2_geo2_19_3*lamda[i]/(lamda[i]**2-a_2_geo2_19_3)**2) + (a_3_geo2_19_3*b_3_geo2_19_3*lamda[i]/(lamda[i]**2-a_3_geo2_19_3)**2))
    derivative_one_geo2_19_3.append(der)

print("this is the value of first derivative of geo2_19_3")
print(derivative_one_geo2_19_3)

for i in range(len(derivative_one_geo2_19_3)):
    #second_der = (1/N_geo2_19_3[i]) * ( (-3*a_1_geo2_19_3*b_1_geo2_19_3*lamda[i]**4 + 2*a_1_geo2_19_3**2 * b_1_geo2_19_3*lamda[i]**2 + a_1_geo2_19_3**3 * b_1_geo2_19_3)/(lamda[i]**2-a_1_geo2_19_3)**4    +   (-3*a_2_geo2_19_3*b_2_geo2_19_3*lamda[i]**4 + 2*a_2_geo2_19_3**2 * b_2_geo2_19_3*lamda[i]**2 + a_2_geo2_19_3**3 * b_2_geo2_19_3)/(lamda[i]**2-a_2_geo2_19_3)**4   +   (-3*a_3_geo2_19_3*b_3_geo2_19_3*lamda[i]**4 + 2*a_3_geo2_19_3**2 * b_3_geo2_19_3*lamda[i]**2 + a_3_geo2_19_3**3 * b_3_geo2_19_3)/(lamda[i]**2-a_3_geo2_19_3)**4   +    derivative_one_geo2_19_3[i]**2)
    f_part = (1/lamda[i])*derivative_one_geo2_19_3[i]
    s_part = (1/N_geo2_19_3[i])*(derivative_one_geo2_19_3[i]**2)
    t_part = (4*lamda[i]**2/N_geo2_19_3[i])*((a_1_geo2_19_3*b_1_geo2_19_3/(lamda[i]**2-a_1_geo2_19_3)**3) + (a_2_geo2_19_3*b_2_geo2_19_3/(lamda[i]**2-a_2_geo2_19_3)**3) + (a_3_geo2_19_3*b_3_geo2_19_3/(lamda[i]**2-a_3_geo2_19_3)**3))
    second_der = f_part-s_part+t_part 
    derivative_two_geo2_19_3.append(second_der)

print("this is the value of second derivative of geo2_19_3")
print(derivative_two_geo2_19_3)  








# this is for p2o5(10.5).
N_p2o5_10_5 =[]
derivative_one_p2o5_10_5 = []
derivative_two_p2o5_10_5 = []

b_1_p2o5_10_5 =0.7058489#0.7083952#0.7058489#0.7347008#0.6910021#0.6961663   #0.7347008#0.7083952#0.7347008 #0.6910021 # #
b_2_p2o5_10_5 =0.4176021#0.4203993#0.4176021#0.4461191#0.4022430#0.4079426   #0.4461191 #0.4203993#0.4461191 #0.4022430 # #
b_3_p2o5_10_5 =0.8952753#0.8663412#0.8952753#0.8081698#0.9439644#0.8974794   #0.8081698#0.8663412#0.8081698 # # #

a_1_p2o5_10_5 =0.005202431#0.007290464#0.005202431#0.005847345#0.004981838#0.004679148  #0.005847345# 0.007290464#0.005847345 #0.004981838 # # 
a_2_p2o5_10_5 =0.01287730#0.01050294#0.01287730#0.01552717#0.01375664#0.01351206  #0.01552717#0.01050294#0.01552717 #0.01375664 # #
a_3_p2o5_10_5 =97.93401#97.93428#97.93401#97.93484#97.93353#97.93400  #97.93484#97.93428 #97.93484 #97.93353 # #

for i in range(len(lamda)):
    big_expression = (b_1_p2o5_10_5/(lamda[i]**2-a_1_p2o5_10_5)+b_2_p2o5_10_5/(lamda[i]**2-a_2_p2o5_10_5)+b_3_p2o5_10_5/(lamda[i]**2-a_3_p2o5_10_5)+1/lamda[i]**2)
    n = lamda[i]*(big_expression**0.5)
    N_p2o5_10_5.append(n)
print("this is the value of n for p2o5_10_5")
print(N_p2o5_10_5)

for i in range(len(lamda)):
    der = (1/((-1)*N_p2o5_10_5[i])) * ((a_1_p2o5_10_5*b_1_p2o5_10_5*lamda[i]/(lamda[i]**2-a_1_p2o5_10_5)**2) + (a_2_p2o5_10_5*b_2_p2o5_10_5*lamda[i]/(lamda[i]**2-a_2_p2o5_10_5)**2) + (a_3_p2o5_10_5*b_3_p2o5_10_5*lamda[i]/(lamda[i]**2-a_3_p2o5_10_5)**2))
    derivative_one_p2o5_10_5.append(der)

print("this is the value of first derivative of p2o5_10_5")
print(derivative_one_p2o5_10_5)

for i in range(len(derivative_one_p2o5_10_5)):
    #second_der = (1/N_p2o5_10_5[i]) * ( (-3*a_1_p2o5_10_5*b_1_p2o5_10_5*lamda[i]**4 + 2*a_1_p2o5_10_5**2 * b_1_p2o5_10_5*lamda[i]**2 + a_1_p2o5_10_5**3 * b_1_p2o5_10_5)/(lamda[i]**2-a_1_p2o5_10_5)**4    +   (-3*a_2_p2o5_10_5*b_2_p2o5_10_5*lamda[i]**4 + 2*a_2_p2o5_10_5**2 * b_2_p2o5_10_5*lamda[i]**2 + a_2_p2o5_10_5**3 * b_2_p2o5_10_5)/(lamda[i]**2-a_2_p2o5_10_5)**4   +   (-3*a_3_p2o5_10_5*b_3_p2o5_10_5*lamda[i]**4 + 2*a_3_p2o5_10_5**2 * b_3_p2o5_10_5*lamda[i]**2 + a_3_p2o5_10_5**3 * b_3_p2o5_10_5)/(lamda[i]**2-a_3_p2o5_10_5)**4   +    derivative_one_p2o5_10_5[i]**2)
    f_part = (1/lamda[i])*derivative_one_p2o5_10_5[i]
    s_part = (1/N_p2o5_10_5[i])*(derivative_one_p2o5_10_5[i]**2)
    t_part = (4*lamda[i]**2/N_p2o5_10_5[i])*((a_1_p2o5_10_5*b_1_p2o5_10_5/(lamda[i]**2-a_1_p2o5_10_5)**3) + (a_2_p2o5_10_5*b_2_p2o5_10_5/(lamda[i]**2-a_2_p2o5_10_5)**3) + (a_3_p2o5_10_5*b_3_p2o5_10_5/(lamda[i]**2-a_3_p2o5_10_5)**3))
    second_der = f_part-s_part+t_part 
    derivative_two_p2o5_10_5.append(second_der)

print("this is the value of second derivative of p2o5_10_5")
print(derivative_two_p2o5_10_5)







# this is for pure geo2_6_3(6.3).
N_geo2_6_3 =[]
derivative_one_geo2_6_3 = []
derivative_two_geo2_6_3 = []

b_1_geo2_6_3 =0.7083952#0.7058489#0.7347008#0.6910021#0.6961663   #0.7347008#0.7083952#0.7347008 #0.6910021 # #
b_2_geo2_6_3 =0.4203993#0.4176021#0.4461191#0.4022430#0.4079426   #0.4461191 #0.4203993#0.4461191 #0.4022430 # #
b_3_geo2_6_3 =0.8663412#0.8952753#0.8081698#0.9439644#0.8974794   #0.8081698#0.8663412#0.8081698 # # #

a_1_geo2_6_3 =0.007290464#0.005202431#0.005847345#0.004981838#0.004679148  #0.005847345# 0.007290464#0.005847345 #0.004981838 # # 
a_2_geo2_6_3 =0.01050294#0.01287730#0.01552717#0.01375664#0.01351206  #0.01552717#0.01050294#0.01552717 #0.01375664 # #
a_3_geo2_6_3 =97.93428#97.93401#97.93484#97.93353#97.93400  #97.93484#97.93428 #97.93484 #97.93353 # #

for i in range(len(lamda)):
    big_expression = (b_1_geo2_6_3/(lamda[i]**2-a_1_geo2_6_3)+b_2_geo2_6_3/(lamda[i]**2-a_2_geo2_6_3)+b_3_geo2_6_3/(lamda[i]**2-a_3_geo2_6_3)+1/lamda[i]**2)
    n = lamda[i]*(big_expression**0.5)
    N_geo2_6_3.append(n)
print("this is the value of n for geo2_6_3")
print(N_geo2_6_3)

for i in range(len(lamda)):
    der = (1/((-1)*N_geo2_6_3[i])) * ((a_1_geo2_6_3*b_1_geo2_6_3*lamda[i]/(lamda[i]**2-a_1_geo2_6_3)**2) + (a_2_geo2_6_3*b_2_geo2_6_3*lamda[i]/(lamda[i]**2-a_2_geo2_6_3)**2) + (a_3_geo2_6_3*b_3_geo2_6_3*lamda[i]/(lamda[i]**2-a_3_geo2_6_3)**2))
    derivative_one_geo2_6_3.append(der)

print("this is the value of first derivative of geo2_6_3")
print(derivative_one_geo2_6_3)

for i in range(len(derivative_one_geo2_6_3)):
    #second_der = (1/N_geo2_6_3[i]) * ( (-3*a_1_geo2_6_3*b_1_geo2_6_3*lamda[i]**4 + 2*a_1_geo2_6_3**2 * b_1_geo2_6_3*lamda[i]**2 + a_1_geo2_6_3**3 * b_1_geo2_6_3)/(lamda[i]**2-a_1_geo2_6_3)**4    +   (-3*a_2_geo2_6_3*b_2_geo2_6_3*lamda[i]**4 + 2*a_2_geo2_6_3**2 * b_2_geo2_6_3*lamda[i]**2 + a_2_geo2_6_3**3 * b_2_geo2_6_3)/(lamda[i]**2-a_2_geo2_6_3)**4   +   (-3*a_3_geo2_6_3*b_3_geo2_6_3*lamda[i]**4 + 2*a_3_geo2_6_3**2 * b_3_geo2_6_3*lamda[i]**2 + a_3_geo2_6_3**3 * b_3_geo2_6_3)/(lamda[i]**2-a_3_geo2_6_3)**4   +    derivative_one_geo2_6_3[i]**2)
    f_part = (1/lamda[i])*derivative_one_geo2_6_3[i]
    s_part = (1/N_geo2_6_3[i])*(derivative_one_geo2_6_3[i]**2)
    t_part = (4*lamda[i]**2/N_geo2_6_3[i])*((a_1_geo2_6_3*b_1_geo2_6_3/(lamda[i]**2-a_1_geo2_6_3)**3) + (a_2_geo2_6_3*b_2_geo2_6_3/(lamda[i]**2-a_2_geo2_6_3)**3) + (a_3_geo2_6_3*b_3_geo2_6_3/(lamda[i]**2-a_3_geo2_6_3)**3))
    second_der = f_part-s_part+t_part 
    derivative_two_geo2_6_3.append(second_der)

print("this is the value of second derivative of geo2_6_3")
print(derivative_two_geo2_6_3)







plt.plot(lamda, derivative_two_sio2, color ='Magenta',markersize = 12,label ='PURE sio2')
plt.plot(lamda, derivative_two_b2o3, color ='black',markersize = 12,label =' b2o3')
plt.plot(lamda, derivative_two_geo2_19_3, color ='red',markersize = 12,label ='geo2(19.3)')
plt.plot(lamda, derivative_two_p2o5_10_5, color ='blue',markersize = 12,label ='p2o5(10.5)')
plt.plot(lamda, derivative_two_geo2_6_3, color ='yellow',markersize = 12,label ='geo2(6.3)')




plt.xlabel('value of lamda') 
plt.ylabel('this is d^2n/d_lamda^2 value')
plt.title('this is a graph of PURE sio2 && b2o3 && geo2(19.3) p2o5(10.5) geo2(6.3) optical fiber materials ----- SECOND DERIVATIVE')
plt.legend()
plt.show() 