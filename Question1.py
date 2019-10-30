
def search(pat, txt): 
    M = len(pat) 
    N = len(txt)
    c = 0
   m=4;
	list = []
    # A loop to slide pat[] one by one */ 
    for i in range(N - M + 1): 
		# For current index i, check 
		# for pattern match */ 
		for j in range (M):
            if ((txt[i + j] != pat[j]) and (pat[j]!="_")): 
				break
		if (j == M - 1):
			c += 1
			list.append(i)
			
    if(c == 0):
        print("no string matching")
	else:
		print(list)


n = int(input("Enter no  of pairs"))
for i in range (1,n):
	text_f = "text"+str(j)+".txt"
	pat_f = "pat"+str(j)+".txt"
	out_f = "out"+str(j)+".txt"

	text = open("text_f","r")
	pat = open("pat_f","r")
	search(pat,text)



