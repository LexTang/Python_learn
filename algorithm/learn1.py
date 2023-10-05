def sortSquare(nums):
    idx_l, idx_r, i = 0, len(nums)-1, len(nums)-1
    res = [0 for _ in range(len(nums))]
    while idx_l <= idx_r:
        if nums[idx_l] ** 2 < nums[idx_r] ** 2:
            res[i] = nums[idx_r] ** 2
            idx_r -= 1
        else:
            res[i] = nums[idx_l] ** 2
            idx_l += 1
        i -= 1
    return res


if __name__ == '__main__':
    a = [-3, -1, 0, 3, 6]
    print(sortSquare(a))