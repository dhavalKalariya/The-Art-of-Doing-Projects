#Dictionaries

bob_info ={
    "first_name":"Bob",
    "last_name":"Jones",
    "age":27,
    "fav_colors": ["green","orange"],
    }

print(bob_info)
print(type(bob_info))

print(bob_info["age"])
print(bob_info["fav_colors"][0])

bob_info["weight"] = 180
bob_info["Height"] = 72.6
print(bob_info)

bob_info["weight"] -= 5
print("Wow "+bob_info["first_name"]+", you lost some weight. You now weigh "+str(bob_info["weight"])+"!")

bob_info["age"] += 1
print("Happy Birthday "+bob_info["first_name"]+"! YOu are now "+str(bob_info["age"])+" years old!")

del bob_info["fav_colors"]
print(bob_info)

user_info = {}
user_info["name"] = input("What is your name: ").title()
user_info["age"] = input("What is your age: ")
user_info["Job"] = input("What is your job: ").title()
print(user_info)