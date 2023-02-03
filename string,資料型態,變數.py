# 基本資料型態&變數

# 1.字串
print("1")
print("Python")

# 數字
# -87
# 47
# 160.6666

# 布林值
# True
# False

name1 = "PYTHON"
name2 = "java"
age = 87
is_good = True

print("好用的程式語言是" + name1)
print(name1 + "是" + str(age) + "歲")
print(name1 + "都跟" + name2 + "配合")
print(name1 + "是否好用?")
print(is_good)
print(age*name1)

# 字串,字串用法

# 函式
print("2")
print(name1.lower())
print(name2.upper())
print(name1.islower())
print(name1.isupper())

# 同行內多個函式
print("3")
print(name1.isupper())

# 取得字元
print("4")
print(name1[0])
# 從0開始

# 尋找字元
print("5")
name1 = "python"
print(name1.index("p"))

# 替換字元
print("6")
print(name1.replace("p", "P"))
