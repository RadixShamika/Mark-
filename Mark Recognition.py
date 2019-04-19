d=open ("std_marks.txt","w")
i = int(input("Enter Index No :- "))
while (i !=0):
	n = input("Enter Name :- ")
	m1 = int(input("Enter Mark 1 :- "))
	m2 = int(input("Enter Mark 2 :- "))
	m3 = int(input("Enter Mark 3 :- "))
	T = m1+m2+m3
	A = T/3
data= "Index_No:- "+str(i)+", Name:- "+str(n)+", Total:- "+str(T)+", Avarage:-"+srt(A)+"\n"
	d.write(data)
	print(Done...!)
	i = int(input(Enter Index No : - "))
d.close()