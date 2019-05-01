"""
    optimize the naive approach
    recursively dfs all the possibilities and avoid duplicate paths by using a hashtable

    e.g. 2, -1, 3, -1
    sort it such that nums = -1, -1, 2, 3

    compute permutations of - 1(index 0)
    skip computation for index 1 becos - 1(index 0) has been considered
    compute permutations of 2(index 2)
    compute permutations of 3(index 3)

    time      O(n!) worst case
    space	    O(n!)
    beats     46.47%
"""


class Solution(object):

    def __init__(self):
        self.result = []

    def permuteUnique(self, nums):
        nums = sorted(nums)
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, prefix):
        if len(nums) == 0:
            self.result.append(prefix)
        visited = {}
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited[nums[i]] = True
            self.dfs(nums[:i] + nums[i+1:], prefix + [nums[i]])


"""
    optimize the naive approach
    recursively dfs all the possibilities and avoid duplicate paths by using a hashtable

    e.g. 2, -1, 3, -1
    sort it such that nums = -1, -1, 2, 3

    compute permutations of - 1(index 0)
    skip computation for index 1 becos - 1(index 0) has been considered
    compute permutations of 2(index 2)
    compute permutations of 3(index 3)

    time      O(n!) worst case
    space	    O(n!)
    44 ms, faster than 96.93%
"""


class Solution(object):

    def __init__(self):
        self.result = []

    def permuteUnique(self, nums):
        nums = sorted(nums)
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, prefix):
        if len(nums) == 0:
            self.result.append(prefix)
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                self.dfs(nums[:i] + nums[i+1:], prefix + [nums[i]])


# print(Solution().permuteUnique([1, 1, 2]))

"""
    iterative insertion using a hashtable to avoid duplicate result
    1
    ^ ^
    2 2

    2,1         1,2
    ^ ^ ^       ^ ^ ^
    3 3 3       3 3 3
    beats 29.92%
"""


def permuteUnique(nums):
    nums = sorted(nums)
    perms = [[]]
    seen = {}
    for num in nums:  # for each number
        new_perms = []
        for perm in perms:  # for each temporary result
            for i in range(len(perm)+1):  # for each slot
                temp = perm[:i] + [num] + perm[i:]
                key = str(temp)
                if key in seen:
                    continue
                seen[key] = True
                new_perms.append(temp)
        perms = new_perms
    return perms


# print(permuteUnique([1, 1]))
# print(permuteUnique([1, 1, 2]))

# suggested solution is kinda confusing
# put it here for study
# beats 99.91%

def permuteUnique1(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    perms = [[]]
    for num in nums:  # for each number
        new_perms = []
        for perm in perms:  # for each temporary result
            for i in range(len(perm)+1):  # for each slot
                new_perms.append(perm[:i]+[num]+perm[i:])
                # if the current number equals to the digit(at i) of current perm(not the new_perm), break
                if i < len(perm) and perm[i] == num:
                    break
        perms = new_perms
    return perms


print(permuteUnique1([1, 1, 2]))
