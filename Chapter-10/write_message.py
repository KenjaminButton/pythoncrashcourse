filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I enjoy creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love analyzing data.\n")
    file_object.write("I love creating webapps.\n")
