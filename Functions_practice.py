# Odd/Even function

# def check_num():
#     number=int(input("enter a number : "));
#     if number%2==0:
#         return "even"
#     else:
#         return "odd"
    
# result=check_num();
# print(result);

# Sum of as many numbers

# def sum_num():
#     sum=0;
#     while True:
#           number=(input("enter the numbr ; "));
#           if number=="done":
#                break;
#           else:
#                sum=sum+int(number);
#     return sum;

# result=sum_num();
# print("the total sum is ",result);
 
# Prime number check

# def isPrime():
#     number=int(input("enter your number : "));
#     if number<=1:
#         return "not a prime";
#     elif number==2:
#         return "yes, prime number";
#     elif number%2==0:
#         return "not prime number";
#     else:
#         for i in range(3,int(number**(0.5))+1,2):
#             if number%i==0:
#                 return "not prime";
                
#         return "yes prime";
        

# result=isPrime();
# print(result);

# Factorial function
# def fact():
#     num=int(input("enter a number : "));
#     if num<0:
#         return "factorial not defined for negatve nums"
#     value=1;
#     for i in range(1,num+1):
#         value*=i;
#     return value;

# result=fact();
# print("factorial is : ",result);

# Factorial using recursion   ( best time complexity and space complexity )
# def facto(n):
#     # n=int(input("enter your number : "));  # when taking parameters , dont ask user
#     if n<0:
#         return "niga , not defined for negative number";
#     elif n==1 or n==0:
#         return 1;
#     else:
#         return n*facto(n-1);

# result=facto(-1);
# print("my nigger , the factorial is : ",result);

# Palindrome check
# Fibonacci series

# Vowel count function
# def vowel_count(s):
#     count=0;
#     count2=0;
#     vowels="aeiouAEIOU"

#     for i in str:
#         if i in vowels:
#             count=count+1;
#     return count;

# str=input("enter your desired string : ")
# print("the number of vowels are ",vowel_count(str))
