def prefixTable(pat):
    m = len(pat)
    table = [0]*m
    i = 1
    j=0
    while(i<m):
        if(pat[i] == pat[j]):
            j += 1
            table[i] = j
            i += 1
           
        else:
            if j != 0:
                j = table[j -1]  
            else:
                table[i] = 0
                i += 1
    print(table)       
                
pat = "ababd"
prefixTable(pat)
