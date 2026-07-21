# Python Fundamentals

## Python Compiler Phases

Python is an interpreted, high-level language executed by the Python Virtual Machine.
Below is the compilation flow of the code.

```
Source Code
      │
      ▼
Lexer
      │
      ▼
Parser
      │
      ▼
Bytecode (.pyc)
      │
      ▼
Python Virtual Machine
      │
      ▼
Output
```

- **Source Code**: The Recipe. The `.py` files we write.
- **Lexer (Tokenizer)**: The Word Grouper. Reads source code and breaks it into tokens (keywords, operators, identifiers).
- **Parser**: The Grammar Checker. Builds an Abstract Syntax Tree (AST) from tokens to represent the code structure.
- **Bytecode (.pyc)**: The Simplified Code. The CPython compiler converts the AST into bytecode for faster execution.
- **Python Virtual Machine (PVM)**: The Chef. Interprets and executes the bytecode instructions into machine code that can be executed by the CPU.
- **Output**: The Meal. The final result printed to the console.

## Variables

- **Definition**: Variables are references to objects.
- **Note**: Meaningful names matter.

```python
name = "Yash"
age = 25
salary = 3.5
print(f"my name is {name}, i am {age} years old and i earn {salary} USD per month")

# Output:
# my name is Yash, i am 25 years old and i earn 3.5 USD per month
```

## Primitive Data Types

- **Definition**: Primitive data types are the basic building blocks of any programming language. They are the simplest form of data that can be stored in a variable.

```python
name = "Ubuntu"        # str
version = 24           # int
cpu = 83.4             # float
running = True         # bool
nothing = None         # NoneType

print(name, type(name))
print(version, type(version))
print(cpu, type(cpu))
print(running, type(running))
print(nothing, type(nothing))

# Output:
# Ubuntu <class 'str'>
# 24 <class 'int'>
# 83.4 <class 'float'>
# True <class 'bool'>
# None <class 'NoneType'>
```

## Collections

- **Definition**: Collections are containers that can store multiple values of different data types.

### List

- **Definition**: A list is an **ordered, mutable (changeable), and iterable** collection of elements. It can store elements of different data types.

```python
items = [1, 2, "Yash", 3.5, True]

print(items[0], type(items[0]))
print(items[1], type(items[1]))
print(items[2], type(items[2]))
print(items[3], type(items[3]))
print(items[4], type(items[4]))

# Output:
# 1 <class 'int'>
# 2 <class 'int'>
# Yash <class 'str'>
# 3.5 <class 'float'>
# True <class 'bool'>
```

### Tuple

- **Definition**: A tuple is an **ordered, immutable (unchangeable), and iterable** collection of elements. It can store elements of different data types.

```python
items = (1, 2, "Yash", 3.5, True)

print(items[0], type(items[0]))
print(items[1], type(items[1]))
print(items[2], type(items[2]))
print(items[3], type(items[3]))
print(items[4], type(items[4]))

# Output:
# 1 <class 'int'>
# 2 <class 'int'>
# Yash <class 'str'>
# 3.5 <class 'float'>
# True <class 'bool'>
```

### Set

- **Definition**: A set is an **unordered, mutable (changeable), and iterable** collection of **unique** elements. It can store elements of different data types.

```python
items = {1, 2, "Yash", 3.5, True, 1, 2, "Yash", 3.5, True}

print(items, type(items))

# Output:
# {1, 2, 'Yash', 3.5, True} <class 'set'>
```

### Dictionary

- **Definition**: A dictionary is an **ordered, mutable (changeable), and iterable** collection of **key-value** pairs. It can store elements of different data types.

- Almost every infrastructure object is represented as key-value data. Most DevOps tools communicate using JSON or YAML, and when Python reads JSON, it becomes a dictionary.

