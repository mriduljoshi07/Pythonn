dictionary = {"name": "Manan", "age": 19, "city": "delhi","slave":"nigger"};
print(dictionary);                                               # Create dictionary

# accessing values from dictionary
print(dictionary["name"]);
print(dictionary.get("name"));

# adding/updating items in dictionary 
dictionary["age"]=22;
print(dictionary);                                           # Update value of existing key in dictionary
dictionary["supplier"]="Mridul";                             # Adding new key-value pair in dictionary
print(dictionary);
dictionary.update({"city":"New delhi"});
print(dictionary);                                               # Update value of existing key in dictionary using update() method

# setdefault method
dictionary.setdefault("country","India");
print(dictionary.setdefault("name","Munnu"));                    # returns existing value of key if present
print(dictionary);                                               # Add key-value pair to dictionary using setdefault() method if key does not exist, otherwise return existing value

# deleting elements
dictionary.pop("age");
print(dictionary);                                             # Remove key-value pair from dictionary using pop() method
dictionary.popitem();
print(dictionary);                                             # Remove last inserted key-value pair from dictionary using popitem() method
del dictionary["city"];
print(dictionary);                                             # Remove key-value pair from dictionary using del keyword
d1={"country":"India","population":1000000000};
d1.clear();
print(d1);                                               # Clear all key-value pairs from dictionary

# dictionary views
print(dictionary.keys());                                               # Get all keys from dictionary
print(dictionary.values());                                               # Get all values from dictionary
print(dictionary.items());                                               # Get all key-value pairs from dictionary

# copying the dictionary
dict2=dictionary.copy();
print(dict2);                                               # Create a shallow copy of dictionary using copy() method

