def getRow(rowIndex: int):
    row = [1]
    for jj in range(rowIndex):
        crr = row[0]
        for ii in range(jj):
            nxt = row[ii+1]
            row[ii+1] = crr + row[ii+1]
            crr = nxt 
        row.append(1)
        print(row,jj)
    return row
