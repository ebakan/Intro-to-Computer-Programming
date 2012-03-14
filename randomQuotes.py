#lists-asg3
#ebakan
from random import randrange
class quoter:
     def __init__(self):
         self.quotes=[["When you have a fat friend there are no see-saws. Only catapults.",
                       "The easiest time to add insult to injury is when you're signing somebody's cast.",
                       "The worst time to have a heart attack is during a game of charades.",
                       "'Sort of' is such a harmless thing to say. Sort of. It's just a filler. Sort of - it doesn't really mean anything. But after certain things, sort of means everything. Like after 'I love you' or 'You're going to live' or 'It's a boy.'",
                       "A drunk driver is very dangerous. So is a drunk backseat driver if he's persuasive. 'Dude make a left.' 'Those are trees...' 'Trust me.'"],
                      ["Life is not measured by the number of breathes we take, but by the moments that take our breath away.",
                       "Don't be afraid that your life will end, be afraid that it will never begin.",
                       "The best way to make your dreams come true is to wake up.",
                       "There are hundreds of languages in the world, but a smile speaks them all.",
                       "To the world you might be one person, but to one person you might be the world."],
                      ["We make war that we may live in peace.",
                       "There never was a good war or a bad peace.",
                       "Everyone's a pacifist between wars. It's like being a vegetarian between meals.",
                       "If you want peace, prepare for war.",
                       "In peace the sons bury their fathers, but in war the fathers bury their sons."]]
         print("Welcome to the Random Quotation Program!")
         self.loop()
         inp=raw_input("Would you like to hear another quote about "+self.inp+"? (y/n)").lower()
         while True:
              if inp=='y':
                  print(self.repeat())
                  inp=raw_input("Would you like to hear another quote about "+self.inp+"? (y/n)").lower()
              elif inp=='n':
                   inp=raw_input("Would you like to hear a quote from a different category besides "+self.inp+"? (y/n)").lower()
                   if inp=='y':
                        self.loop()
                   elif inp=='n':
                       break
               
              else:
                  inp=raw_input("You must have entered something wrong. Would you like to hear another quote about "+self.inp+"? (y/n)").lower()

     def mood(self):
         self.inp=raw_input("Do you want to hear funny quotes, inspirational quotes, or quotes about war?").lower()
         while True:
             if self.inp=='funny':
                  self.moods=0
                  break
             elif self.inp=='inspirational':
                  self.moods=1
                  break
             elif self.inp=='war':
                  self.moods=2
                  break
             else:
                  self.inp=raw_input("You must have entered something wrong. Please select 'funny', 'inspirational', or 'war':").lower()

     def loop(self):
          self.mood()
          self.x=randrange(5)
          print(self.quotes[self.moods][self.x])

     def repeat(self):
          while True:
              y=randrange(5)
              if y!=self.x:
                  self.x=y
                  return self.quotes[self.moods][y]
                  break

if __name__=='__main__':
     q=quoter()
