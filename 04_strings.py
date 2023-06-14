print("Hello from string")

# String to a Variable
a = "String Variable"
print(a)

# Multiline Strings
b = """This is a 
example of
multiline string"""
print(b)

# Accessing elements of the string
c = "Example of string"
print(c[2])

# String Length
d = "Length"
print(len(d))

# Looping a String
for x in "String":      # Direct
    print(x)

e = "Looping"
for x in e:             # Using Variable
    print(x)

# Check String
txt = "This ia a simple line"
print("simple" in txt)      # Boolean Output

txt1 = "This is a another line"
if "another" in txt1:       # Using with if statement
    print("Match found")

# Check NOT
txt = "This is a simple line"
print("simple" not in txt)      # Boolean Output

txt1 = "This is a another line"
if "simple" not in txt1:        # Using with if statement
    print("Match not found")
