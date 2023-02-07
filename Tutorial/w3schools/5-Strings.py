# Multiline Strings
a = """
    <html>
        <head>
            <title>Kuda</title>
        </head>
        <body>
            <h1>Hallo Python</h1>
        </body>
    </html>
"""

print(a)

#String are arrays
a = "Hello Python"
print(a[3], end="\n\n")

#Looping through a String
for x in a :
    print(x)

#len()
a = "Hello, World"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("are" in txt)

# Check if NOT
txt = "The best things in life are free!"
print("expresive" in txt)

# Slicing
b = "Hello, World!!!"
print(b[2:5])

# Slice From the Start
print(b[:5])

# Slice To the End
print(b[2:])

# Negative Start
print(b[:-5])

# Negative End
print(b[-2:])

# Negative Slicing
print(b[-2:-5])

# UPPER CASE
print(b.upper())

# LOWER CASE
print(b.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
a = " Hello Python "
print(a)
print(a.strip())

a = "# Hello Python #"
print(a)
print(a.strip('#'))

# Replace String
a = "Hello Python"
print(a.replace("Python", 'Java'))

# Split String
a = "mangga jeruk semangka"
print(a.split(" "))

# Normal Concat
a = "Hello"
b = "Python"
print(a + b)

# String Format
age = 21
name = "John"
txt = "My name is {}, I am {} "
print(txt.format(name, age))

# String format using number
age = 21
name = "John"
txt = "My name is {1}, I am {0}"
print(txt.format(age, name))

