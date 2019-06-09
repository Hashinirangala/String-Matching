def search(pat, txt,out_f):
    M = len(pat)
    N = len(txt)
    c = 0
# A loop to slide pat[] one by one */
    if(N !=0 and M !=0 ):
        for i in range(0,(N - M +1)):
            # For current index i, check
            # for pattern match */
            for j in range(0,M):
                if ((txt[i + j] != pat[j]) and (pat[j] != "_")):
                    break
            if ((j == M-1) and ((txt[i + j] == pat[j]) or (pat[j] =="_"))):
                c += 1
                f = open(out_f, "a+")
                f.write("A pattern found at position "+str(i)+"\n")

    if (c == 0):
        f = open(out_f, "a+")
        f.write("Pattern is not found  \n")



n = int(input("Enter no  of pairs -: "))
for j in range(1, n+1):
    text_f = "text" + str(j) + ".txt"
    pat_f = "pat" + str(j) + ".txt"
    out_f = "out" + str(j) + ".txt"
    text = open(text_f, "r").read()
    pat = open(pat_f, "r").read()
    search(pat, text, out_f)



