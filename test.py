def multiply(a):
    return lambda b : a * b

"""
    => এই function টি কিন্তু 2 টি argument চাচ্ছে একটি multiply() এর `a` জন্যে,
    অন্যটি lambda এর ভেতর `b` এর জন্যে।
"""


## এখানে `a` এর value কে Constant করা হয়েছে।
obj = multiply(5)
"""
NOTE:- If `multiply(5, 6)`, then TypeError: multiply() takes 1 positional argument but 2 were given
তার মানে সে একটির বেশি parameter receive করে না।
"""


"""
    => এখানে `b` এর value কে argument হিসেবে pass করা হেয়েছে, যা মূলত 
    lambda function parameter হিসেবে accept করতেছে।
"""
result1 = obj(3)
result2 = obj(4)
result3 = obj(5)
result4 = obj(6)

print("Result 1 = ",result1)  ## Result 1 =  15  
print("Result 2 = ",result2)  ## Result 2 =  20
print("Result 3 = ",result3)  ## Result 3 =  25
print("Result 4 = ",result4)  ## Result 4 =  30 

