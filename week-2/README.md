# Python OOPS

- Real-world systems contain multiple related objects. Object-oriented design models those relationships.
- Classes allow you to model real-world entities inside your code.
- A K8s Cluster contains many Node objects.

```python
class Cluster:

    def __init__(self):
        self.nodes = []
```

- Each node contains many pods.

```python
class Node:

    def __init__(self):
        self.pods = []
```

- Each pod contains containers.

```python
class Pod:

    def __init__(self):
        self.containers = []
```

- It mirrors how Kubernetes itself models resources.

- Each resource has:
  - Data (state)
  - Operations (behavior)
  - Relationships with other resources
- This makes the code easier to extend, test, and maintain.

- Model software around real-world entities and their relationships. Large systems become easier to understand when each class has a single, well-defined responsibility.

- Encapsulation is one of the core ideas of object-oriented programming. It bundles data (attributes) and methods that operate on the data within a single unit (class). It helps to hide the internal state of an object and only expose the necessary functionality.
  - Easier to understand.
  - Easier to maintain.
  - Reduces bugs.
  - Keeps related code together.
  - Makes objects responsible for their own behavior.

## Python Classes & Objects

- A class stores data/state **(attributes)** and behavior **(methods)** together.
- A class is a blueprint for creating objects.
- Think of a class as an architectural drawing. You can build many houses from one blueprint.

```python
class Server:
    pass
```

- Each actual server is an object created from it.

```python
server = Server()

print(type(server)) # <class '__main__.Server'>
```

## `__init__()` Method

- Objects usually need initial data.
- The `__init__()` method is a special method that is called automatically when you create an object from a class. It is used to initialize the attributes of the object.
- Strictly speaking, `__init__()` is an initializer, not the constructor itself.
- An instance variable belongs to one specific object. Every object gets its own copy.
- Instance variables store the unique state of each object.
- Always initialize every attribute your object will use.

```python
class Server:
    def __init__(self, hostname, cpu):
        self.hostname = hostname
        self.cpu = cpu

server = Server("web-1", 42)

print(server.hostname) # web-1
```

## `self`

- `self` refers to the current object.
- It's the first argument of any method inside a class.
- It tells Python which object's data you're accessing.

```python

class Server:
    def __init__(self, hostname, cpu):
        print("creating server") # prints when object is created

server = Server("web-1", 42) # creating server
print(server.hostname) # web-1
# Output
# creating server
# web-1
```

```python
web = Server("web-1") # Server.__init__(web, "web-1") internally
```

## Class Methods

- Classes can contain functions called methods.

```python

class Server:
    def __init__(self, hostname):
        self.hostname = hostname

    def restart(self):
        print(f"Restarting {self.hostname}")

server = Server("web-1")
server.restart() # Restarting web-1
```

## Class vs Dictionary

- Use a dictionary when you simply need to store data.
- Use a class when the object has both **state (data/attributes)** and **behavior (methods)**.
- Many Python libraries you'll use are object-oriented. Instead of returning plain dictionaries, they often return objects with methods.

# Python Modules & Packages

- Modules let you split code into logical pieces.
- It is simply a Python file (.py) containing code.
- Each module has a single responsibility. It follows the Single Responsibility Principle (SRP) and makes it easier to test, debug, review, reuse and easier for multiple engineers to work on simultaneously.
- Python find modules in a specific order.
- If Python cannot find a module, you'll get `ModuleNotFoundError` which often caused by:
  - wrong folder
  - missing installation
  - incorrect virtual environment

```python

Import

↓

Current Folder

↓

Installed Packages

↓

Standard Library

↓

sys.path

# Directories listed in
import sys
print(sys.path)
# These paths tell Python where else to search.

```

```python

# health.py
def check_cpu(cpu):
    return cpu < 80

# main.py
import health
print(health.check_cpu(42))
```

- You can also import specific functions or classes.

```python
from math import sqrt
print(sqrt(16)) # don't need the module name
# Output: 4.0

import math as m # alias

print(m.pi) # Useful for long module names
```

- A package is a directory containing related modules.
- Packages help organize larger applications.
- Each file has one clear responsibility, making the codebase easier to test, review, and maintain.

```
automation/

    __init__.py

    aws.py

    kubernetes.py

    logging.py
```

```python
from automation import aws
```

## Standard Python Library Modules for SRE

