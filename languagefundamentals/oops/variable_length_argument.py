# *args

# def product(*args):
#     result=1
#     for n in args:
#         result=result*n
#     return result

# def add(*args):
#     return sum(args)

# print(product(10,20))
# print(product(10,20,30))

# print(add(10,20))
# print(add(10,20,30))

# --------------------------------------------------------------


# print last digit sum

# def last_digit_sum(*args):
#     last_digit=0
#     for n in args:
#        last_digit=last_digit+n%10
#     return last_digit

#     #OR
#     # return sum([n%10 for n in args])

# print(last_digit_sum(123,345,567,760,678))


# --------------------------------------------------------------


# print last digit max

# def last_digit_max(*args):
#     digits=[n%10 for n in args]
#     return max(digits)

# print(last_digit_max(16,20,19,15))


# --------------------------------------------------------------


# **kwargs

# def add_employee(**kwargs):
#     print(kwargs.get("name"))
#     print(kwargs.get("salary"))

# add_employee(id=10,name="hari",n_place="ekm",w_place="tvm",salary=24000)


# --------------------------------------------------------------


# def my_fun(*args,**kwargs):
#     print(args) # tuple
#     print(kwargs)   # dict

# my_fun(23,45,17,36,reversed=True)


# --------------------------------------------------------------


# def last_digit_sort(*args,**kwargs):
#     digits=[n%10 for n in args]
#     value=kwargs.get("reversed")
#     if value==True:
#         digits.sort(reverse=True)
#     else:
#         digits.sort(reverse=False)
#     print(digits)

# last_digit_sort(17,12,14,3,1,reversed=True)
# last_digit_sort(17,12,14,3,1,reversed=False)


# --------------------------------------------------------------


# last_digit_calculator(423,234,123,453,567,op=+)
# op= + | -| * 

def last_digit_calculator(*args,**kwargs):
    digits=[n%10 for n in args]
    value=kwargs.get("op")
    if value=="+":
        print(sum(digits))
    elif value=="-":
        result=0
        for n in digits:
            result=n-result
        print(result)
    elif value=="*":
        result=1
        for n in digits:
            result=result
        print(result)

last_digit_calculator(423,234,123,453,567,op="+")
last_digit_calculator(423,234,123,453,567,op="-")
last_digit_calculator(423,234,123,453,567,op="*")



