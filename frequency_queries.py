"""
You are given  queries. Each query is of the form two integers described below:
- 1 x: Insert x in your data structure.
- 2 y : Delete one occurence of y from your data structure, if present.
- 3 z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.
The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element. For example, you are given array . The results of each operation are:
Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1
Return an array with the output: [0, 1]
"""

def freqQuery(queries):

    ds = {}

    bool_dict = {
        True: 1,
        False: 0
    }

    output = []

    for i,j in queries:
        if i == 1:
            if ds.get(j, None):
                    ds[j] = ds.get(j)+1
            else:
                ds[j] = 1

        if i == 2:
            if ds.get(j, None):
                if ds.get(j) == 1:
                    ds.pop(j)
                else:
                    ds[j] = ds.get(j)-1
        if i == 3:
            output.append( bool_dict[j in ds.values()] )

    return output
