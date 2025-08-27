class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def info(self):
        return f"{self.brand} {self.model}"

class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage
    def call(self, number):
        print(f"{self.info()} is calling {number}... ")
    def take_photo(self):
        print(f"{self.info()} takes a photo ")

if __name__ == "__main__":  # 👈 quick demo
    phone1 = Smartphone("Huawei", "huawei p30 lite", "android", "256GB")
    phone2 = Smartphone("Samsung", "Galaxy S24", "android", "512GB")
    phone1.call("727434767")
    phone2.take_photo()
    phone2.call("123456789")    
