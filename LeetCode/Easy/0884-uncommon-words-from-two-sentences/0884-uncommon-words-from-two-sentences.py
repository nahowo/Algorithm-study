class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        d=dict()
        s1=s1.split()
        s2=s2.split()
        uncommon=[]
        
        for i in range(len(s1)):
            d[s1[i]]=d.get(s1[i],0)+1
        for i in range(len(s2)):
            d[s2[i]]=d.get(s2[i],0)+1
        
        for i,j in d.items():
            if j==1:
                uncommon.append(i)
        
        return uncommon