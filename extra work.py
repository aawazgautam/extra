# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:49:02 2022

@author: Awaz
"""
#assigning the constants given in question.
n=0.02
s=.03 # 3%
q=15000 #cfs
b_max = 600 #ft 
#A= Area = by+y^2
#R= wetted perimeter = b+2*1.41*y

from sympy import symbols, Eq, solve  # sympy library imported for solving equation.

#Writing function for solving manings equation.
def maning (b_max):
    b=b_max
    y = symbols('y')

    eq1 = Eq(((1.49/n* (b+y)*y * pow((b+2*1.41*y),2/3) * pow(s,0.5))-q),0) # Mannings Equation 


    sol = solve(eq1)
    sol
    
    a=sol[0]  # taken Positive value of solution obtained of the equation. # value of y
    
    #y=0.027ft
       
    return sol
a=maning(b_max)

