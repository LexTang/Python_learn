memo = {}
def L(nums, cur):
    if cur in memo:
        return memo[cur]
    if cur == len(nums) - 1:
        return 1
    max_len = 1
    for j in range(cur + 1, len(nums)):
        if nums[j] > nums[cur]:
            max_len = max(max_len, L(nums, j) + 1)

    memo[cur] = max_len
    return max_len


def length_lis(nums):
    return max(
        L(nums, i) for i in range(len(nums))
    )


nums = [1, 5, 2, 4, 3]
print(memo)
print(length_lis(nums))