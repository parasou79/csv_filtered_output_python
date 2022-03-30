#sp = '=><#[]~*$^!'
sp = ['<=','>=','!=','==','=','<','>','#','[',']','~','*','$','^','!']
def fSplit(qn,pos):
	if type(qn) == type('') or len(qn)==0 or pos == len(sp):
		return qn
	y = sp[pos]
	ans = []
	for idx, x in enumerate(qn):
		tmp = x.split(y)
		if len(tmp) > 1 and tmp[0]!='' and tmp[1]!='' and tmp[0] not in sp and tmp[1] not in sp:
			ans.append([tmp[0], y, tmp[1]])
		else:
			ans.append([x])
	ans = sum(ans,[])
#	print("\tSplitFor ", y, ans)
	return [ *fSplit(ans,pos+1) ]

qns = ['1^A,2$B,3=-6,4#C,5>9',  '2^10/6/2011', 'Code>=9', '9>=','>=9']
for qn in qns:
	print(qn)
	ans = fSplit(qn.split(','),0)
	print(ans)
