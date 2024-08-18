# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):
    error = "please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print("please enter a number that is more than zero")

        except ValueError:
            print(error)


# main routine goes here
for item in range(0, 2):
    amount = num_check("amount: ")


