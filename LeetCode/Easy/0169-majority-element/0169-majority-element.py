class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Majority Element는 항상 존재하기 때문에, 가장 높은 빈도수를 가지는 원소를 찾는 것과 동일하다. 
        
        current=nums[0]
        cnt=0
        
        for i in nums:
            if i==current: # 현재까지 가장 빈도수 높은 원소가 다시 등장한 경우
                cnt+=1 # 최대 빈도수 +1
            elif cnt==1: # 새로운 원소가 등장했는데 지금까지의 최대 빈도수가 1일 경우
                current=i # 새로운 원소로 current 업데이트
            else: # 새로운 원소가 등장했지만 지금까지의 최대 빈도수가 1보다 큰 경우
                cnt-=1 # 현재까지 가장 빈도수 높은 원소가 등장한 것이 아니므로 cnt 감소
        
        return current