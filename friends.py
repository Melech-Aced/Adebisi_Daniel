range(1,101)





for r in range(1,101):
    


    if r % 15 == 0:
        print(r,"fizz-buzz")
    elif r % 3 == 0:
        print(r,"fizz")
    elif r % 5 == 0:
        print(r,"buzz")
    else:
        print(r)
