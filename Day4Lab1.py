"""
Create 3 lists for names, hometown, and favorite foods.
Ask the user to pick a number. Based off that number the corresponding student will be picked from the list.
Output the chosen student name
Output the two other categories. Ask the user which category they would like to know more on
Once the user types in the correct category it will output the specific data within the list of that category

to validate user number:
if the number is within 1 snd the overall length of the list
else have a output saying "Invalid input. Enter a number within the range"

to validate category:
set category to the user input
if category in hometown and favorite food is correct. return the data value
else tell the user it is invalid and ask them to enter a valid input.
 """


names = ["Jay", "Tom", "Bob", "David"]
hometowns = ["Charlotte", "Detroit", "Chicago", "Kansas"]
favorite_foods = ["Pizza", "Burgers", "Pasta", "Ice Cream"]

# Validate user number
def validate_user_number():
    while True:
        try:
            user_number = int(input("Enter a student number (1 to 4): ".format(len(names))))
            if 1 <= user_number <= len(names):
                return user_number
            else:
                print("Invalid input. Please enter a number between 1 and 4.".format(len(names)))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Validate category
def validate_category():
    while True:
        category = input("Which category to display (Hometown or Favorite Food): ").title()
        if category in ["Hometown", "Favorite Food"]:
            return category
        else:
            print("Invalid category. Please enter either 'Hometown' or 'Favorite Food'.")

while True:
    # Prompt the user to ask about a particular student
    user_number = validate_user_number()

    # Use the user number as the index for the lists
    student_index = user_number - 1
    student_name = names[student_index]

    print("\nInformation for student {}: {}".format(user_number, student_name))

    # Ask the user which category to display
    chosen_category = validate_category()

    # Display the relevant information
    if chosen_category == "Hometown":
        print("Hometown: {}".format(hometowns[student_index]))
    elif chosen_category == "Favorite Food":
        print("Favorite Food: {}".format(favorite_foods[student_index]))

    # Ask the user if they would like to learn about another student
    another_student = input("Do you want to learn about another student? (yes/no): ").lower()
    if another_student != 'yes':
        break