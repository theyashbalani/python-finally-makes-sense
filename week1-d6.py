# with open("file/server.txt", "w") as file:
#     content = file.write("Hello Canonical")

# with open("file/server.txt", "r") as file:
#    content = file.read()
#    print(content)

# ####
# with open("file/server.txt", "a") as file:
#     content = file.write("\nWelcome to SRE")

# with open("file/server.txt", "r") as file:
#     for line in file.readlines():
#         print(line.strip())

# ####

# def count_lines(filename):
#     with open(filename, "r") as file:
#         count = 0
#         for line in file:
#             count += 1
#         print("Number of lines in a file: {}".format(count))

# count_lines("file/server.txt")

# def count_words(filename):
#     with open(filename, "r") as file:
#         count = 0
#         for line in file:
#             count += len(line.split())
#         print("Number of words in a file: {}".format(count))

# count_words("file/server.txt")

####

# Create a list to temporarily store our filtered production lines
prod_lines = []

# Open both the source and destination files at the same time
with open("file/server.txt", "r") as infile, open("file/newserver.txt", "w") as outfile:
    # Open the file and read the content
    print(type(infile.read()))
    text = infile.readlines()
    print(type(text))
    # Immediately write the line to the new file (copies everything)
    for line in text:
        outfile.write(line)

# 3. Read and display the newly created file
with open("file/newserver.txt", "r") as file:
    print("\n" + file.read())

#####

with open("file/log.txt", "r") as file:
    count = 0
    for line in file:
        line = line.split(" ")
        if "ERROR" in line:
            count += 1
    print("Number of errors: ", count)

####
def unique_servers_from_file(filename):
    unique_server = []
    with open("file/demo.txt", "r") as file:
        for line in file:
            if line.strip() not in unique_server:
                unique_server.append(line.strip())
    print(unique_server)

unique_servers_from_file("file/demo.txt")

# ####
# with open("file/server.txt", "a") as file:
#     file.write("\nAdded at the end")

# with open("file/server.txt", "r") as file:
#     content = file.read()
#     print(content)

# try:
#     with open("file/servers.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("File not found")
