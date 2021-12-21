# string concatenation which means putting the strings together
# suppose we want to create a string that says subscribe to ________"

youtuber = "programmer" #some string variable

# a few ways to do this
print("subscribe to " + youtuber)
print("subscribe to {}" .format(youtuber))
print(f"subscribe to {youtuber}")

# concatinating the string using the f string
# First creating the variable for storing the f string and then creating
# variable for thing which needs to changed periodically
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famousPerson = input("Famous Person: ")

madlibstr = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famousPerson}!"
print(madlibstr)