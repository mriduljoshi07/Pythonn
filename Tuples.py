str="rohan is a boy","jelly";                      # Create tuple from string
tup=tuple(str);
print(tup);

tup1=tuple();
print(tup1);                                                # Empty tuple 

list1=[10,100,20,300];
tup2=tuple(list1);
print(tup2);                                               # Create tuple from list

# Dictionary to tuple
dict1={"name":"manan","slave":"nigger","age":24,"origin":"africa"};
tup_key=tuple(dict1);
print(tup_key);
tup_values=tuple(dict1.values());
print(tup_values);
tup_items=tuple(dict1.items());
print(tup_items);

print(len(tup2));                                               # Length of tuple
print(tup2.count(10));                                          # Count of element in tuple

tuple1=(2,4,7,1,9,11,0,2,4);
print("max element is,",max(tuple1));
print(tuple1[1:4]);                                               # Tuple slicing
print(tuple1.count(2));                                               # Count of element in tuple
print(tuple1.index(11,2,6));                                               # Index of element in tuple
print(len(tuple1));                                               # Length of tuple
print(sorted(tuple1));                                               # Sorted tuple
print(any(i>=11for i in tuple1));                                               # Check if any element is true
print(sum(tuple1));                                               # Sum of elements in tuple
print(all(i>=0 for i in tuple1));                                               # Check if all elements are true
print(list(enumerate(tuple1[1:3])));                                               # Enumerate of tuple