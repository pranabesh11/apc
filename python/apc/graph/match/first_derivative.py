import matplotlib.pyplot as plt
import numpy as np

N =[]
derivative = []
derivative_two =[]
lamda = [0.95,1.15,1.25,1.35,1.45,1.55,1.65]

b_1 = 0.6961663
b_2 = 0.4079426
b_3 = 0.8974794

a_1 = 0.004679148
a_2 = 0.01351206
a_3 = 97.93400


for i in range(len(lamda)):
    big_expression = (b_1/(pow(lamda[i],2)-a_1)+b_2/(pow(lamda[i],2)-a_2)+b_3/(pow(lamda[i],2)-a_3)+1/pow(lamda[i],2))
    n = lamda[i]*pow(big_expression,0.5)
    N.append(n)



print(N)


for i in range(len(lamda)):
    der = 1/(-1)*N[i] * (a_1*b_1*lamda[i]/(lamda[i]**2-a_1)**2 + a_2*b_2*lamda[i]/(lamda[i]**2-a_2)**2 +a_3*b_3*lamda[i]/(lamda[i]**2-a_3)**2)
    derivative_two.append(der)



print(derivative_two)


for i in range(len(lamda)):
    d = pow(N[i],2)/pow(lamda[i],2) - lamda[i] * pow(N[i],2) * (b_1/(pow(lamda[i],2)-a_1)+b_2/(pow(lamda[i],2)-a_2)+b_3/(pow(lamda[i],2)-a_3)+1/pow(lamda[i],2))
    derivative.append(d)

print(derivative)



plt.plot(lamda, derivative_two, color ='Magenta',markersize = 12,label ='PURE SIO2')
plt.xlabel('value of lamda') 
plt.ylabel('this is dn/d_lamda value')
plt.title('this is a graph of PURE SIO2 optical fiber materials')
plt.legend()
plt.show()