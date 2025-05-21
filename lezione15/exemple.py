PATH: str = "lezione15/exemple.txt"
mode: str = "r"
encoding: str = "utf-8"


file = open(PATH)
output: str = file.read()
print(output)
file.close()

# file = open("lezione15/example.txt","a")
#try:
#     pass
# except Exception as e: 
#     pass
# finally:
#     file.close()
# lezione15/example.txt
