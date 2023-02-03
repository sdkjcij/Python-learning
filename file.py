# 檔案讀取與寫入

# open("檔案位置", mode="開啟模式")
# 絕對位置 e.g: C:/Users/user/Desktop/python.txt
# 相對位置 以程式位置作延伸 python.txt

# mode="r" 讀取
# mode="w" 覆寫
# mode="a" 原先資料後寫東西

# file = open("python.txt", mode="r",encoding="編碼方式")
# print(file.read())

# for line in file :
#   print(line)


file = open("python.txt", mode="a", encoding="utf-8")
file.write("讚")
file.close()

with open("python.txt", mode="a", encoding="utf-8") as file:
    file.write("\n哈哈哈哈哈")
