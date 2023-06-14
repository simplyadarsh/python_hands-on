# Slicing
a = "String"
print(a[3:5])

# Slicing from start
b = "Example of slicing"
print(b[:10])

# Slice till End
c = "Slicing to the end"
print(c[4:])

# Negative Indexing (start the slice from the end of the string)
d = "Let's start from end"
print(d[-7:-3])

'''----------------------------------------------------------
-----------------------------------------------------------------'''
# Modification of Strings

# Upper Case
a = "lower case to upper"
print(a.upper())

# Lower Case
b = "UPPER CASE TO LOWER"
print(b.lower())

# Removing whitespaces
c = "  There is whitespace in beginning and end of this string   "
print(c.strip())

# Replacing String
txt = "First string"
print(txt.replace("F","T"))       # Replacing particular character

txt1 = "Second replaced string"
print(txt1.replace("replaced","simple"))        # Replacing word

# Split String
str = "This is a base string,let's split it !!"
print(str.split(","))
    # Storing both strings into different variables
[tempstr1,tempstr2] = str.split(",")
print(tempstr1)
print(tempstr2)