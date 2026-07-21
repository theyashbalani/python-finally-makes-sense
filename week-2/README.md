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
