###
servers = ["web", "db", "api", "cache"]
it = iter(servers)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

print(100*"#")

def count():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for value in count():
    print (value)

print(100*"#")

def read_servers(servers):
    for server in servers:
        yield server
    
print(next(read_servers(servers)))

print(100*"#")

def even_numbers(limit):
    for even_num in range(2, limit, 2):
        yield even_num

for even_num in even_numbers(10):
    print(even_num)

print(100*"#")

def read_file():
    with open("week-2/file/log.txt", "r") as file:
        for line in file:
            if "ERROR" in str(line):
                yield line.strip()

for line in read_file():
    print(line)

print(100*"#")

servers = [
    {"hostname": "web-1", "cpu": 45},
    {"hostname": "db-1", "cpu": 92},
    {"hostname": "cache-1", "cpu": 61}
]

def healthy_servers(servers):
    for server in servers:
        if server["cpu"] <= 80:
            yield server

for server in healthy_servers(servers):
    print(server)

print(100*"#")




# gen = count()
# print(next(gen))


# print(100*"#")


# def read_items(items):
#     for item in items:
#         yield item

# items = read_items(['a', 'b', 'c'])
# for item in items:
#     print(item)



