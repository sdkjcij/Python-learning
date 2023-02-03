# if判斷句

score = int(input())
if score == 100:
    print("我給你一千塊")
elif 100 > score >= 60:
    print("我給你五百塊")
else:
    print("我給你一百塊")

# if判斷

# and
# and not

# or
# or not


def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num2:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num2 and num3 > num1:
        return num3


print(max_num(3, 69, 70))
