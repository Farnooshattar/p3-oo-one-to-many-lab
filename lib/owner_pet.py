class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner=owner
        if pet_type not in self.PET_TYPES:
            raise TypeError("pet type not valid")
        self.pet_type = pet_type
        Pet.all.append(self)
        

class Owner:
    def __init__(self,name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self, pet):
        if pet.pet_type not in Pet.PET_TYPES:
            raise TypeError("pet type not valid")
        pet.owner = self
    def get_sorted_pets(self):
        pet_collection=[pet for pet in Pet.all if pet.owner == self]
        pet_collection.sort(key=lambda pet: pet.name)
        return pet_collection