class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        s_dict=dict()
        t_dict=dict()
        for i in range(len(s)):
            s_dict[s[i]]=s_dict.get(s[i],0)+1
        for i in range(len(t)):
            t_dict[t[i]]=t_dict.get(t[i],0)+1

        for i,j in t_dict.items():
            if i not in s_dict:
                return False
            if s_dict.get(i)!=j:
                return False
        return True