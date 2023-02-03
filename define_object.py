# 物件函式
class phone:
    def __init__(self, os, model, is_waterproof):
        self.os = os
        self.model = model
        self.is_waterproof = is_waterproof

    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False

    @staticmethod
    def add_to(number1, number2):
        return number1 + number2


samsung_A8s = phone("android10", "SM-G887F/DS", False)
Iphone_13 = phone("ios15.1", 123, True)

print(samsung_A8s.model)
print(samsung_A8s.add_to(5, 6))
