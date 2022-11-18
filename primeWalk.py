def getPrimes(n):
    primes=[]
    for i in range(1,n+1):
        prime=True
        for j in primes[1:]:
            if(i%j==0):
                prime=False
                break
        if(prime):
            primes.append(i)
    return primes


def getFactors(n,primes):
    if n in primes:
        return 1
    for i in primes[1:]:
        if(n%i==0):
            return 1+getFactors(n/i,primes)
    

n=100000
primes=getPrimes(n)
pos=0
positions=[]
for i in range(1,n+1):
    # print("i={}, getFac={}".format(i,getFactorsEve(i,primes)))
    pos+=getFactors(i,primes)%2*-2+1
    positions.append(pos)
print(pos)
import matplotlib.pyplot as plt
plt.plot(positions)
plt.show()