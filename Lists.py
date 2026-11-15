list1=[10,20,1110,40,50];
print(list1);
random="nigger","manan",1,2,3,4,5,3,3,3,True;
l1=list(random);
print(l1);                                               # Create list from tuple
print(sorted(list1,reverse=True));                                               # Sorted list
print(len(list1));                                               # Length of list
print(max(list1));                                               # Maximum element in list
print(min(list1));                                               # Minimum element in list
print(sum(list1));                                               # Sum of elements in list
print(list(enumerate(list1)));                                               # Enumerate of list


l1.append("helu");                                               # Append element in list
print(l1);
l1.extend(list1);                                                 # Extend list with another list
print(l1);                                              
l1.insert(1,"gay");                                               # Insert element at specific index
print(l1);
l1.remove(3);
print(l1);                                               # Remove element from list
l1.pop();
print(l1);                                               # Pop element from list
l1.pop(5);
print(l1);                                               # Pop element from specific index
list1.clear();
print(list1);                                               # Clear all elements from list
print(l1.index(1,3,8));                                               # Index of element in list
print(l1.count(3));                                               # Count of element in list
# l1.sort(reverse=True);                                               # Sort list in descending order
# print(l1);                                             
print(l1.reverse());                                               # Reverse list
l2=l1.copy();                                               # Copy list
print(l2);
l1.reverse();                                               # Reverse list
print(l1);

if l2.reverse()==l1:
    print("balle balle");
else:
    print("no balle balle");