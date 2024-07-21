#!/usr/bin/env python
# coding: utf-8

# In[4]:


# This tutorial is on Python data types and some basic data manipulation.
#Basic Data Types and their Manipulation


# In[29]:


#BASIC DATA TYPES
#1. Integers
#Integers are whole numbers, positive or negative, without decimals.

#Example
a = 10
b = -5
print(a)
print(b)

# Arithmetic operations
sum_result = a + b
product_result = a * b

g(f"Sum: {sum_resprintult}")
print(f"Product: {product_result}")


# In[32]:


#2. Floats
#Floats are numbers with decimal points.

#Example
c = 10.5e-5
d = -3.14
print(c)
print(d)

print(f"Float: {c}, Type: {type(c)}")


# In[40]:


# 3. Strings
#Strings are sequences of characters enclosed in quotes.

#Example
e = "You people, hmm!!"
print(f"String: {e}, Type: {type(e)}")

# String operations
length = len(e)
print(f"Length of string: {length}")

# String slicing
substring = e[12:17]
print(f"Substring: {substring}")

# String formatting
Reason = "Finishing without me"
Feeling = f"Feeling betrayed for, {Reason}!"
print(Feeling)


# In[41]:


#3. Lists
#Lists are ordered, mutable collections of items.

#Example
lst = [1, 2, 3, 4, 5]
print(f"List: {lst}, Type: {type(lst)}")

# List operations
lst.append(6)
print(f"List after append: {lst}")

lst.remove(3)
print(f"List after remove: {lst}")

# List slicing
sublist = lst[1:4]
print(f"Sliced List: {sublist}")


# In[42]:


#4. Tuples
#Tuples are ordered, immutable collections of items.

#Example
tpl = (1, 2, 3, 4, 5)
print(f"Tuple: {tpl}, Type: {type(tpl)}")

# Tuple operations (note: you can't modify a tuple)
# Accessing elements
first_element = tpl[0]
print(f"First element: {first_element}")

# Slicing
subtuple = tpl[1:4]
print(f"Sliced Tuple: {subtuple}")


# In[48]:


#5. Booleans
#Booleans represent one of two values: True or False.
# Boolean variables
is_raining = True
is_sunny = False
print(f"is_raining: {is_raining}, Type: {type(is_raining)}")
print(f"is_sunny: {is_sunny}, Type: {type(is_sunny)}")

# Boolean operations
is_warm = True
is_winter = False

# Logical AND
print(f"Is it warm and not winter? {is_warm and not is_winter}")

# Logical OR
print(f"Is it either warm or winter? {is_warm or is_winter}")

# Logical NOT
print(f"Is it not sunny? {not is_sunny}")

# Comparison operations
a = 10
b = 20

is_a_greater = a > b
print(f"Is a greater than b? {is_a_greater}")

is_a_equal_b = a == b
print(f"Is a equal to b? {is_a_equal_b}")

is_a_not_equal_b = a != b
print(f"Is a not equal to b? {is_a_not_equal_b}")

# Using Booleans in conditional statements
if is_raining:
    print("Take an umbrella.")
else:
    print("No need for an umbrella.")

# Boolean expressions in lists
# List comprehension with condition
numbers = [1, 2, 3, 4, 5]
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Using all() and any() functions
all_positive = all(num > 0 for num in numbers)
print(f"Are all numbers positive? {all_positive}")

any_negative = any(num < 0 for num in numbers)
print(f"Are any numbers negative? {any_negative}")


# In[46]:


#6. Dictionaries
#Dictionaries are unordered, mutable collections of key-value pairs.

#Example
dct = {"name": "Arnold", "age": 23, "city": "Kasland"}
print(f"Dictionary: {dct}, Type: {type(dct)}")

# Accessing values
name = dct["name"]
print(f"Name: {name}")

# Adding a new key-value pair
dct["email"] = "arnold@gmail.com"
print(f"Dictionary after addition: {dct}")

# Removing a key-value pair
del dct["age"]
print(f"Dictionary after deletion: {dct}")


# In[47]:


#6. Sets
#Sets are unordered collections of unique items.

#Example
st = {1, 2, 3, 4, 5}
print(f"Set: {st}, Type: {type(st)}")

# Set operations
st.add(6)
print(f"Set after addition: {st}")

st.remove(3)
print(f"Set after removal: {st}")

# Set operations
another_set = {4, 5, 6, 7, 8}
union_set = st.union(another_set)
print(f"Union: {union_set}")

intersection_set = st.intersection(another_set)
print(f"Intersection: {intersection_set}")

