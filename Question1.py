def search(pat, txt): 
    M = len(pat) 
    N = len(txt)
    c = 0
    list = []
    # A loop to slide pat[] one by one */ 
    for i in range(N - M + 1): 
        # For current index i, check 
            # for pattern match */ 
        for j in range(0, M):
            if ((txt[i + j] != pat[j]) and (pat[j]!="_")): 
                break
        if (j == M - 1):
            c += 1
            list.append(i)
                
    if(c==0):
        print("no matching")
        print('\n')
    else:
        print(list)
        print('\n')

f = open("test.txt", "r")
f1 = f.readlines()
k = 1
for x in f1:
	if(k%2 != 0):
		txt = x
		print("txt -: ",txt)
		k += 1
	else:
		pat = x
		print("pattern -: ",pat)
		k += 1
		search(pat,txt)
		
		
