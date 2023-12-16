# lambda function => used to simplify program
#                    does not have function name

add=lambda n1,n2:n1+n2
print(add(100,200))


#cube of a number

cube=lambda num:num**3
print(cube(5))


#check num is positive or negative

num_check=lambda num:"+ve" if num>0 else "-ve" if num<0 else "zero"
print(num_check(5))


# largest among 2 numbers

max_two=lambda num1,num2:num1 if num1>num2 else num2
print(max_two(12,13))


# odd or even number

odd_even=lambda num:"even" if num%2==0 else "odd"
print(odd_even(11))


# max of 3 numbers

max_three=lambda num1,num2,num3:num1 if num1>num2 and num1>num3 else num2 if num2>num1 and num2>num3 else num3 if num3>num1 and num3>num2 else "all 3 are equal"
print(max_three(4,7,6))
print(max_three(4,4,4))


# sort the longest word first

text="good evening all"
words=text.split(" ")
srt_words=sorted(words,key=lambda w:len(w),reverse=True)
print(srt_words) #['evening', 'good', 'all']

