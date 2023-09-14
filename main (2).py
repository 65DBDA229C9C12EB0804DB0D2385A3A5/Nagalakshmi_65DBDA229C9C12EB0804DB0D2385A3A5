'''Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.'''
#Define the base class player
class player:
  def play(self):
      print("the player is playing cricket.")
#Define the derived class Batsman is
class Batsman(player):
  def play(self):
      print("the Batsman is batting.")
#Define the derived class Bowler
class Bowler(player):
  def play(self):
      print("the Bowler is bowling.")
#create objecs of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()
#call the play() method for each object
batsman.play()
bowler.play()


