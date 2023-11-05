import math

import sympy
from sympy import diff
 


x=sympy.symbols('x')
derece=math.pi/5
taylor_1_terimli=math.cos(0)-math.sin(0)*(derece-x)
taylor_2_terimli=math.cos(0)-math.sin(0)*(derece-x)-(math.cos(0)*derece**2)/2

kesmehatasi_1=math.cos(derece)-taylor_1_terimli
kesmehatasi_2=math.cos(derece)-taylor_2_terimli

print("1.TAYLOR SERİSİ: {0}".format(taylor_1_terimli))
print("2.TAYLOR SERİSİ: {0}".format(taylor_2_terimli))

print("TAYLOR SERİSİNİN 1 TERİMLİ KESME HATASI: {0} ".format (kesmehatasi_1))
print("TAYLOR SERİSİNİN 2 TERİMLİ KESME HATASI: {0} ".format (kesmehatasi_2))
