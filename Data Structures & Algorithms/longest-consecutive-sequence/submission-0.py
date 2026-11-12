class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        hsNums=set(nums)

        for n in nums:
            if n-1 not in hsNums:
                curLen=0
                curNum=n
                while curNum in hsNums:
                    curLen+=1
                    curNum+=1
                longest=max(curLen,longest)
        return longest
                    



        