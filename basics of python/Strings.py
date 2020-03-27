# Strings
# strings are used to record textual information as well as arbitary collections of bytes.
# Accesing Value in Strings
Name = "Johnny"

print(Name)

print(Name[0])

print(Name[3:])

print(Name[-1])

print(Name[-3:-1])

# Update Strings
var1 = "Hello World"
print(var1)

poem = """ twinkle twinkle little star
            how i wonder what you are """

print("2+3")
print(2+3)
print("Updated String :- ", var1 + 'Python')
print("Updated String :- ", var1[:5] + ' Python')


# String Formating
print("My name is %s and weight is %d kgs! my father name is %s " %
      ("vinod", 70, 'narasimha rao'))


#Ex :1

Name = input("Enter your name: ")

Age = int(input("Please Enter your age:"))


# eval() evaluates the string as python expression.
Weight = eval(input("Enter your Weight: "))
2.
print("1+1")
eval("1+1")



sum = eval("1+1")
sum

(Name, Weight)


# Triple Quotes

''
""
""" """

Statement = """Welcome to "python"
                basics "3"
                day session"""

print(Statement)
Name = "welcome to python"
print(Name.capitalize())


# count() method returns the number of occurrences of the substring in the given string.
x = "Welcome to python basics"
y = "o"

count = x.count(y)

# print count
print("The count is:", count)

# Count number of occurrences of a given substring using start and end
# define string
string = "Python is awesome, isn't it"
string[6]
string[25]

substring = "i"

# count after first 'i' and before the last 'i'
count = string.count(substring, 6, 25)

# print count
print("The count is:", count)

# Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.

Num = "M234567onica"  # No space in this string
print(Num.isalnum())

help(Num.isalnum)

Num = "this is string examplehi!!!"
Num.isalnum()


Num = "this is string example 0909090"
Num.isalnum()

Num = "123"
Num.isalnum()
# This method returns true if all characters in the string are alphabetic and there is at least one character, false otherwise.
Num = "this"  # No space & digit in this string
Num.isalpha()


# This method returns true if all characters in the string are digits and there is at least one character, false otherwise.

Num = "123456"  # Only digit in this string
Num.isdigit()

Num = "this is string example!!!"
Num.isdigit()

# his method returns a copy of the string in which all case-based characters have been lowercased.
Num = "THIS IS STRING EXAMPLE!!!"
Num.lower()

# his method returns a copy of the string in which all case-based characters have been Uppercase.
Num = "this is string example!!!"

Num.upper()


# The following example shows the usage of replace() method.

reply = "it is string example!!! is really a string"
print(reply.replace("is", "was"))
print(reply.replace("is", "was", 1))
help(reply.replace)


# The following example shows the usage of split() method.
split1 = "Line1-abcdef\nLine2-abc\nLine4-abcd"
print(split1.split("\n"))
help(split1.split)


