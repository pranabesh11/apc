import matplotlib.pyplot as plt
import numpy as np


#lamda = [0.95,1.15,1.25,1.35,1.45,1.55,1.65]
lamda = [0.95,1.0,1.10,1.15,1.20,1.25,1.30,1.35,1.40,1.45,1.50,1.55,1.60,1.65]
#lamda = [0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9]




# this is for pure sio2.
N_sio2 =[]
derivative_one_sio2 = []
derivative_two_sio2 = []
derivative_two_second_sio2 = []

b_1_sio2 =0.7347008#0.7083952#0.7347008 #0.6910021 # #0.6961663
b_2_sio2 =0.4461191 #0.4203993#0.4461191 #0.4022430 # #0.4079426
b_3_sio2 =0.8081698#0.8663412#0.8081698 #0.9439644 # #0.8974794

a_1_sio2 =0.005847345# 0.007290464#0.005847345 #0.004981838 # #0.004679148 
a_2_sio2 =0.01552717#0.01050294#0.01552717 #0.01375664 # #0.01351206
a_3_sio2 =97.93484#97.93428 #97.93484 #97.93353 # #97.93400

for i in range(len(lamda)):
    f_term = b_1_sio2/lamda[i]**2 - a_1_sio2
    s_term = b_2_sio2/lamda[i]**2 - a_2_sio2
    t_term = b_3_sio2/lamda[i]**2 - a_3_sio2
    fo_term = 1/lamda[i]**2
    big_expression = f_term + s_term + t_term + fo_term
    n = lamda[i]*(big_expression**0.5)
    N_sio2.append(n)
print("this is the value of n for sio2")
print(N_sio2)

for i in range(len(lamda)):
    out_term = ((-1)*lamda[i]) / N_sio2[i]
    fb_term = (a_1_sio2*b_1_sio2) / (lamda[i]**2 - a_1_sio2)**2
    sb_term = (a_2_sio2*b_2_sio2) / (lamda[i]**2 - a_2_sio2)**2
    tb_term = (a_3_sio2*b_3_sio2) / (lamda[i]**2 - a_3_sio2)**2
    der = out_term * (fb_term + sb_term + tb_term)
    derivative_one_sio2.append(der)

print("this is the value of first derivative of sio2")
print(derivative_one_sio2)

for i in range(len(derivative_one_sio2)):
    #second_der = (1/N_sio2[i]) * ( (-3*a_1_sio2*b_1_sio2*lamda[i]**4 + 2*a_1_sio2**2 * b_1_sio2*lamda[i]**2 + a_1_sio2**3 * b_1_sio2)/(lamda[i]**2-a_1_sio2)**4    +   (-3*a_2_sio2*b_2_sio2*lamda[i]**4 + 2*a_2_sio2**2 * b_2_sio2*lamda[i]**2 + a_2_sio2**3 * b_2_sio2)/(lamda[i]**2-a_2_sio2)**4   +   (-3*a_3_sio2*b_3_sio2*lamda[i]**4 + 2*a_3_sio2**2 * b_3_sio2*lamda[i]**2 + a_3_sio2**3 * b_3_sio2)/(lamda[i]**2-a_3_sio2)**4   +    derivative_one_sio2[i]**2)
    #f_part = (1/lamda[i])*derivative_one_sio2[i]
    #s_part = (1/N_sio2[i])*(derivative_one_sio2[i]**2)
    #t_part = (4*lamda[i]**2/N_sio2[i])*((a_1_sio2*b_1_sio2/(lamda[i]**2-a_1_sio2)**3) + (a_2_sio2*b_2_sio2/(lamda[i]**2-a_2_sio2)**3) + (a_3_sio2*b_3_sio2/(lamda[i]**2-a_3_sio2)**3))
    
    fs_term = (1/lamda[i]) * (derivative_one_sio2[i])
    ss_term = (1/N_sio2[i]) * (derivative_one_sio2[i])**2

    tso_term = (4*lamda[i]**2)/N_sio2[i]
    tsf_term = (a_1_sio2 * b_1_sio2) / (lamda[i]**2 - a_1_sio2)**3
    tss_term = (a_2_sio2 * b_2_sio2) / (lamda[i]**2 - a_2_sio2)**3
    tst_term = (a_3_sio2 * a_3_sio2) / (lamda[i]**2 - a_3_sio2)**3

    ts_term = tso_term * (tsf_term + tss_term + tst_term)

    second_der = fs_term - ss_term + ts_term
    derivative_two_sio2.append(second_der)



#for i in range(len(derivative_one_sio2)):
    
   # out_term = (-1) /N_sio2[i]
    #f_up_term = (a_1_sio2**2 * b_1_sio2) + (3*a_1_sio2*b_1_sio2*lamda[i]**2)
    #f_down_term = (lamda[i]**2 - a_1_sio2)**3
    #first_total =f_up_term/f_down_term

    #s_up_term = (a_2_sio2**2 * b_2_sio2) + (3 * a_2_sio2 * b_2_sio2 * lamda[i]**2)
    #s_down_term = (lamda[i]**2 - a_2_sio2)**3
    #second_total =s_up_term/s_down_term

    #t_up_term = (a_3_sio2**2 * b_3_sio2) + (3 * a_3_sio2 * b_3_sio2 * lamda[i]**2)
    #t_down_term = (lamda[i]**2 - a_3_sio2)**3
    #third_term = t_up_term/t_down_term

    #fourth_term = (derivative_one_sio2[i]**2)


    #second_der_alternate = out_term * (first_total + second_total + third_term + fourth_term)
    #derivative_two_second_sio2.append(second_der_alternate)



print("this is the value of second derivative of sio2")
print(derivative_two_sio2)

plt.plot(lamda, derivative_two_sio2, color ='Magenta',markersize = 12,label ='PURE SIO2')
#plt.plot(lamda, derivative_two_second_sio2, color ='red',markersize = 12,label ='PURE SIO2')

plt.xlabel('value of lamda') 
plt.ylabel('this is d^2n/d_lamda^2 value')
plt.title('this is a graph of PURE SIO2 optical fiber materials ----- SECOND DERIVATIVE')
plt.legend()
plt.show()