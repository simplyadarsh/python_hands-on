a = 2
b = 3.01
string = 'Heloo World'
char = 'a'

print(a,end = ' ') # Type of variable in same line (Method-1)
print(type(a))
print(b,type(b))  # Type of variable in same line (Method-2)
print(string,type(string))

# Specifying data type with casting

x = str(2)
y = int(6.9)
z = float(5)

print(x,type(x))
print(y,type(y))
print(z,type(z))


# Multiple Values

m,n,o = 200, "NAME", 55.6

print(m, type(m))
print(n, type(n))
print(o, type(o))

# Unpacking using variable

student = ['Name', 20, 95.5]
s,t,u = student

print(s)
print(t)
print(u)
