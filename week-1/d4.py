servers =["web", "db", "ui"]

for server in servers:
    print(server)

for index, server in enumerate(servers):
    print(f"INDEX: {index} AND SERVER: {server}")

#####
servers.append("db")
print(servers)

servers.remove("db")
print(servers)

print(len(servers))

####
servers = ["worker", "db", "web", "cache"]

servers.sort()
print(servers)

servers.reverse()
print(servers)

####
last = servers.pop()
print(f"LAST SERVER: {last}")
print(servers)

if "worker" in servers:
    print("present")
else:
    print("not present")

####

def running_pods(pods):
    for i, pod in enumerate(pods):
        if pod.lower() == "running":
            print(f"Pod {i} is in running")

running_pods(["Running", "Pending", "Running", "Failed"])

####
def unique_servers(servers):
    unique = []
    for server in servers:
        if server not in unique:
            unique.append(server)
    return unique

print(unique_servers(["web", "db", "web", "cache", "db"]))

####
