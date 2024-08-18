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

print(f"There are {answer_mass} {to_unit} in {amount} {from_unit}")