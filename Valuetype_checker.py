# ask users for value type (Time /distance / Mass)
def get_valuetype():
    while True:
        response = input("Unit type: ").lower()

        # check for exit code
        if response == "xxx":
            return response

        # check if its seconds
        elif response in ["s", "sec", "second", "seconds"]:
            return "seconds"

        # check if it minutes
        elif response in ["m", "min", "minute", "minutes"]:
            return "minutes"

        # check if it hours
        elif response in ["h", "hr", "hour", "hours"]:
            return "hours"

        # check if its millimeters
        elif response in ["millimeters", "mm", "milimeters"]:
            return "millimeters"

        # check if its centimeters
        elif response in ["centimeters", "cm", "centi"]:
            return "centimeters"

        # check if it meters
        elif response in ["meters", "m", "meter"]:
            return "meters"

        # check if its kilometers
        elif response in ["km", "kilo", "kilometers", "kilometer" ]:
            return "kilometers"
            
        # if response is invalid output an error
        else:
            print ("please enter a valid file type")


# Main routine goes here
while True:
    value_type = get_valuetype()

    print(f"you chose {value_type}")

    if value_type == "xxx":
        break