```python
items = {
    "name": "Yash",
    "age": 25,
    "salary": 3.5,
    "running": True
}

print(items, type(items))

# Output:
# {'name': 'Yash', 'age': 25, 'salary': 3.5, 'running': True} <class 'dict'>

items["name"] = "Ubuntu"
print(items)

# Output:
# {'name': 'Ubuntu', 'age': 25, 'salary': 3.5, 'running': True}

response = {
    "status": "success",
    "data": {
        "result": [
            {
                "cpu": 91
            }
        ]
    }
}

cpu = response["data"]["result"][0]["cpu"]
print("CPU: {}".format(cpu))

# Output:
# CPU: 91
```

## Operators

- **Definition**: Operators are special symbols that perform operations on variables and values.

### Arithmetic Operators

- **Definition**: Arithmetic operators are used to perform mathematical operations on variables and values.

```python
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulo
//  Floor Division
**  Exponentiation
```

```python
a = 5
b = 2

print(a + b)  # 7
print(a - b)  # 3
print(a * b)  # 10
print(a / b)  # 2.5
print(a % b)  # 1
print(a // b) # 2
print(a ** b) # 25
```

### Comparison Operators

- **Definition**: Comparison operators are used to compare two values.

```python
==  Equal to
!=  Not equal to
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to
```

```python
a = 5
b = 2

print(a == b) # False
print(a != b) # True
print(a > b)  # True
print(a < b)  # False
print(a >= b) # True
print(a <= b) # False
```

### Logical Operators

- **Definition**: Logical operators are used to perform logical operations on variables and values.

- **and**: It checks the first value. If it is truthy, it returns the second value. If it is falsy, it returns the first value
- **or**: It checks the first value. If it is truthy, it returns it immediately. It only looks at the second value if the first one is falsy.
- **not**: It turns truthy values into False and falsy values into True

```python
a = 5
b = 2

print(a and b) # 2
print(a or b)  # 5
print(not a)   # False
```

### Assignment Operators

- **Definition**: Assignment operators are used to assign values to variables.

```
= 	Assign
+= 	Add and Assign
-= 	Subtract and Assign
*= 	Multiply and Assign
/= 	Divide and Assign
%= 	Modulus and Assign
//= Floor Divide and Assign
**= Exponent and Assign
```

```python
a = 5
a += 2
print(a) # 7

a = 5
a -= 2
print(a) # 3

a = 5
a *= 2
print(a) # 10

a = 5
a /= 2
print(a) # 2.5

a = 5
a %= 2
print(a) # 1

a = 5
a //= 2
print(a) # 2

a = 5
a **= 2
print(a) # 25
```

### Membership Operators

- **Definition**: Membership operators are used to check if a value is present in a collection.

```python
a = 5
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a in b) # True
print(a not in b)  # False
```

## Input & Output

```python

name = input("Name: ") # Yash
age = int(input("Age: ")) # 25
salary = float(input("Salary: ")) # 3.5
running = bool(input("Running: ")) # True
nothing = input("Nothing: ") # None

print(name, type(name))
print(age, type(age))
print(salary, type(salary))
print(running, type(running))
print(nothing, type(nothing))

# Output

# Name: Yash <class 'str'>
# Age: 25 <class 'int'>
# Salary: 3.5 <class 'float'>
# Running: True <class 'bool'>
# Nothing: None <class 'NoneType'>
```

## Type Conversion

```python
str()

int()

float()

bool()

list()

tuple()

set()
```

```python
a = "25.5"

print(str(a), type(str(a))) # "25.5" <class 'str'>
print(int(a), type(int(a))) # ValueError: invalid literal for int() with base 10: '25.5'
print(float(a), type(float(a))) # 25.5 <class 'float'>
print(bool(a), type(bool(a))) # True <class 'bool'>
print(list(a), type(list(a))) # ['2', '5', '.', '5'] <class 'list'>
print(tuple(a), type(tuple(a))) # ('2', '5', '.', '5') <class 'tuple'>
print(set(a), type(set(a))) # {'2', '5', '.', '5'} <class 'set'>
```

