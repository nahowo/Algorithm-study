class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l=10**4
        arr=[0]*((l*2)+1)
        for i in nums:
            arr[i+l]+=1 # 음수 인덱스 바이어스 처리
            
        for i in range(len(arr)-1,-1,-1):
            k-=arr[i]
            if k<=0:
                return i-l