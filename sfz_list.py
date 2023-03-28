import itertools
# 遍历的 x 的范围
x_range = range(10)
# 生成所有排列
permutations = itertools.product(x_range, repeat=3)
# 筛选最后一个 x 是奇数的排列
filtered_permutations = [p for p in permutations if p[-1] % 2 == 1]
# 输出结果
count = 1
for p in filtered_permutations:
    print("37048119980619"+"".join([str(x) if i != len(p) - 1 else str(x) + "0" for i, x in enumerate(p)]))
    count = count+1

print(count)