#------------------PYTHON---------------------#
# Python is an interpreted , high level programming language used for web development , data analytics , AI-ML etc


# Taking input from user
# a=input("enter the marks 1")
# a2=input("enter the marks 2")
# avg=0;
# avg+=(int(a)+int(a2))/2                                               # default input is taken in strings
# print("average marks is",avg)

# Type finding and conversion
# a=1;
# b=2.00;
# c=False;
# d="hello";
# print(type(a), type(b), type(c), type(d));

# m=float(a);                                                           # m gets converted to float
# print(m, type(m));

# Data types in python 

# 1) Dictionary
# 2) Boolean 
# 3) Set
# 4) Numeric ( integers , float , complex numbers )
# 5) Sequence ( list , tuple , strings )

# f string
# name=input("enter name : ");
# print(f"the name of the human is {name}")

str1=input("enter string 1 : ")
str2=input("enter string 2 : ")
count=0;
for i in str1:
    if i in str2:
        count=count+1
        print("letter common --> ",i)
print("no. of common letters in these strings are ",count)