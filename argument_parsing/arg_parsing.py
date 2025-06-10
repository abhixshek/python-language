import argparse


def calculator(operation, operand_1, operand_2):
    if operation == 'sum':
        return operand_1 + operand_2
    elif operation == 'subtract':
        return operand_1 - operand_2
    elif operation == 'multiply':
        return operand_1 * operand_2
    elif operation == 'divide':
        return operand_1 / operand_2
    else:
        return None


print("starting the script.")
parser = argparse.ArgumentParser()
parser.add_argument("op", help="specify the binary operation to perform")
parser.add_argument("num_1", help="first number", type=int) # type=int runs int() on the string input argument and then saves it into arg.num_1
parser.add_argument("num_2", help="second number", type=int)

# optional arguments
parser.add_argument("--verbose", help="increase verbosity", type=int, choices=[0,1,2]) # choice restricts the values the --verbose option can take

parser.add_argument("-f", "--float", help="treat operands as float", action="store_true") # action="store_true" essentially converts this into a flag. if this is passed it will be true otherwise false.
# NOTE that if you specify only the shortversion, for example "-f" in the above agg_arguments() then the attribute will be args.f. but if you provide both then the attribute will take the name of -- flag.
# i.e. args.float

args = parser.parse_args()

print(args)
print(type(args))
print(args.op)
print(type(args.op)) # arguments passed as all strings by default

print(args.num_1, type(args.num_1)) # int, because we passed the kwarg type=int
print(args.num_2, type(args.num_2))


if args.verbose: # args.verbose takes the value passed after --verbose. and because its an optional arg, not passing --verbose means args.verbose takes the value None
    # and therefore this if block will not be run.
    print(args.verbose, type(args.verbose)) 

if args.float:
    print("converting operands to float")
    args.num_1 = float(args.num_1)
    args.num_2 = float(args.num_2)
    print(type(args.num_1))
    print(type(args.num_2))


result = calculator(args.op, args.num_1, args.num_2)

if args.verbose == 2:
    print("The {} of {} and {} is {}.".format(args.op, args.num_1, args.num_2, result))

elif args.verbose == 1:
    print("{} of {} and {} = {}".format(args.op, args.num_1, args.num_2, result))
else:
    print(result)

