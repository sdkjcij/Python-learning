# 類別class,物件object

class phone:
    def __init__(self, os, model, is_waterproof):
        self.os = os
        self.model = model
        self.is_waterproof = is_waterproof


samsung_A8s = phone("android10", "SM-G887F/DS", False)


print(samsung_A8s.model)
