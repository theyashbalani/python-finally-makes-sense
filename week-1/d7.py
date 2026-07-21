try:
  result = 10/0
except ZeroDivisionError as e:
  print(e)

####
try:
  num = int(input("Enter a number: "))
  if num == 0:
    raise ValueError("Invalid Value: Zero is not allowed")
  result = 10/num
  print(result)

except ValueError as e:
  print(e)


####
try:
  with open("file/servers.txt", "r") as file:
    print(file.read())
except FileNotFoundError as e:
  print(e)

###
####
try:
  result = 10/0
  print(result)
  
except Exception as e:  # Catching all types of exceptions
  print(e)

else:
  print("success")

finally:
  print("Operation Completed")

####
try:
  value = int("beta0")
except ValueError:
  print("Invalid")
else:
  print("Success")

####
try:
  print("running")
finally:
  print("Done")

####

def validate_cpu(cpu):
  try:
    if cpu < 0 or cpu > 100:
      raise ValueError("CPU is out of range")
  except ValueError as e:
    print(e)

validate_cpu(101)

####

def safe_divide(a, b):
  try:
    if b == 0:
      raise ValueError("Cannot divide by zero")
    return a/b

  except ValueError as e:
    print(e)

safe_divide(5,0)

#####

cpu_values = [35, 62, -5, 91, 110]
for cpu in cpu_values:
  try: 
    if cpu < 0 or cpu > 100:
      raise ValueError("Invalid CPU")
    print(cpu)
  except ValueError as e:
    print(e)
print("Finished")

  
#####

invalid_response = {
    "status_code": 500,
    "error": "Internal Server Error"
}
try: 
  if "hostname" not in invalid_response:
    raise KeyError("Missing required key: hostname")
except KeyError as e:
  print(e)

####

def deploy(server):
  try:
    if server["status"] != "Running":
      raise ValueError("Server is not Running")
  except ValueError as e:
    print(e)

server = {"hostname": "Server01", "status": "Stopped"}
deploy(server)

  