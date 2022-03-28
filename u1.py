import csv
import sys

sp = ',=><#[]~*$^!'
def fSplit(qn,pos=0,arr=[]):
	if type([]) != type(qn):
		print("Qn: ", qn)
		fSplit([qn], pos,arr)
		print("Ans: ", arr)
		return arr

	for x in qn:
		if pos==len(sp):
			return arr
		spl = sp[pos]
		ans = x.split(spl)
		# print(spl, x, ans)
		if len(ans) == len(x):
			# for s in sp:
			# 	if qn(s) >= 0:
			# 		print(error, qn)
			arr.append( (int(qn[0]), qn[1],sp[pos-1]))
			return arr
		else:
			# print('split ', x, ' by ', spl, ans)
			fSplit(ans, pos+1, arr)

qns = ['1^A,2$B,3=-6,4#C,5>9', '2^10/6/2011']
for qn in qns:
	# fSplit(qn)
	pass
# exit(0)


# def check1(p,q,r):
# 	try:
# 		a = p.index(q)
# 		a = a + len(q)
# 		b = p.index(r,a)
# 		print(p[a:b])
# 	except:
# 		pass

# from pandas import read_csv

# df = read_csv(sys.argv[1])
# data = df.values
# print(data[:, [0,2]  ])


infile = sys.argv[1]
# filters = sys.argv[2].split(',')

if len(sys.argv) == 2:
	with open( infile ) as ina:
		inf = list(csv.reader(ina, delimiter=','))
		for x in inf[:10]:
			print(x)
	exit(0)

filters = fSplit(sys.argv[2])
# filters = sys.argv[2].split('=')
# filters[0] = int(filters[0])


fields = sys.argv[3] if len(sys.argv) > 3 else '0,1,2,3'
fields = [ int(x) for x in fields.split(',')] 
with open( infile ) as ina:
	inf = list(csv.reader(ina, delimiter=','))
	inl = len(inf)
	# sp = ',=><#[~]*$^'
	for x in inf:
		found = True
		for flt in filters:
			a,b,op = flt
			if found and op=='=':
				found = x[a] == b
			if found and op=='>':
				found = x[a] > b
			if found and op=='<':
				found = x[a] < b
			if found and op=='#':
				found = x[a] != b
			if found and op=='*':
				found = x[a].contains(b)
			if found and op=='^':
				found = x[a].startswith(b)
			if found and op=='$':
				found = x[a].endswith(b)
			if found and op==']':
				found = len(x[a]) > int(b)
			if found and op=='[':
				found = len(x[a]) < int(b)
			if found and op=='~':
				found = len(x[a]) == int(b)
			if found and op=='!':
				found = len(x[a]) != int(b)

		# if x[filters[0]] == filters[1]:
		if found:
			ans = [ x[f] for f in fields]
			print(ans)

