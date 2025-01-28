# Get user's first name
your_name = input("What is your name? ")

# Get user's surname
your_surname = input("What is your surname? ")

# Convert the first letter of each word to uppercase and the rest to lowercase
# This is done using the title() method
your_name = your_name.title()
your_surname = your_surname.title()

# Print a personalized greeting message
print ("Hello " + your_name + " " + your_surname + "!")
print("you name has " + str(len(your_name)) + " characters")