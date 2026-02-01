class SuperHero:
    def introduce(self):
        print(f"I am {self.name} and my power is {self.power} !")

#create first superhero object 
hero1=SuperHero()
hero1.name="Spidermen"
hero1.power="Wall crawling"
#second superhero object
hero2=SuperHero()
hero2.name="Ehtehsam Anwar"
hero2.power="Mind Reader"

#call the function
hero1.introduce()
hero2.introduce()