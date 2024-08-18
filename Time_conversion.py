
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

print(f"There are {answer_time} {to_unit} in {amount} {from_unit}")
