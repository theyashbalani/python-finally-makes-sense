squares = [ n**2 for n in range (1,11) ]
print(squares)

print(25*"---")

odds = [n for n in range(1,20,2)]
print(odds)

print(25*"---")

mapping = { s: len(s) for s in ["web", "db", "cache"]}
print(mapping)

print(25*"---")

unique = { n for n in [1,2,2,3,3,4,4,4]}
print(unique)

print(25*"---")

#generators
gen = ( n**3 for n in range(5))
print(gen)
print(next(gen))
print(list(gen))

print(25*"---")

servers = [
    {"hostname":"web","cpu":42},
    {"hostname":"db","cpu":91},
    {"hostname":"cache","cpu":61}
]

hosts = [server["hostname"] for server in servers if server["cpu"] > 80]
print(hosts)

print(25*"---")

compute = {server["hostname"]: server["cpu"] for server in servers}
print(compute)

print(25*"---")

servers = [
    {"hostname":"web","zone":"a"},
    {"hostname":"db","zone":"b"},
    {"hostname":"cache","zone":"a"}
]

unique_zones = {server["zone"] for server in servers}
print(unique_zones)

print(25*"---")

sqs = (n**2 for n in range(1, 101))
count = 0
while count < 5:
    print(next(sqs))
    count += 1

print(25*"---")

cpu_values = [45,82,61,91,72]

cpu80 = (cpu for cpu in cpu_values if cpu >= 80)
print(list(cpu80))

print(25*"---")
print(25*"---")

names = ["yash", "balani", "abhinav", "anurag", "shubham", "sankalp", "sarthak"]

result = [name.upper() for name in names]
print(result)

print(25*"---")

result = []

for name in names:
    result.append(name.upper())

print(result)


