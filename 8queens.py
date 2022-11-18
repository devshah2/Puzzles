counts=0
def nextQueen(n, rows, cols, diag, positions):
    ans=[]
    # global counts
    # counts+=1
    # if(counts%10000==0):
    #     # print()
    #     print("n={}, rows={}, cols={}, diag={}, positions={} \n\n".format(n,rows,cols,diag,positions))
    if(n==0):
        return positions
    for ii in range(len(rows)):
        for jj in range(len(cols)):
            i=rows[ii]
            j=cols[jj]
            da=i+j
            db=i+(8-j)+1
            if(not da in diag[0] or not db in diag[1]):
                continue
            d1=diag[0].index(da)
            d2=diag[1].index(db)
            # if(d1==)
            res=nextQueen(n-1,rows[:ii]+rows[ii+1:],cols[:jj]+cols[jj+1:],[diag[0][:d1]+diag[0][d1+1:],diag[1][:d2]+diag[1][d2+1:]],positions+[[i,j]])
            if(res!=[]):
                # return res
                return res
                # ans.
    return []

rows=[1,2,3,4,5,6,7,8]
cols=[1,2,3,4,5,6,7,8]
diag=[[x for x in range(2,17)],[x for x in range(2,17)]]
lets=["A","B","C","D","E","F","G","H"]
# print(nextQueen(8,rows,cols,diag,[]))
inp=input("Enter 1st position (A4, B8, etc): ")
a=lets.index(inp[0])+1
b=int(inp[1])
rows.remove(a)
cols.remove(b)
diag[0].remove(a+b)
diag[1].remove(a+(8-b)+1)
# print(rows)
# print(cols)
# print(diag)
out=nextQueen(7,rows,cols,diag,[[a,b]])
print(out)
# print("{}{}".format("B",2),end=", ")
for i in out:
    print("{}{}".format(lets[i[0]-1],i[1]),end=", ")