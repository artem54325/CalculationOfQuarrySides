
a = -1.246
b = -5.841
c = 2.754
d = 0.766
n = -1.778
m = -4.729
g = 2.602

x = -2.232
y = -6.363
p = 2.764
q = 0.857
alha = 11.496
betta = 5.969

f = 0.577
u=1

# Первое уравнение
cal1 = (((f-2*p) * ((1-q*q)**(1/2))+
                           2*((f*f*q*q*(1-q*q)+p*(p-f))**(1/2)))/
                          (2*f*q*q+(2*p-f)*q-f))
print('\n Первое уравнение')
print(cal1, 0.523)
print((x-a), -0.984)

print('\n Второе уравнение')
# Второе уравнение
cal21 = ((2 * p - f * (1 + 2 * q))/(f - p))*(q - d)
cal22 = (((f - 2 * p)*(1 - q * q)**(1/2) + 2 * (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2))/((f - p)*(1 - q * q)**(1/2)))*(q - d)
cal23 = (u * (y - b)*(2 * p + (q - 1) * f)/((f - p) * p))
cal24 = (u * (x - a)*((q * q -1) * f)/(p * (f - p)*(1 - q * q)**(1/2)))
cal25 = (4 * (p - c) / f)

calFul = (((x-a) * (((f-2*p) * ((1-q*q)**(1/2))+
                           2*((f*f*q*q*(1-q*q)+p*(p-f))**(1/2)))/
                          (2*f*q*q+(2*p-f)*q-f)))-(y-b))


print(cal21, -0.152)
print(cal22, -0.17)
print(cal23, 0.468)
print(cal24, -0.05)
print(cal25, 0.042)
print(calFul, 0)


print('\n Третьте уравнение')
cal3Full = (((2 * p - f * (1 + 2 * q))/(f - p))*(q - d) +
                 (((f - 2 * p)*(1 - q * q)**(1/2) + 2 * (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2))/((f - p)*(1 - q * q)**(1/2)))*(q - d) +
                 (u * (y - b)*(2 * p + (q - 1) * f)/((f - p) * p)) +
                 (u * (x - a)*((q * q -1) * f)/(p * (f - p)*(1 - q * q)**(1/2))) -
                 (4 * (p - c) / f))
print(cal3Full, 0)


# a = 0.129
# b = -2.622
# c = 2.296
# d = -0.833
# n = -0.475
# m = -1.568
# g = 2.115
#
# x = -1.2
# y = -3.12
# p = 2.4
# q = -0.655
# alha = 8.42
# betta = 3.58
#
# f = 0.577
# u = 1
#
# # Первое уравнение
# cal1 = (((f-2*p) * ((1-q*q)**(1/2))+
#                            2*((f*f*q*q*(1-q*q)+p*(p-f))**(1/2)))/
#                           (2*f*q*q+(2*p-f)*q-f))
# print('\n Первое уравнение')
# print(cal1, 0.384)
# print((x-a), -1.329)
#
# print('\n Второе уравнение')
# # Второе уравнение
# cal21 = ((2 * p - f * (1 + 2 * q))/(f - p))*(q - d)
# cal22 = (((f - 2 * p)*(1 - q * q)**(1/2) + 2 * (f * f * q * q * (1 - q * q) + p * (p - f))**(1/2))/((f - p)*(1 - q * q)**(1/2)))*(q - d)
# cal23 = (u * (y - b)*(2 * p + (q - 1) * f)/((f - p) * p))
# cal24 = (u * (x - a)*((q * q -1) * f)/(p * (f - p)*(1 - q * q)**(1/2)))
# cal25 = (4 * (p - c) / f)
#
#
# print(cal21, -0.152)
# print(cal22, -0.17)
# print(cal23, 0.468)
# print(cal24, -0.05)
# print(cal25, 0.042)