```python
b = 25.5

print(str(b), type(str(b))) # "25.5" <class 'str'>
print(int(b), type(int(b))) # 25 <class 'int'>
print(float(b), type(float(b))) # 25.5 <class 'float'>
print(bool(b), type(bool(b))) # True <class 'bool'>
print(list(b), type(list(b))) # [25.5] <class 'list'>
print(tuple(b), type(tuple(b))) # (25.5,) <class 'tuple'>
print(set(b), type(set(b))) # {25.5} <class 'set'>
```

```python
c = True

print(str(c), type(str(c))) # "True" <class 'str'>
print(int(c), type(int(c))) # 1 <class 'int'>
print(float(c), type(float(c))) # 1.0 <class 'float'>
print(bool(c), type(bool(c))) # True <class 'bool'>
print(list(c), type(list(c))) # [True] <class 'list'>
print(tuple(c), type(tuple(c))) # (True,) <class 'tuple'>
print(set(c), type(set(c))) # {True} <class 'set'>
```

```python
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(str(d), type(str(d))) # "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" <class 'str'>
print(int(d), type(int(d))) # ValueError: invalid literal for int() with base 10: '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'
print(float(d), type(float(d))) # ValueError: could not convert string to float: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
print(bool(d), type(bool(d))) # True <class 'bool'>
print(list(d), type(list(d))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] <class 'list'>
print(tuple(d), type(tuple(d))) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) <class 'tuple'>
print(set(d), type(set(d))) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} <class 'set'>
```

```python
e = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(str(e), type(str(e))) # "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)" <class 'str'>
print(int(e), type(int(e))) # ValueError: invalid literal for int() with base 10: '(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)'
print(float(e), type(float(e))) # ValueError: could not convert string to float: "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"
print(bool(e), type(bool(e))) # True <class 'bool'>
print(list(e), type(list(e))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] <class 'list'>
print(tuple(e), type(tuple(e))) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) <class 'tuple'>
print(set(e), type(set(e))) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} <class 'set'>
```

```python
f = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(str(f), type(str(f))) # "{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}" <class 'str'>
print(int(f), type(int(f))) # ValueError: invalid literal for int() with base 10: '{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}'
print(float(f), type(float(f))) # ValueError: could not convert string to float: "{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"
print(bool(f), type(bool(f))) # True <class 'bool'>
print(list(f), type(list(f))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] <class 'list'>
print(tuple(f), type(tuple(f))) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) <class 'tuple'>
print(set(f), type(set(f))) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} <class 'set'>
```

```python
g = {"name": "Yash", "age": 25, "salary": 3.5, "running": True}

print(str(g), type(str(g))) # "{'name': 'Yash', 'age': 25, 'salary': 3.5, 'running': True}" <class 'str'>
print(int(g), type(int(g))) # ValueError: invalid literal for int() with base 10: "{'name': 'Yash', 'age': 25, 'salary': 3.5, 'running': True}"
print(float(g), type(float(g))) # ValueError: could not convert string to float: "{'name': 'Yash', 'age': 25, 'salary': 3.5, 'running': True}"
print(bool(g), type(bool(g))) # True <class 'bool'>
print(list(g), type(list(g))) # ['name', 'age', 'salary', 'running'] <class 'list'>
print(tuple(g), type(tuple(g))) # ('name', 'age', 'salary', 'running') <class 'tuple'>
print(set(g), type(set(g))) # {'name', 'age', 'salary', 'running'} <class 'set'>
```

## if / elif / else

```python
cpu = 91

if cpu > 90:
    print("Critical")
elif cpu > 75:
    print("Warning")
else:
    print("Healthy")

# Output:
# Critical
```

## for Loop

```
for item in collection:
    print(item)
```

```python
servers = ["web", "db", "cache"]

for server in servers:
    print(server)

# Output:
# web
# db
# cache
```

- **`range()` generates a sequence of numbers.**
- **Syntax:** `range(start, stop, step)`
- **`stop` is exclusive.**
- **`step` is optional.**
- **default `start` is 0.**

```
range(5) → 0 to 4
range(1, 6) → 1 to 5
range(2, 11, 2) → 2, 4, 6, 8, 10
```

