class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    def __init__(self,name,pet_type,owner=None):
        self.name=name
        
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not valid pet type")
        self.pet_type=pet_type

        if owner is not None and not isinstance(owner,Owner):
            raise Exception("owner must be an instance of Owner or None")
        self.owner=owner

        Pet.all.append(self)
        
class Owner:
    def __init__(self,name):
        self.name=name

    #returns a full list of the owner's pets.
    def pets(self):
        return [pet for pet in Pet.all if pet.owner==self]
    #that checks that the the pet is of type Pet and adds the owner to the pet.
    def add_pet(self, pet):
        if not isinstance(pet,Pet):
            raise Exception("add_pet expects an instance of Pet")
        pet.owner=self


    def get_sorted_pets(self):
        return sorted(self.pets(),key=lambda pet:pet.name)

