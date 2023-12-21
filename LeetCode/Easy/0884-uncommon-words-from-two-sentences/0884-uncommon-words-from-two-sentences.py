class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        d1=dict()
        d2=dict()
        s1=s1.split()
        s2=s2.split()
        uncommon=[]
        
        for i in range(len(s1)):
            d1[s1[i]]=d1.get(s1[i],0)+1
        for i in range(len(s2)):
            d2[s2[i]]=d2.get(s2[i],0)+1
        
        for i,j in d1.items():
            if j==1:
                if i not in d2:
                    uncommon.append(i)
        for i,j in d2.items():
            if j==1:
                if i not in d1:
                    uncommon.append(i)
        
        return uncommon