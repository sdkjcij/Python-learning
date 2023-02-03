# for迴圈

# for 變數 in 字串&列表
#   要執行的事

for letter in "小白你好":
    print(letter)

for num in [1, 2, 3, 4, 5]:
    print(num)

for num in range(5):
    print(num)

# range(2,7)
# =[2,3,4,5,6]


def power(base_num, pow_num):
    result = base_num 
    for index in range(pow_num-1):
        result = result*base_num
    return result


print(power(2, 6))
