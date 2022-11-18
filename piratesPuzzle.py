def getPaths(n, guesses):
    def helper(start, guess):
        # print(start)
        # print(guess)
        if(len(guess)==0):
            return False

        g=guess[0]
        if(start==0):
            return g==start or helper(1,guess[1:])
        elif(start==n-1):
            return g==start or helper(n-2,guess[1:])
        else:
            return (g==start or helper(start+1,guess[1:])) and (g==start or helper(start-1,guess[1:]))

    for i in range(n):
        if not helper(i,guesses):
            return False
    return True

print(getPaths(5, [1,2,3,4,1,1,2,3,4]))