```python
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
```

## while Loop

Use a `while` loop when you don't know in advance how many iterations are needed.

```python
count = 1

while count <= 5:
    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5
```

## break and continue

`break` stops the loop immediately.

```python
for cpu in [30, 55, 95, 60]:
    if cpu > 90:
        print("Critical server found")
        break

# Output
# Critical server found (at 95)
```

`continue` skips the current iteration.

```python
for cpu in [30, 55, 95, 60]:
    if cpu > 90:
        continue
    print(cpu)

# Output:
# 30
# 55
# 60
```

## Functions

- A function groups reusable logic under a name.
- A function must have **single responsibility**, other it will be **hard to read, review, debug, test, reuse, modify**.

```python
# function definition
def greet():
    print("Hello Canonical")

# function calling
greet()

# Output
# Hello Canonical
```

### Function Parameters

Parameters allow a function to work with different inputs.

- **Parameter**: Placeholder. Variable defined in the function definition.
- **Argument**: Actual value passed to the function.

```python
def greet(name):
    print(f"Hello {name}")

greet("Yash")
greet("Ubuntu")

# Output
# Hello Yash
# Hello Ubuntu
```

### Return Values

A function can return a result to its caller.

- `print()` displays a value.
- `return` gives the value back to the caller so it can be used later.
- Python automatically returns `None` if no return statement is specified.

```python
def add(a, b):
    return a + b

result = add(1, 2)
print(result)

# Output
# 3
```

## Iterating Over Dictionaries

```python
server = {
    "cpu": 81,
    "memory": 64
}

for key, value in server.items():
    print(key, value)

# Output
# cpu 81
# memory 64
```

## String Manipulation

- Strings help us process text.
- Strings are **immutable**, meaning they cannot be changed after creation.
- Python protects strings from accidental modification. Instead, Python creates a new string.

```python
name = "ubuntu"

name[0] = "U"

# Output
# TypeError: 'str' object does not support item assignment

name = "Ubuntu"  # This is valid, because it creates a new string
```

### String Indexing & Slicing

- **Indexing** → Retrieves one element.
- **Slicing** → Retrieves multiple elements (a portion of the sequence).
- Syntax: `string[start:stop:step]`
- Default `start` is 0. **start is included**
- Default `stop` is the length of the string. **stop is excluded**
- Default `step` is 1.
- Negative indexing starts from the end.

```python
name = "Ubuntu"

print(name[0])  # U

print(name[-1]) # u

text = "Canonical"

print(text[0:5]) # Canon, prints 5 characters from the start (stop is excluded)
print(text[:3])  # Can, print 3 characters from the start (stop is excluded)
print(text[2:])  # nonical, print characters from the index 2 to the end
print(text[:]) # Canonical, prints the entire string
print(text[::-1]) # lacinonaC, prints the string in reverse order
```

### Common String Methods

```python
name = "ubuntu"

print(name.upper()) # Converts the string to uppercase
print(name.lower()) # Converts the string to lowercase
print(name.capitalize()) # Capitalizes the first character of the string
print(name.title()) # Capitalizes the first character of each word in the string
print(name.swapcase()) # Swaps the case of each character in the string
#####
print(name.strip()) # Removes leading and trailing whitespace
Example file:
web
db
cache

with open("servers.txt") as f:
    for line in f:
        print(line.strip())

# Output:
# web
# db
# cache

# Actual Output Without strip()
# web\n
# db\n
# cache\n

line = "web\n"
print(line == "web") # False
print(line.strip() == "web") # True

#############

print(name.replace("ubuntu", "Canonical")) # Replaces all occurrences of a substring with another substring

#############
servers = "web,db,cache"
print(name.split(",")) # Splits the string into a list of substrings
# Output: ['web', 'db', 'cache']

servers = ["web", "db", "cache"]
print("-".join(servers)) # Joins the elements of an iterable with the specified separator into a string.
# Output: web-db-cache

split()

"web,db,cache"

↓

["web", "db", "cache"]


join()

["web", "db", "cache"]

↓

"web,db,cache"

############

print(name.startswith("prod")) # Checks if the string starts with a specific substring
print(name.endswith("dev")) # Checks if the string ends with a specific substring
print(name.find("ubuntu")) # Returns the index of the first occurrence of a substring, if not found then returns -1
print(name.index("ubuntu")) # Returns the index of the first occurrence of a substring, if not found then raises ValueError
print(name.count("ubuntu")) # Returns the number of occurrences of a substring

```

