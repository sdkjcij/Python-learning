# 列表,列表用法
scores = [90, 70, 80, 95, 60]
names = ["小黑", "小白", "小黃"]
things = [60, "python", "及格", True]
print(scores[0])

# 輸出指定字元OR資料
print(things[1:3])

# 與字串配合使用
phrase = "Hello World"
print(phrase[0:5])

# 改變列表中資料
scores[0] = 30
print(scores)

# 列表延伸
scores.extend(names)
print(scores)

# 列表增加
scores.append(50)
print(scores)

# 列表插入
names.insert(2, "小紅")
print(names)

# 列表刪除
scores.remove(60)
print(scores)

# 列表清除
scores = [90, 70, 80, 95, 60]
scores.clear()
print(scores)

# 列表移除最後一位
scores = [90, 70, 80, 95, 60]
scores.pop()
print(scores)

# 列表由小到大排列
scores = [90, 70, 80, 95, 60]
scores.sort()
print(scores)

# 列表反轉
scores.reverse()
print(scores)

# 列表中資料尋找
scores = [90, 70, 80, 95, 60]
print(scores.index(80))

# 列表中有幾個特定資料
scores = [90, 80, 80, 80, 60]
print(scores.count(80))

# 列表中有幾筆資料
scores = [90, 70, 80, 95, 60]
print(len(scores))
