import random 

with open("text_file.txt", "w") as fp:
    for _ in range(5):
        fp.write(f"Numéro de cette ligne : {random.randint(1,2)}\n")