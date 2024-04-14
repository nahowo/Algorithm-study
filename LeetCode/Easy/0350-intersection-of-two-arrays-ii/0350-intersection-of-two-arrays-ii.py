class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer=[]
        d1=dict()
        d2=dict()
        
        for i in nums1:
            d1[i]=d1.get(i,0)+1
            
        for i in nums2:
            d2[i]=d2.get(i,0)+1
            
        for k,v in d1.items():
            if k in d2:
                j=min(v,d2[k])
                answer.extend([k]*j)
            
        return answer