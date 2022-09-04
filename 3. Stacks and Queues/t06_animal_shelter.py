import time


#### ANIMALS #### #### ANIMALS #### #### ANIMALS #### #### ANIMALS #### #### ANIMALS #### #### ANIMALS ####


class Animal:
    def __init__(self, name):
        self.name = name
        self.time = time.time()


class Dog(Animal):
    pass


class Cat(Animal):
    pass


###########################################################################################################

class Shelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal):
        self.cats.append(animal) if isinstance(animal, Cat) else self.dogs.append(animal)

    def dequeue_any(self):
        return self.cats.pop(-1) if self.cats[-1].time < self.dogs[-1].time else self.dogs.pop(-1)

    def dequeue_cat(self):
        return self.cats.pop(-1)

    def dequeue_dog(self):
        return self.dogs.pop(-1)


animal_shelter = Shelter()
animal_shelter.enqueue(Cat("1"))
animal_shelter.enqueue(Cat("2"))
animal_shelter.enqueue(Dog("1"))
animal_shelter.enqueue(Dog("2"))
animal_shelter.enqueue(Dog("3"))
animal_shelter.enqueue(Dog("4"))
animal_shelter.enqueue(Cat("3"))
animal_shelter.enqueue(Cat("4"))
print(animal_shelter.dequeue_any().name)
print(animal_shelter.dequeue_cat().name)
print(animal_shelter.dequeue_dog().name)
