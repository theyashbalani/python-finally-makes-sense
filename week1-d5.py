server = {
    "hostname" : "prod-1",
    "cpu" : 81,
    "memory" : 100
}

print(server.values())

####
server["disk"] = 85
print(server)

###

server["cpu"] = 91
print(server)

print(server.get("cpu", 77))

####

print(server.get("network", "Not Available"))

for key in server.keys():
    print(key)

for value in server.values():
    print(value)

for key, value in server.items():
    print(key, value)

####
memory = server.pop("memory")
print(memory)
print(server)

####
servers = [
    {
        "hostname": "web-1",
        "cpu": 45
    },
    {
        "hostname": "db-1",
        "cpu": 91
    },
    {
        "hostname": "cache-1",
        "cpu": 82
    }
]

for server in servers:
    host = server["hostname"]
    cpu = server["cpu"]
    if cpu > 80:
        print(f"High CPU Alert: {host} is running at {cpu}%")


def average_cpu(servers):
    total_cpu = 0
    for server in servers:
        total_cpu += server["cpu"]
    return total_cpu / len(servers)


print(round(average_cpu(servers), 2))
    