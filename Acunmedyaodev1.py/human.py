class Human:
    name = "Mert"
    #built-in
    #constructor
    def __init__(self,name):
        self.name = name
        print("Bir Human Instance'i üretildi")  
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer: {self.name}"      
    def talk(self, senctence):
        name = "Barış"
        print(f"{self.name}: {senctence}")
        #print(f"{name}: {senctence}")
    def walk(self):
        print(f"{self.name} is Walking.")