# ask user for value type (time /distance / mass)
def get_conversion_type():
    while True:
        response = input("conversion type: ").lower()

        # check for exit code
        if response == "xxx":
            return response

        # check if its time
        elif response in ['time']:
            return "time"

        # check if its distance
        elif response in ['dist', 'distnace']:
            return "distance"

        # check if its mass
        elif response in ['mass']:
            return "mass"


# MAin routine goes here
while True:
    conversion_type = get_conversion_type()

    print (f"you chose {conversion_type}")

    if conversion_type == "xxx":
        break