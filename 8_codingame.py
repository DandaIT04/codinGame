class Solution(object):
    def sortDict(self,n,t):
        d = {}

        countOnce = 0
        for count,value in enumerate(n):
            d[n[count]] = t[count]

        d = dict(sorted(d.items()))    

        print(d)

n = list(str(15243))
t = list("enaet")

#n = list(str(input()))
#t = list(input())

runSolution = Solution()

runSolution.sortDict(n,t)
