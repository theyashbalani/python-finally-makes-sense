list = ["TEST", "ERROR"]
print ("ERROR" in list)


###
print("Hello Canonical")

###
myname = "Ubuntu"
print("Hello " + myname)
print(f"Hello {myname}")
print("Hello {}".format(myname))
print("Hello {name}".format(name=myname))

###
print(len(myname))
print(myname.upper())
print(myname.lower())
print(myname.title())
print(myname.capitalize())
print(myname.find("n"))
print(myname.replace("n", "N"))

###
cpu = 75

if cpu > 80:
    print("Critical")
elif cpu > 60:
    print("Warning")
else:
    print("Healthy")

###
servers = ["web", "db", "cache"]
print(servers[1])

###
server = {
    "cpu": 90,
    "storage": 80
}
print("Storage: {}".format(server["storage"]))

###
items = ["yash", 28, 25.6]
print(items)

###
server = {
    "hostname":"prod-1",
    "cpu":81,
    "memory":64
}

print("Hostname: {}".format(server["hostname"]))
print("CPU: {}".format(server["cpu"]))
print("Memory: {}".format(server["memory"]))

if server["cpu"] > 80 and server["memory"] > 80:
    print("Scale Up")
else:
    print("Healthy")
    





