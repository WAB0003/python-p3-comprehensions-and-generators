
#! General Syntax for list comprehension
# new_list = [optional_operation(item) for item in old_list if optional_condition == True]

#? Practice:

one_to_three = range(1,4)

#List Comprehension uses square brackets
squared_lc = [n **2 for n in one_to_three]
print(squared_lc)

#Generateor expression uses parentheses
#GE's produce generator objects and NOT lists
squared_ge = (n**2 for n in one_to_three)
print(squared_ge)

