# Here are all of my conditional tests. Warning, there are a lot.
 # I have made comments above the various sections to make skimming easier.

# Let's start with some numbers!
print("IS 12*2 equal to 24? I predict true.")
print(12 * 2 == 24)
print("Does 35+2 not equal 37? I predict false.")
print(35 + 2 != 37) 
print("Is 12/2 < 10? I predict true.")
print(12/2 < 10)
print("IS 54 % 5 > 32? I predict false.")
print(54 % 5 > 32)
randomNumber = 6392 + 3607 
print("Is randomNumber <= 10,000? I predict true.")
print(randomNumber <= 10000) 
randomNumber2 = 3 * 100 
print("Is randomNumber2 <= 300? I predict true.")
print(randomNumber2 <= 300)
randomNumber3 = 11*7
print("Is randomNumber3 >= 123? I predict false.")
print(randomNumber3 >= 123)
randomNumber4 = 374
print("Does randomNumber4 == 666? I predict false.")
print(randomNumber4 == 666)

# Here are some word problems. 
myAge = 12+5
votingAge = 9 * 2
print("Am I able to vote? Does myAge = votingAge? I predict false")
print(myAge >= votingAge)
seniorDiscount = 5 * 13
JeffAge = 9 ** 2
katherineAge = 44 + 10
print("At store X, you can recieve a senior discount if you are 65 or older.")
print("Is Jeff able to recieve a senior discount? I predict true.")
print(JeffAge >= seniorDiscount)
print("IS Katherine able to recieve a senior discount? I predict false.")
print(katherineAge >= seniorDiscount) 
anakin = 16
padme = anakin + 5
print("The Republic is holding an election. \n Padme and Anakin both wish to vote, but they have a 5 year age difference, and you must be 18 to vote. \n If they both attempt to enter the voting area at the same time, they may get rejected.")
print("Anakin is 16. Can Anakin and Padme both vote in the Republic Election? I predict false.")
print(anakin >= 18 and padme >= 18)
anakin = 20
print("Four years have past. Now can both of them vote? I predict true.")
print(anakin >= 18 and padme >= 18)
jake = 1.5
jim = 5.25
jane = 2.
print("You must be 5 feet to go on ride x unless someone of the height requirements is with you. \n Three people wish to go. Jim, Jake, and Jane. \n However, Jane and Jake are children, meaning they are too short to go on their own.")
print("Can Jim and Jane go on the ride? I predict true.")
print(jim >= 5 or jane >= 5)
print("Can Jake and Jane go on the ride? I predict false.")
print(jake >= 5 or jane >= 5) 

"""Now, let's do some fun ones involving words, = and !=. I tried to incorperate some humor into this one."""
greenDay = "zzz"
print("September has ended, has anyone woken up Green Day? In other words, does greenDay == 'woken'? I predict false.")
print(greenDay == "woken")
python = "awesome"
print("Does python == 'awesome'? I predict true.")
print(python == "awesome")
elonMusk = 0
print("On a scale of 1-10, is Elon Musk's trustworthiness above 5? I predict false.")
print(elonMusk >= 5)
objectiveC = "unknown"
print("Does objectiveC != learned? I predict true.")
print(objectiveC != "learned")
giveYouUp = "never" 
print("Does giveYouUp != never? I predict false.")
print(giveYouUp != "never")
haveYouBeenRickrolled = "yes"
print("Does haveYouBeenRickrolled == yes? I predict true.")
print(haveYouBeenRickrolled == "yes")

# We've done numbers and words... Now what? Ah, yes, lists!
# Let's start by experimenting with capitalisation.
domesticAnimals = ["dog", "cat", "rabbit", "fish", "Hamster", "rat"]
print("Is 'rabbit' in list domesticAnimals? I predict true.")
print("rabbit" in domesticAnimals)
print("Is 'Rabbit' in the list domesticAnimals? I predict false.")
print("Rabbit" in domesticAnimals)
print("Does adding .lower() to Rabbit make it to the list? I predict true.")
print("Rabbit".lower() in domesticAnimals)
print("Does it have the same effect on Hamster? I predict false.")
print("hamster".lower() in domesticAnimals) 

# Great! Now for some practical examples!
print("Here is a database of users for program X, as well as banned users.")
users = ["john_smith", "notfound404", "no_clue122", "randomuser123"]
print("is official_karen on the list of users? I predict false.")
print("official_karen" in users)
print("IS no_clue122 in the list of users? I predict true.")
print("no_clue122" in users)
bannedUsers = ["darthvator666", "lord_voldemort", "official_karen", "stupid_troll", "troublemaker"]
print("Is sirius_black not on the list of banned users? I predict true.")
print("sirius_black" not in bannedUsers)
print("Is lord_voldemort not included in banned users? I predict false.")
print("lord_voldemort" not in bannedUsers)