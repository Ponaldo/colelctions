def jug():
    letterdict = {
        '1': ['a', 'b', 'p' , 'r'],
        '2': ['c', 'd', 'q', 's']
    }

    for x in letterdict['1']:
        for y in letterdict['2']:
            print(x + y)


