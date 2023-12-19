class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s1=s2=0
        nums=[]
        nums2.append(0)
        while s1<=m and s2<=n:
            if s1==m:
                nums.append(nums2[s2])
                s2+=1
            elif s2==n:
                nums.append(nums1[s1])
                s1+=1
            elif nums1[s1]<nums2[s2]:
                nums.append(nums1[s1])
                s1+=1
            elif nums1[s1]>nums2[s2]:
                nums.append(nums2[s2])
                s2+=1
            else:
                nums.append(nums1[s1])
                s1+=1
                nums.append(nums2[s2])
                s2+=1
        nums.pop()
        nums1[:] = nums