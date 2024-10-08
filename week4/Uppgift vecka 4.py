import numpy as np
import random

class Person:
    def __init__(self):
        self.recover_prob = 0.2   
        self.die_prob = 0.05      
        self.init_sick_prob = 0.1  
        self.recovered = False
        self.dead = False
        self.sick = False
        
        self.init_sick_or_not()
        
    def init_sick_or_not(self):
        """When created each person starts as either sick or healthy"""
        prob = random.random()
        if prob <= self.init_sick_prob:
            self.sick = True  
            self.sick = False
    
    def day_passes(self):
        """Describes what happens to each person each day"""
        if self.sick:
            if random.random() <= self.recover_prob:
                self.sick = False
                self.recovered = True
        if self.sick:
            if random.random() <= self.die_prob:
                self.dead = True
                self.sick = False  


class Village:
    def __init__(self, init_population_size):
        self.population = np.empty(init_population_size, dtype=object)  
        self.generate_inhabitants()
    
    def generate_inhabitants(self):
        """Generates the population"""
        for i in range(len(self.population)):
            self.population[i] = Person()
        
    def advance_days(self):
        """Counts the status of the citizens in the community"""
        people_sick = 0
        people_recovered = 0
        people_dead = 0

        for person in self.population:
            if person.sick:
                people_sick += 1
            elif person.recovered:
                people_recovered += 1
            elif person.dead:
                people_dead += 1
            
            person.day_passes()  

        return people_sick, people_recovered, people_dead
    
    def start_simulation(self):
        """Controls the simulation and what happens in a day"""
        current_day = 0
        
        people_sick, people_recovered, people_dead = self.advance_days()
        while people_sick > 0:  
            print(f"By day {current_day} {people_sick} people are sick, {people_dead} are dead and {people_recovered} has recovered")
            current_day += 1
            people_sick, people_recovered, people_dead = self.advance_days()
        
        people_unaffected = len(self.population) - (people_sick + people_recovered + people_dead)
        print(f"\nBy day {current_day} {people_sick} people are sick, {people_dead} are dead and {people_recovered} has recovered. {people_unaffected} people were never in contact with the virus.")
        print("The village has recovered and the virus is eliminated!")


def main():
    pop_size = 1000  
    village = Village(pop_size)
    village.start_simulation()

main()