### f-Strings

Old way:

```python
host = "prod-1"

cpu = 81

print(host + " CPU is " + str(cpu) + "%")
```

Problem:

- Hard to read
- Need explicit conversion using `str()`
- Easy to forget spaces

New way:

```python
host = "prod-1"

cpu = 81

print(f"{host} CPU is {cpu}%")
```

- f-strings are preferred over string concatenation because they are:
  - **More readable**
  - **Faster**
  - **Easier to maintain**
  - **Less error-prone**

```python
name = "Ubuntu"

print(f"Hello {name}")
# Output: Hello Ubuntu
```

## List & Tuple Manipulation

- Lists help us process collections of things.
- Instead of storing each value separately, you group them together and can process them with a single loop.
- Lists are **mutable**, meaning they can be changed after creation.
- Tuples are **immutable**, meaning they cannot be changed after creation.

```python
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)

list_example[0] = 10  # This is valid
tuple_example[0] = 10  # This is invalid

# Output:
# TypeError: 'tuple' object does not support item assignment
```

### Common List Methods

```python
servers = ["web", "db"]
servers.append("cache") # ['web', 'db', 'cache'] Appends an element to the end of the list
servers.extend(["cache", "db2"]) # ['web', 'db', 'cache', 'db2'] Adds multiple elements to the end of the list


servers = ["web", "db"]
servers.insert(1, "cache") # ['web', 'cache', 'db'] Inserts an element at a specific index

servers = ["web", "db", "cache"]
servers.remove("cache") # ['web', 'db'] Removes the first occurrence of an element

servers = ["web", "db", "cache"]
last = servers.pop()
print(last) # cache Removes and returns the last element
print(servers) # ["web", "db"]

servers = ["web", "db", "cache"]
servers.pop(1) # db Removes and returns the element at a specific index
print(servers) # ["web", "cache"]

servers = ["web", "db", "cache"]
servers.index("cache") # 2 Returns the index of the first occurrence of an element
print(servers) # ["web", "db", "cache"]

servers = ["web", "db", "cache"]
servers.count("cache") # Returns the number of occurrences of an element
print(servers) # ["web", "db", "cache"]

servers = ["web", "db", "cache"]
servers.sort() # Sorts the list in place
# sorted() creates a new sorted list
print(servers) # ["cache", "db", "web"]

servers = ["web", "db", "cache"]
servers.reverse() # Reverses the list in place
print(servers) # ["cache", "db", "web"]

servers = ["web", "db", "cache"]
servers.clear() # Removes all elements from the list
print(servers) # []

servers = ["web", "db", "cache"]
new = servers.copy() # Returns a shallow copy of the list
print(new) # ["web", "db", "cache"]

servers = ["web", "db", "cache"]
len(servers) # 3 Returns the number of elements in the list
```

- Preserving order helps you reconstruct the sequence of events and identify the root cause. If the alerts are reordered, troubleshooting becomes more difficult.
- Preserve order whenever the sequence reflects: **Dependencies, Time, Execution order, Priority, Event chronology**
- When Python creates a list, it stores `Pointer to items`, `Capacity` and `Current length`. `len()` simply reads the stored number, hence `len()` considered an O(1) operation
- **Time Complexity O(1)** means that the time taken to perform the operation does not depend on the size of the input.

### Iterating with enumerate()

- `enumerate()` adds a counter to an iterable.
- It returns pairs of (index, value).
- This is useful for loops where you need both the index and the value.

