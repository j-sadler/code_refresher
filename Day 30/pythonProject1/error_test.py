# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# except KeyError as error_message:
#     print(f"Key {error_message} doesn't exist")
# else:
#     content = file.read()
# finally:
#     raise TypeError("hahaha no code for you")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("check height")
bmi = weight/height **2
print(bmi)
