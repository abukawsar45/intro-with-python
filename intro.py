print('Hey');


# Number
""" integer
    float
    complex"""


# String
""" string """
ab = "sad"
print(ab)



# Boolennan
""" boolean """
ab = "sad two"
cd = '34'
if(type(ab)==type(cd)):
 print(ab)
else:
 print(cd)

# operaton
'''+ - * / **power/exponential //nearest_integer_Quotient %_Remainder'''
age = 20

# calculation= age/2
# calculation= age**8
# calculation= age//8
calculation= age%8
print(calculation)

# comparison operator ==, !=, >, <, >=, <=
# print(5<=4)

# sting concatenation/join
first_name= "Abu"
last_name="Kawsar"
print(first_name+ " "+last_name)

# range = start, n-1 // 1, n-1 
# join
range_of_numbers = range(2, 11)
''' 1  =1
    1+2=3
    3+3=6
    6+4=10
    10+5=15
    15+6=21
    21+7=28
    28+8=36
    36+9=45
    36+10=55
    '''

sum_of_integers = sum(range_of_numbers)
print('sum of integers :', sum_of_integers)

# area of circle
radius = 3
area = 3.14159*radius*radius

# print(f"'area of a circle: ', {(3.14159*radius*radius):.2f}")
print(f"'area of a circle: ', {area:.2f}")

# ___________________________CONDITION_________________________________
# condition  // logical operator
result = 90
# indentation / space 

# if result>100 and result<0:
if result>100 or result<0:
   print('internal error')
elif result>=80 :
    print('Congratulation, your result is A+')
elif 60>=80 :
    print('Congratulation, your result is A')
else:
    print('fail')

# 