# MicroRootAI - Smart Irrigation System  
# Uproszczony kod dla adaptacyjnego mikrodozowania wody  

class Plant:  
    def __init__(self, name, moisture_level):  
        self.name = name  
        self.moisture_level = moisture_level  

    def check_soil_moisture(self):  
        if self.moisture_level < 40:  
            return "Needs Water"  
        elif self.moisture_level > 70:  
            return "Overwatered"  
        else:  
            return "Optimal Hydration"  

# Przykładowe użycie  
plant1 = Plant("Tomato", 35)  
print(f"{plant1.name}: {plant1.check_soil_moisture()}")  
