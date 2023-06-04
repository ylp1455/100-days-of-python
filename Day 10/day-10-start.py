# Function with outputs

def format_name(firstname, lastname):
    if firstname == "" or lastname == "":
        return
    
    fname = firstname.title()
    lname = lastname.title()

    return f"{fname} {lname}"


print(format_name(input("What is your first name? "), input("Enter your last name: ")))