```python
servers = ["web", "db", "cache"]

for index, server in enumerate(servers):
    print(index, server)

# Output:
# 0 web
# 1 db
# 2 cache
```

### Membership Testing

- Membership testing is used to check if an element exists in a sequence.

```python
servers = ["web", "db", "cache"]

if "db" in servers:
    print("Database server found")

# Output:
# Database server found
```

## Dictionary Manipulation

- The data is self-describing by storing key-value pairs
- A dictionary is designed for fast lookup.
- Each key acts like a unique identifier. If duplicate keys were allowed, Python wouldn't know which value to return
- Internally, dictionaries use a hash table.

```
Key
↓
Memory Location
↓
Value
```

- Use a List when you care about:
  - Position
  - Order
  - Sequence

- Use a Dictionary when you care about:
  - Meaning
  - Labels
  - Attributes

- Nested dictionaries naturally represent hierarchical systems.
- Nested dictionaries mirror the structure of real infrastructure.

```
Pod
│
├── metadata
│      ├── name
│      └── namespace
│
├── status
│      ├── phase
│      └── IP
│
└── spec
       ├── containers
       └── node
```

- APIs are not guaranteed to return every field. Sometimes fields are Missing, Null, Optional or Version dependent.
- Use `dict.get(key, default_value)` instead of `dict[key]` to avoid `KeyError`.
- Production systems should fail gracefully. Defensive programming is a hallmark of good SRE code.

- A fleet contains multiple servers. Each server has multiple properties. The natural representation is "List of dictionaries"

```python
server = {
    "hostname": "prod-1",
    "cpu": 81,
    "memory": 72
}

print(server["hostname"]) # prod-1
print(server["disk"]) # KeyError

disk = server.get("disk", 50) # If the key is not found, it returns the default value (no default value then returns None)
print(disk) # 50

server["disk"] = 80 # Python adds the key if it doesn't exist; otherwise, it updates the value.
server["cpu"] = 91

memory = server.pop("memory") # Removes the key-value pair and returns the value.
del server["cpu"] # Removes the key-value pair
```

### Dictionary Iteration

```python
for key in server: # keys only
    print(key)

for key in server.keys(): # keys only
    print(key)

for value in server.values(): # values only
    print(value)

for key, value in server.items(): # both
    print(key, value)


server = {
    "hostname": "prod-1",
    "cpu": 81,
    "memory": 72
}

server_copy = server.copy()
server_copy["disk"] = 50

print(server)
print(server_copy)
```

## File Handling

- Automation scripts rarely work only with variables in memory. They constantly interact with files such as:
  - Log files
  - Configuration files
  - Inventory files
  - Backup manifests
  - Kubernetes YAML
  - Environment files
  - CSV reports

- Built-in `open()` function returns a file object. Syntax: `open(file_path, mode)`
  - `file_path`: The path to the file you want to open.
  - `mode`: The mode in which you want to open the file. Common modes are:
    - `"r"`: Read (default)
    - `"w"`: Write (overwrites existing content)
    - `"a"`: Append (adds to the end of the file without deleting existing content)

- Never assume external resources will always be available. **Treat file operations as potentially unreliable and handle failures explicitly.**

```python
file = open("servers.txt", "r") # Open a file in read mode.
content = file.read() # returns the entire contents of the file as one string.
file.close() # Manually closes the file, If an exception occurs before close(), the file remains open

with open("servers.txt", "r") as file: # When the with block ends, with automatically closes the file.
    content = file.read() # Reads the entire file into memory at once. Suitable for small files.

with open("servers.txt", "r") as file: # Preferred for log files because it uses less memory.
    for line in file: # Reads one line at a time
        print(line.strip()) # Removes leading/trailing whitespace, including newline characters.

with open("report.txt", "w") as file: # Create a new file for writing. If the file already exists, its content is overwritten.
    file.write("Deployment Successful\n")
    file.write("Disk usage: 80%")


with open("report.txt", "a") as file: # Appends content in the end to an existing file. If the file does not exist, it creates a new one.
    file.write("\nDisk usage: 90%")

# Reading from non-existent files causes FileNotFoundError.
# Use try-except blocks to handle potential errors gracefully.
try: # Try to open and read the file.
    with open("servers.txt", "r") as file: # If the file does not exist, it raises FileNotFoundError
        print(file.read())
except FileNotFoundError: # Catches the FileNotFoundError and prints a friendly message.
    print("File not found")
```

