file = open('youtube.txt', 'w')

# when things that need to be handle like communication with databases , try catch error handlng should be done
try:
    file.write("chai aur code")
finally:
    file.close()

# this with code does not need try catch finally error handling its done internally
# automatically the given mode is executed and close automatically not needed to explicitly mention it
with open("youtube.txt", "r") as file:
    print(file.read())