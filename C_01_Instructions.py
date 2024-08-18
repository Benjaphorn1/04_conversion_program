# generate headings (eg: -----Heading-----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator(statement="instructions", decoration="-")

    print('''To use this program please enter the
    type of conversion you would like to do (time,
     distance or mass) Then enter the number 
    and unit that you want to convert and then the
     unit you would like to convert too.
     
     To exit the program, please type xxx''')


# main routine goes here

# Display instructions if requested
want_instructions = input("press <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()

print()
print("program continues")