"""
    euclid_gcd(0 is used to find the gcd of two numbers using euclidean algorithm
    @input: num1, num2 numbers
    @output gcd(num1,num2)
"""

def euclid_gcd(num1, num2):
    
    if num1 == 0:
        return num2    
    if num2 == 0 :
        return num1    
    if num1 < num2:
        return euclid_gcd(num2, num1)
    while num2 != 0:
        (num1, num2) = (num2, num1%num2)
    return num1
