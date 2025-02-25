import math
from sympy import symbols, diff, integrate, lambdify, sympify, deg
import re

def format_result(value):
    try:
        return math.floor(value) if math.isclose(value, round(value)) else value
    except:
        return None

def addition(num1, num2):
    try:
        return format_result(num1+num2)
    except:
        return None

def subtraction(num1, num2):
    try:
        return format_result(num1-num2)
    except:
        return None

def multiplication(num1, num2):
    try:
        return format_result(num1*num2)
    except:
        return None

def division(num1, num2):
    try:
        return format_result(num1/num2)
    except:
        return None

def remainder(num1, num2):
    try:
        return round(num1%num2, 10)
    except:
        return None
    

def evaluation(func, x, num):
    try:
        x = symbols(x)
        func_eval = lambdify(x, sympify(func), modules=["sympy"])
        return format_result(func_eval(num))
    except:
        return None

def differentiation(func, x, num=None):
    try:
        x = symbols(x)
        derivative = diff(sympify(func), x)
        return evaluation(str(derivative), x, num) if num is not None else str(derivative)
    except:
        return None

def integration(func, x, num1=None, num2=None):
    try:
        x = symbols(x)
        func = func.replace("^", "**")
        integral = integrate(sympify(func), x)
        if num1 is not None and num2 is not None:
            return format_result(evaluation(str(integral), x, num2)-evaluation(str(integral), x, num1))
        return str(integral)
    except:
        return None
    
def exponentiation(base, exponent):
    try:
        return format_result(base**exponent)
    except:
        return None

def square_root(num):
    try:
        return format_result(num**0.5)
    except:
        return None

def logarithm(num, base):
    try:
        return format_result(math.log(num, base))
    except:
        return None

def factorial(num):
    try:
        return math.factorial(int(num))
    except:
        return None

def gcd(num1, num2):
    try:
        return math.gcd(num1, num2)
    except:
        return None

def lcm(num1, num2):
    try:
        return math.lcm(num1, num2)
    except:
        return None

def absolute_value(num):
    try:
        return abs(num)
    except:
        return None

def trigonometric(func, angle):
    try:
        x = symbols('x')
        expr = sympify(func)
        result = expr.subs(x, angle)
        return format_result(result.evalf())
    except:
        return None

def inverse_trigonometric(func, value):
    try:
        x = symbols('x')
        expr = sympify(func)
        result = expr.subs(x, value)
        return format_result(deg(result.evalf()))
    except:
        return None

def hyperbolic(func, value):
    try:
        x = symbols('x')
        expr = sympify(func)
        result = expr.subs(x, value)
        return format_result(result.evalf())
    except:
        return None

def extract_numbers(text):
    return [float(n) for n in re.findall(r'[-+]?[0-9]*\.?[0-9]+', text)]