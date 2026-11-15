nums=[1,12,34,56,32,8]
# print(sorted(nums,reverse=True));
# print(nums);
# print(list(map(str,nums)));

# # maps using user defined functions
# def s1(l1):
#     return sorted(nums);

# print(list(map(s1,nums)));
print(list(map(lambda x: x**3,nums)));



## FILTER
# num=["23","45","1","26"];
# num1=int(num);
# def even(s):
#        return s%2==0;

# print(list(filter(even,num1)))
n=[23,12,45,3,6,7,8];
print(list(filter(lambda x:x>7 and x%2==0,n)));    # lambda x: condition , iterable
print(list(map(str,nums))); 
            