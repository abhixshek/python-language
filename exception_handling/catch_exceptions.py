def fetcher(object, index):
    return object[index]


if __name__ == "__main__":
    s = 'king'
    print(s)
    try:
        print(fetcher(s, 4))
    except IndexError: # catch and recover
        print('exception encountered')

    try:
        print(fetcher(s, 3)) # try block ran successfully this time
    except IndexError: # catch and recover
        print('exception encountered')


    # raising exceptions
    try:
        raise IndexError
    except IndexError:
        print('caught "raised" IndexError just like any other error that is raised automatically by Python')

