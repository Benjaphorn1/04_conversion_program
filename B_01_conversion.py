# generate heading
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# display instructions
def instructions():
    statement_generator(statement="Conversion program", decoration="-")

    print('''To use this program please enter the
    type of conversion you would like to do (time,
     distance or mass) Then enter the number 
    and unit that you want to convert and then the
     unit you would like to convert too.
     
     To exit the program, please type xxx''')


# ask for the correct integer over 0 (whole number)
def num_check(question):
    error = "please enter a number over 0"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for the number
            response = int(response)

            # check that the number is over 0
            if response > 0:
                return response
            else:
                print("please enter a number that is more zero")

        except ValueError:
            print(error)


# ask users for their sort of conversion (distance/ time / volume / xxx)
def get_conversiontype():
    while True:
        response = input("Conversion Type: ").lower()

        # check if its exit code
        if response == "xxx":
            return response

        # check if its time
        elif response in ['time']:
            return "time"

        # check if its distance
        elif response in ['distance', 'dist']:
            return "distance"

        # check if its mass
        elif response in ['mass']:
            return "mass"

        # if response is invalid output an error
        else:
            print("please enter a valid file type")


# Distance conversion code
def distance_conv():
    distance_dict = {
        "mm": 1000,
        "cm": 100,
        "m": 1,
        "km": .001
    }

    # Get amount and units (assume they are valid)
    amount = float(input("how much? "))
    from_unit = input("from unit? ")
    to_unit = input("To Unit? ")

    # Multiply to get our standard value...
    multiply_by = distance_dict[to_unit]
    standard = amount * multiply_by

    # Divide to get the value
    divide_by = distance_dict[from_unit]
    total = standard / divide_by

    # look up value
    multiply_by = distance_dict[to_unit]

    answer = f"There are {total} {to_unit} in {amount} {from_unit}"

    return answer


# Time conversion code
def time_conv():
    time_dict = {
        "seconds": 3600,
        "second": 3600,
        "sec": 3600,
        "s": 3600,
        "minutes": 60,
        "min": 60,
        "m": 60,
        "hours": 1,
        "hrs": 1,
        "hr":1,
        "h": 1,
    }

    # Get amount and units (assume they are valid)
    amount = float(input("how much? "))
    from_unit = input("from unit? ")
    to_unit = input("To Unit? ")

    # Multiply to get our standard value...
    multiply_by = time_dict[to_unit]
    standard = amount * multiply_by

    # Divide to get the value
    divide_by = time_dict[from_unit]
    answer_time = standard / divide_by

    # look up value
    multiply_by = time_dict[to_unit]

    answer = f"There are {answer_time} {to_unit} in {amount} {from_unit}"

    return answer


def mass_conv():
    mass_dict = {
        "mg": 1000000,
        "milligram": 1000000,
        "grams": 1000,
        "g": 1000,
        "gs": 1000,
        "kilograms": 1,
        "kg": 1,
        "kgs": 1,
    }

    # get amount and unit (assume they are valid)
    amount = float(input("how much? "))
    from_unit = input("from unit? ")
    to_unit = input("To unit? ")

    # Multiply to get our standard value
    multiply_by = mass_dict[to_unit]
    standard = amount * multiply_by

    # divide to get the value
    divide_by = mass_dict[from_unit]
    answer_mass = standard / divide_by

    # look up value
    multiply_by = mass_dict[to_unit]

    answer = f"There are {answer_mass} {to_unit} in {amount} {from_unit}"

    return answer


# main routine goes here

# display headings
statement_generator(statement="Conversion program", decoration="-")

# Display instructions if requested
want_instructions = input("press <enter> to read the instructions "
                          "or an key to continue")

if want_instructions == "":
    instructions()

# Output answer from conversion type
while True:

    # ask user what they want to convert to / from
    conversiontype = get_conversiontype()

    # exit if user types exit code
    if conversiontype == "xxx":
        break

    # do conversion and output result

    if conversiontype == "distance":
        distance_ans = distance_conv()
        print(distance_ans)

    elif conversiontype == "time":
        time_conv_ans = time_conv()
        print(time_conv_ans)

    elif conversiontype == "mass":
        mass_conv_ans = mass_conv()
        print(mass_conv_ans)

print()
print("Thank you for using the conversions program!")
