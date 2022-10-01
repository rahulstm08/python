def printPascal(height):
    onevalue = [1]
    zero = [0]
    for i in range(height):
        print(*onevalue)
        onevalue = [left+right for left,
                    right in zip(onevalue+zero, zero+onevalue)]


# given height
height = 5
# passing the height as paramter to printPascal function
printPascal(height)
