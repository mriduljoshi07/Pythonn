a=input("enter something : ")
print(a, type(a))

b=input("enter something again : ")
print(b, type(b))

c=a+b
print(c, type(c))                                                       # String concatenation
print(b*4);                                                             # String repetition

print(a[0:3])                                                           # String slicing
print(a[0:5:3])                                                         # String slicing with skip
print(a[::-1])                                                          # String slicing with reverse 

length_A=len(a)                                                         # length of string
print("length of string is", length_A)

txt="python";
print(txt.encode());
print(txt.encode().decode());