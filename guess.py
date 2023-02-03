import random
guess_number = int(random.uniform(1, 100))
Guess = None
Guess_count = 0
guess_limit = 10
out_of_limit = False

while Guess != guess_number and not out_of_limit:
    Guess_count += 1
    
    if Guess_count > 10:
        out_of_limit = True
        break
    if Guess_count <= guess_limit:
        Guess = int(input("請猜個數字:"))
        if Guess > guess_number:
            print("小一點")
        if Guess < guess_number:
            print("再大一點")
    

if out_of_limit is True:
    print("菜雞幫QQ")
else:
    print("你猜對了!!!")
