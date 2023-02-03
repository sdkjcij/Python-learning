
def max_sum(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


def pow_num(base_num, power_num):
    pownum = pow(base_num, power_num)
    return pownum


print(pow_num(832874934, 48011))
