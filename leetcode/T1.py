def two(nums, target):
    a = [0, 0]
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                a[0] = i
                a[1] = j
                return a


if __name__ == '__main__':
    lis = [2, 7, 11, 15]
    x = 9
    print(two(lis, x))
