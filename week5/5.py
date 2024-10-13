import numpy as np
import random
import pandas as pd

class Person:
    def __init__(self):
        self.recover_prob = 0.2
        self.die_prob = 0.05
        self.init_sick_prob = 0.1
        self.infect_others_prob = 0.05
        self.vaccinated = False
        self.recovered = False
        self.dead = False
        self.sick = False
        self.average_meetups = 10
        self.days_sick = 0
        self.init_sick_or_not()
        
    def init_sick_or_not(self):
        prob = random.random()
        if prob <= self.init_sick_prob:
            self.sick = True
        else:
            self.sick = False
    
    def day_passes(self, population, init_scenario):
        if self.sick:
            self.days_sick += 1
            if not init_scenario:
                self.infect_others(population)
        
        prob = random.random()
        if prob <= self.recover_prob and self.sick:
            self.sick = False
            self.recovered = True 
        
        prob = random.random()
        if prob <= self.die_prob and self.sick:
            self.dead = True
            self.sick = False
            
    def infect_others(self, population):
        person_encounters = random.sample(range(population.size), self.average_meetups)
        for person_id in person_encounters:
            prob = random.random()
            person = population[person_id]
            if prob <= self.infect_others_prob and not (person.dead or person.recovered or person.vaccinated):
                population[person_id].sick = True  

class Village:
    def __init__(self, init_population_size):
        self.population = np.empty(init_population_size, Person)
        self.init_vaccination = 0.2 * init_population_size
        self.daily_vaccination_threshold = 0.04 * init_population_size
        self.vaccination_started = False
        self.generate_inhabitants()
        
    def advance_days(self, init_scenario=False):
        people_sick = 0
        people_recovered = 0
        people_dead = 0
        people_vaccinated = 0     
        people_immune = 0
        
        for person in self.population:
            if person.sick:
                people_sick += 1
            if person.dead:
                people_dead += 1
            if person.recovered and person.vaccinated:
                people_recovered += 1
                people_vaccinated += 1
                people_immune += 1
            elif person.vaccinated:
                people_vaccinated += 1
                people_immune += 1
            elif person.recovered:
                people_recovered += 1 
                people_immune += 1
            
            person.day_passes(self.population, init_scenario)
        
        people_susceptible = self.population.size - (people_immune + people_dead + people_sick)
        
        if people_sick >= self.init_vaccination and not self.vaccination_started:
            print(f"Vaccination has started! At the end of the day {people_sick} are sick and the community is on the alert")
            self.vaccination_started = True
            
        if self.vaccination_started:
            self.vaccinate_population()
            
        return people_sick, people_recovered, people_dead, people_vaccinated, people_immune, people_susceptible
    
    def generate_inhabitants(self):
        for i in range(self.population.size):
            self.population[i] = Person()
            
    def vaccinate_population(self):
        people_vaccinated_today = 0
        
        for person in self.population:
            if people_vaccinated_today == self.daily_vaccination_threshold:
                break
            elif not (person.sick or person.dead or person.vaccinated):
                person.vaccinated = True
                people_vaccinated_today += 1
    
    def start_simulation(self):
        current_day = 0
        day_data_list = []
    
        people_sick, people_recovered, people_dead, people_vaccinated, people_immune, people_susceptible = self.advance_days(init_scenario=True)
        day_data = [people_sick, people_recovered, people_dead, people_vaccinated, people_immune, people_susceptible]
        day_data_list.append(day_data)
        
        while people_sick != 0:
            print(f"By day {current_day} {people_sick} people are sick, {people_recovered} has recovered and {people_dead} are dead.")
            current_day += 1
            
            people_sick, people_recovered, people_dead, people_vaccinated, people_immune, people_susceptible = self.advance_days()
            day_data = [people_sick, people_recovered, people_dead, people_vaccinated, people_immune, people_susceptible]
            day_data_list.append(day_data)
        
        day_data_array = np.array(day_data_list)
        self.gen_df_and_save(day_data_array)
        
        days_sick = [person.days_sick for person in self.population]
        
        print("\n-------END OF SIMULATION-------")
        print(f"By day {current_day} {people_sick} people are sick, {people_recovered} has recovered and {people_dead} are dead.")
        print(f"In total {people_vaccinated} people received vaccination and {people_susceptible} remain susceptible to the virus.")
        print("--------------")
        print("The village has recovered and the virus is eliminated!")
        print("The longest time an individual was sick is: ", max(days_sick), "days")
        print(day_data_array)
    
    def gen_df_and_save(self, day_data_array):
        columns = ["Sick", "Recovered", "Deceased", "Vaccinated", "Immune", "Susceptible"]
        df = pd.DataFrame(day_data_array, columns=columns)
        print(df.head())  # Display first few rows as a preview
        df.to_csv("my_ass5_dataset.csv", index=False)

def main():
    pop_size = 1000
    village = Village(pop_size)
    village.start_simulation()

main()
