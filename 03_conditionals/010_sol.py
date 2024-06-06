# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

def recommend_pet_food(species, age):
    if species.lower() == 'dog':
        if age < 1:
            return "Puppy food"
        elif age < 7:
            return "Adult dog food"
        else:
            return "Senior dog food"
    elif species.lower() == 'cat':
        if age < 1:
            return "Kitten food"
        elif age < 7:
            return "Adult cat food"
        else:
            return "Senior cat food"
    else:
        return "Sorry, we do not have a recommendation for that species."

# Example usage:
pet_species = input("Enter the species of your pet (dog/cat): ")
pet_age = int(input("Enter the age of your pet in years: "))

recommended_food = recommend_pet_food(pet_species, pet_age)
print("Recommended food for your", pet_species, "is:", recommended_food)
