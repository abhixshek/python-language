import argparse


def printer(metric):
    print(metric)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("metric") # this is a positional argument. positional arguments cannot be optional.
    parser.add_argument("alpha", default=0.2) # setting default parameter has no effect on positional arguments, since this argument has to be passed in the CLI. there is no way it can be skipped.
    parser.add_argument("--plot", "-p", default="line", required=True) # any --name or -name is an optional argument but here the required parameter makes this one required/compulsory
    parser.add_argument("-c", default="r") # optional. if not passed it will take the default value, which is "r"
    parser.add_argument("-s", action="store_true") # optional. if passed it gets the value True, otherwise it stays False

    args = parser.parse_args()
    
    print(args)
    # run python arg_parsing2.py -h to see the usage of all arguments