## Exception Handling

- In the real world, your code interacts with systems you don't fully control. A good SRE writes software that expects failures and handles them predictably.
  - Files may be missing.
  - APIs may be unavailable.
  - Networks may fail.
  - Users may provide invalid input.
  - Cloud resources may not exist.

- An **Exception** is an object that represents an error occurring during program execution.
- **Exception handling** gives you two capabilities:
  - Keep your program running.
  - Do something safe instead of crashing.

- Catch an exception only if your code knows how to recover from it. Otherwise, let it propagate to a higher level where it can be handled appropriately.
  - Suppose Kubernetes API returns `Unauthorized`
  - Your script cannot magically fix authentication.
  - The exception should reach the deployment controller, which can:
    - Log the error
    - Notify engineers
    - Stop deployment

- Catching `Exception` is appropriate only at the top level of an application, where the goal is to:
  - Log the failure
  - Clean up resources
  - Exit gracefully
- It should not be the default way of handling errors throughout your code.

```python

try: # try the code in this block and monitor for exceptions
    value = int(input("Enter a number: "))
    result = 10 / value

    # It's sometimes useful to proactively raise an exception when you detect an invalid state.
    if value == 0:
        raise ValueError("Division by zero error")

# If the specified exception occurs, control moves to the matching except block
except ValueError as e: # store the exception object in a variable
    print(e) # print the exception object

except ZeroDivisionError:
    print("Zero is not allowed.")

else: # executes only if no exceptions are raised in the try block
    print("division successful")
    print(result)

finally: # always executes regardless of whether an exception was raised or not
    print("Execution completed")
```

- **Built-in Exceptions:** Choosing a specific exception type that fits your context helps write cleaner, more maintainable code
  - `ValueError`: Triggered when a function receives an argument of the correct type but an inappropriate value.
    ```python
    if age < 0:
        raise ValueError("Age cannot be negative.")
    ```
  - `TypeError`: Triggered when an operation or function is applied to an object of an inappropriate type.
    ```python
    if type(value) is not int:
        raise TypeError("Value must be an integer.")
    ```
  - `IndexError`: Raised when accessing a sequence index that is out of bounds.
    ```python
    if index < 0 or index >= len(sequence):
        raise IndexError("Index out of range.")
    ```
  - `KeyError`: Raised when accessing a non-existent key in a dictionary.
  - `RuntimeError`: Raised when an appropriate exception is not found.

- **SRE Rule**: Assume every external system can fail. Validate before you trust.

- Production environments are unpredictable. Good automation:
  - validates inputs
  - checks assumptions
  - handles failures
  - logs useful information
  - exits safely

- Cloud APIs are external systems. External systems are never 100% reliable.
- Cloud API common failures:
  - `timeout` (The request took too long)
  - `auth_error` (Bad credentials or insufficient permissions or expired token)
  - `permission_error` (You don't have access to this resource)
  - `resource_not_found` (You asked for a VM that doesn't exist)
  - `rate_limit_exceeded` (You hit the API usage cap)
  - `server_error` (Something went wrong on the API's end)
  - `temporary outage` (Cloud provider is having issues)
  - `invalid request` (The API rejected your input)

- A good error message answers three questions:
  - What failed?
  - Why did it fail?
  - What should the user do next?
  - **Examples:**
    - Deployment failed because Kubernetes API returned 401 Unauthorized. Verify that KUBECONFIG points to the correct cluster and that your credentials have not expired.
    - Failed to create VM: 502 Bad Gateway. Cloud API is likely experiencing temporary issues. Please try again in 5 minutes.
