# 二維迴圈,巢狀迴圈

nums = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
]


print(nums[2][2])

# row 行
# col 欄

for row in nums:
    for col in row:
        print(col)
