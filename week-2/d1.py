# ####
# class Server:
#     pass

# ####
# class Server:
#     def __init__(self, hostname: str):
#         self.hostname = hostname

# ####
# server = Server("web-1")
# print(server.hostname)

# ####
# class Server:
#     def restart(self):
#         print("Restarting...")

# ####
# server.restart()


####
class Server:
    def __init__(self, hostname, cpu, mem):
        self.hostname = hostname
        self.cpu = cpu
        self.mem = mem

    def Restart(self):
        print("Restarting... {}".format(self.hostname))

    def IsOverload(self):
        if self.cpu >= 80:
            return(True)
        else:
            return(False)

    def Utilization(self):
        print(f"CPU: {self.cpu}% | Memory: {self.mem}%")

    def UpdateCPU(self, new_cpu):
        try: 
            if self.cpu < 0 or self.cpu > 100:
                self.cpu = new_cpu
                raise ValueError("Invalid CPU Value")
        except ValueError as e:
            print(e)
            print("CPU Updated to {}%".format(self.cpu))


server1 = Server("web-1", 90, 80)
server2 = Server("web-2", 80, 55)
server3 = Server("web-3", 110, 104)

print("Server 1: Host is {} and CPU Usage is {}".format(server1.hostname, server1.cpu))
print("Server 2: Host is {} and CPU Usage is {}".format(server2.hostname, server2.cpu))

server1.Restart()
server2.Restart()

servers = [server1, server2, server3]

for server in servers:
    if server.IsOverload():
        print(server.hostname)

server1.Utilization()

server3.UpdateCPU(20)
server2.UpdateCPU(-10)


class Cluster:
    def __init__(self, servers):
        self.servers = servers
        
    def RunningServers(self):
        count = 0
        for server in self.servers:
            print(server.cpu)
            if server.cpu <= 80:
                count += 1
        print(count)

    def AverageCPU(self):
        total_cpu = 0
        for server in self.servers:
            total_cpu += server.cpu
        print(total_cpu / len(self.servers))
        

cluster = Cluster([server1, server2, server3])
cluster.RunningServers()
cluster.AverageCPU()
