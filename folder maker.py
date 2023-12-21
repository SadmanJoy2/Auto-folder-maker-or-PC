import os

os.mkdir("NewFolder")
for i in range(0,50):
    os.mkdir(f"NewFolder/Folder{i+1}")

print("50 folders made successfully")
input("Press Enter key to exit")

