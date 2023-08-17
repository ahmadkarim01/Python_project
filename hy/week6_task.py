#python function:
# Q 8.1

# def display_message():
#     print("In this chapter I learn the functions: How to call functions.")
# display_message()

#Q 8.2

# def favorite_book(name):
#    favorite_book = input(f"The name of my favorite book is {name}")

# favorite_book("Sucess Habits")

# Q 8.3
# def make_shirt = (length,height):
#     print(f"The length of of the shirt is{length} and the height of the shirt is {height}")
# make_shirt = ("length","height")


# Q 8.4
# def make_shirt(length="l", height="l"):
#     if length.lower() == "l" and height.lower() == "l":
#         print("i love python")
#     else:
#         print(f"the length is {length} and the height is {height} ")
# make_shirt("median", "large")
# make_shirt("l", "l")

#8.5
# def describe_city():
#     print("Gilgit is the city of Pakistan")
# describe_city()

# def describe_city(Islamabad,kpk,Karachi):
#     print(f"These are the cities of Pakistan:"{Isamabad,Kpk,Karachi})

# describe_city()

# Correct one
def describe_city(city = "Gilgit"):
    print(city + " is in Pakistan")
describe_city()

def describe_city(city = "Islamabad"):
    print(city + " is my city ")
describe_city("Dehli")
describe_city("Islamabad")
describe_city("Norway")
