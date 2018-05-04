## 015 3Sum
## Given an array S of n integers, are there elements 
## a, b, c in S such that a + b + c = 0? Find all unique 
## triplets in the array which gives the sum of zero.

"""
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
            return []
    nums.sort()
    res = set()
    for key, v1 in enumerate(nums[:-2]):
        if key >= 1 and v1 == nums[key-1]:
            continue
        d = dict()
        for v2 in nums[key+1:]:
            if v2 not in d:
                d[-v1-v2] = 1
            else:
                res.add((v1, -v1-v2, v2))
           
    return list(map(list, res))
                    

    return map(list, res)

s = [-1,0,1,2,-1,-4]
res = threeSum(s)
for item in res:
	print(item)