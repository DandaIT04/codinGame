class Solution(object):
    def sortDict(self,n,t):
        d = {}

        for count,value in enumerate(n):
            d[n[count]] = t[count]

        d = dict(sorted(d.items()))    
        e = list(d.values())
        f = ""
        
        for count1,value1 in enumerate(e):
            f += e[count1]

        print(f)

#n = list(str(15243))
#t = list("enaet")

n = list(str(input()))
t = list(input())

runSolution = Solution()

runSolution.sortDict(n,t)
