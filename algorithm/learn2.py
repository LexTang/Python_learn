# 阶乘
def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)


# 字符串倒序输出
def str_r(start, str):
    if start == len(str):
        return
    str_r(start + 1, str)
    print(str[start])


# 递归冒泡
def mao(size, str):
    if size == 0:
        return str
    for i in range(size):
        if str[i] > str[i + 1]:
            str[i], str[i + 1] = str[i + 1], str[i]
        # print(str, size)
    mao(size - 1, str)


# 斐波那契数列
cache = {0: 0, 1: 1}
def fei(idx):
    if idx in cache:
        return cache[idx]
    val = fei(idx-1)+fei(idx-2)
    cache[idx] = val
    return val


# 电话号码的字母组合
phn = {2:"abc",
       3:"def",
       4:"ghi",
       5:"jkl",
       6:"mno",
       7:"pqrs",
       8:"tuv",
       9:"wxyz"
       }
def let_cob(tmp_lis, nums, idx):
    if len(tmp_lis) == len(nums):
        lis.append(tmp_lis[:])
        return
    for i in phn[nums[idx]]:
        tmp_lis.append(i)
        let_cob(tmp_lis, nums, idx+1)
        tmp_lis.pop()


# 组合问题
lis = []
def zu(num, size, idx, lis_sit):
    if len(lis_sit) == size:
        # 创建一个新的列表，以避免将同一组合多次添加到结果中
        lis.append(lis_sit[:])
        return
    if num - idx + 1 < size - len(lis_sit):
        return
    for i in range(idx, num + 1):
        lis_sit.append(i)
        zu(num, size, i + 1, lis_sit)
        lis_sit.pop()


# 组合总和
def zu_sum(aim, size, idx, lis_sp):
    if sum(lis_sp) > aim:
        return
    if sum(lis_sp) == aim:
        lis.append(lis_sp[:])
        return
    for i in range(idx, 10):
        lis_sp.append(i)
        zu_sum(aim, size, i+1, lis_sp)
        lis_sp.pop()


# 组合总和39
def zu_sum1(cdit, aim, lis_tmp, idx):
    if sum(lis_tmp)>aim:
        return
    if sum(lis_tmp)==aim:
        lis.append(lis_tmp[:])
        return
    for i in range(idx, len(cdit)):
        lis_tmp.append(cdit[i])
        zu_sum1(cdit, aim, lis_tmp, i+1)
        lis_tmp.pop()


# 



if __name__ == '__main__':
    zu_sum2([10,1,2,7,6,1,5],8 , [], 0)
    print(lis)
