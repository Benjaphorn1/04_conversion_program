# ask users for value type (Time /distance / Mass)
def get_valuetype():
    while True:
        response = input("Value type: ").lower()

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

        # if response is invalid output an error
        else:
            print("please enter a valid file type")


# Main routine goes here
while True:
    value_type = get_valuetype()

    print(f"you chose {value_type}")

    if value_type == "xxx":
        break