- Python comes with many built-in modules. Here are some useful for SRE:
  - **os**: Interact with the operating system.

  ```python
    import os
    print(os.getcwd()) # Current working directory

  ```

  - **pathlib**: Handle file paths. (Modern approach, object-oriented, cleaner than os.path)

  ```python
  from pathlib import Path

  config = Path("config.yaml") # object, not a string

  print(config.name) # config.yaml

  from pathlib import Path
  path = Path("/var") / "logs" / filename # automatically builds the correct path. Cleaner and cross-platform

  ```

  - **sys**: Interact with the Python interpreter.

  ```python
  import sys

    print(sys.version) # Python version
  ```

  - **requests**: Make HTTP requests to interact with APIs.

  ```python
  import requests #

  resp = requests.get("https://google.com")
  print(resp.status_code) # 200
  ```

  - **json**: Work with JSON data (APIs return JSON).

  ```python
  import json

  data = {"name": "web-1", "cpu": 42}
  print(json.dumps(data)) # {"name": "web-1", "cpu": 42}

  data = json.loads('{"cpu": 81}')
  print(data["cpu"]) # 81
  ```

  - **re**: Work with regular expressions.

  ```python
  import re

  print(re.search(r"\d+", "web-1")) # <re.Match object; span=(3, 4), match='1'>
  ```

  - **subprocess**: Run external commands.

  ```python
  import subprocess

  subprocess.run(["ls", "-l"]) #
  ```

  - **logging**: Application logging.

  ```python
  import logging

  logging.warning("This is a warning")
  logging.error("This is an error")
  logging.critical("This is a critical error")
  ```

  - **datetime**: Work with dates and times.

  ```python
  import datetime

  now = datetime.datetime.now()
  print(now) # 2026-07-21 15:29:35.849553
  ```

  - **time**: For timestamps

  ```python
  import time

  print(time.time()) # 1753130975.849553
  time.sleep(5) #
  ```

## Iterators and Generators

- Iterators and Generators let Python process data one item at a time.

- An iterable is anything you can loop over.

```python
servers = ["web", "db", "cache"]

text = "Canonical"

server = {
    "hostname": "web-1"
}

for item in iterable:
    ...
```

- An iterator produces values one at a time.

```python
servers = ["web", "db", "cache"]

it = iter(servers)

print(next(it)) # web
print(next(it)) # db
print(next(it)) # cache
print(next(it)) # StopIteration Error
```

- A generator is a special type of iterator created with the `yield` keyword. Instead of returning everything at once, it pauses and resumes execution.

```python

def numbers():
    yield 1
    yield 2
    yield 3

for n in numbers():
    print(n)

# Output
# 1
# 2
# 3
```

### return vs yield

```python
def values():
    return [1, 2, 3] # The entire list is created before it is returned.

def generator():
    yield 1
    yield 2
    yield 3 # Values are produced one at a time. (Memory Efficient)
```

```python
def read_logs(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip()
```

### Lazy Evaluation

- Generators don't compute values until requested.
- Useful for large datasets.
- Saves memory.
- Ideal for streaming data.

```
Generator

↓

next()

↓

Compute one value

↓

Pause

↓

next()

↓

Compute next value
```

- Many production systems expose data as streams:
  - Log files
  - Kafka topics
  - API pagination
  - Monitoring events
  - Message queues

- Generators let you process these streams without exhausting system memory.

## Python Comprehension

- Many programming tasks involve:
  - filtering
  - transforming
  - collecting
- Comprehensions express these operations clearly.
- Python provides a shorter and often more readable way.

- Use a list comprehension when you want to build a new list by transforming or filtering items from an existing iterable.
- Use a traditional loop when the logic is complex or involves multiple actions.
- If you need to explain your comprehension, write a loop instead.

```python

cpu_values = [35, 81, 92, 61]

overloaded = []

for cpu in cpu_values: # 1. Loop
    if cpu > 80: # 2. Filter
        overloaded.append(cpu) # 3. Collect

overloaded = [cpu for cpu in cpu_values if cpu > 80] # loop + filter + collect

######

servers = [
    {"hostname":"web", "cpu":42},
    {"hostname":"db", "cpu":91},
    {"hostname":"cache", "cpu":61}
]

overloaded = [ s["hostname"] for s in servers if s["cpu"] > 80 ] # ["db"]
```

### List Comprehensions

- Use list comprehensions when you are building a new list from an existing iterable.
- For every item, produce a value.
- Syntax: `[expression for item in iterable if condition]`

```python
numbers = [1,2,3,4]

squares = [ n*n for n in numbers ] #[1,4,9,16]

evens = [ n for n in numbers if n % 2 == 0 ] # [2,4]
```

### Dictionary Comprehensions

- Use when creating a new dictionary from an iterable.
- When each item naturally maps to a key-value pair.
- Syntax: `{key_expr: value_expr for item in iterable if condition}`

```python
servers = ["web","db","cache"]

mapping = { s: "Running" for s in servers }
# {"web":"Running","db":"Running","cache":"Running"}
```

### Set Comprehensions

- Sets automatically remove duplicates.
- Choose a set comprehension when uniqueness matters more than order.

```python
servers = [
    "web",
    "db",
    "web",
    "cache"
]

unique = { s for s in servers } # {"cache", "db", "web"}
```

### Generator Expressions

- A list comprehension creates the entire list immediately. A generator expression creates values one at a time.
- Lists store everything. Generators calculate values only when requested.
- A generator expression returns a generator object. It does not return a list.
- They look similar but use parentheses `( )` instead of brackets `[ ]`.
- They return a generator object, not a list.
- Generator expressions are memory-efficient.
- Use generator expressions for very large datasets.

```python
[ n*n for n in numbers ] # list comprehension
( n*n for n in numbers) # generator
```

### When NOT to Use Comprehensions

- Readability is more important than writing fewer lines.
