class Solution:      
    def plusOne(self, digits: List[int]) -> List[int]:
        strint=str(int(''.join(map(str,digits)))+1)
        digits=list(map(int,list(strint)))
        return digits