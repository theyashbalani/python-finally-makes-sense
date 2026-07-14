text = "CanoniCal"

print(text[0:5]) # Canon, prints 5 characters from the start (stop is excluded)
print(text[:3])  # Can, print 3 characters from the start (stop is excluded)
print(text[2:])  # nonical, print characters from the index 2 to the end
print(text[::-1])
print(text[::2])


print(text.upper())

### String Strip ###
text = ",Can,onical, "
print(text.strip(", "))

### String join and split ###

servers ="web, db, cache"
separate = servers.split(",")
print(separate)
print(type(separate))
print(",".join(separate))

###
myserver = "prod-api-01"

print(myserver[:4])

###

log = "ERROR nginx crashed"

for word in log.split(" "):
    print(word)

###

servers = [
    "web",
    "db",
    "cache"
]

print("-".join(servers))

###

hostname = "prod-db-01"
print(hostname.startswith("prod"))

myfile = "backup.tar.gz"
print(myfile.endswith(".gz"))

###

logs = "ERROR INFO ERROR WARNING ERROR"
print(logs.count("ERROR"))

###

host = "prod-api"
cpu = 91

print(f"{host} CPU usage is {cpu}%")

###

log = "2026-07-15 ERROR Payment Service Down"

print(log.split(" ")[1])