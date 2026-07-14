

###
for i in range(1,11):
    print(i)

###
servers = ["web", "db", "cache", "worker"]

for server in servers:
    print(server)

###
num = [5,10,15,20]
sum = 0
for i in num:
    sum += i
print(sum)

####
def average(numbers):
    total = 0
    for i in numbers:
        total += int(i)
    return total / len(numbers)

num = [5,10,15,20]
print (average(num))

################
cpus = [45, 81, 92, 73, 99]
total = 0
for cpu in cpus:
    if cpu > 80:
        total += 1
print("Number of CPUs with more than 80% Load: {}".format(total))

def is_critical(cpu):
    if cpu > 90:
        print ("Critical")
    elif cpu > 75:
        print ("Warning")
    else:
        print ("Healthy")

for cpu in cpus:
    print(cpu)
    is_critical(cpu)

####

server = {
    "hostname": "prod-1",
    "cpu": 82,
    "memory": 71
}

for lft,rgt in server.items():
    print("{}\n{}".format(lft,rgt))


###
count = 10
while count > 0:
    print (count)
    count -= 1

###

pods = [
    "Running",
    "Pending",
    "Running",
    "CrashLoopBackOff",
    "Running"
]

is_running = 0
for pod in pods:
    if pod.lower() == "running":
        is_running += 1

print("Number of Running Pods: {}".format(is_running))

###

cpus = [40, 55, 92, 68, 97]

def find_high_cpu(cpus):
    high_cpu = []
    for cpu in cpus:
        if cpu > 80:
            high_cpu.append(cpu)
    return high_cpu

print(find_high_cpu(cpus))

# ###
# def square(num):
#     return num ** 2

# result = square(9)
# print (result)

# ###
# server = {
#     "cpu": 81,
#     "memory": 64
# }

# for left, right in server.items():
#     print(left, right)

# for left in server:
#     print(left, (server[left]))