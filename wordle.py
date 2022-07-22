app.stepsPerSecond = 1
def onStep():
    holder.timer += 1
   # print(pythonRound(timer[0]))

#border
Rect(0, 0, 400, 400, fill='white', border='grey')


#boxes (do not change for the most part)
Grid = Group()
for i in range(1,7):
    for j in range(1,6):
        Grid.add(Rect(25 + 50 * j, 25 + 50 * i, 50, 50, fill = 'white', border = 'lightGray'))
        
        
#title
title = Label('WORDLE', 200, 40, font='monospace', size = 60)



holder = Circle(-10,-10,1) #this is just to hold all of the global variables
holder.x = 100
holder.y = 100

#holder.lastLabel = Label('', 0, 0)
holder.my_Objects = []
holder.turnCounter = 0
holder.greenCounter = 0


holder.gameWin = False #currently unused
holder.gameLose = False #currently unused

#TODO: import dictionary of words or manually add a lot of 5 letter words
wordList = ['VALUE', 'STUDY','TABLE', 'COURT', 'DEATH', 'PARTY', 'CHILD', 'MONEY', 'NIGHT', 'CLASS', 'HEART', 'MATCH', 'TEAMS', 'SATYA', 'IDIOT', 'HUMOR', 'MICRO', 'TOUGH', 'TEACH', 'TRAIN', 'SPANK', 'BOOTY', 'BROOM', 'WORDS', 'SATYR', 'PARTS', 'RINGS', 'HANGS', 'DRAWS']
holder.word = wordList[randrange(0, len(wordList))]
#print(holder.word)
#holder.word = 'VALUE' # <--remove this line, currently just testing with the world "value"


holder.wordSet = set() #allows us to check if a character from holder.inputWord is contained in holder.word in O(1)
for y in holder.word:
    holder.wordSet.add(y)
holder.inputWord = ''

'''youWin = Group(Rect(100, 100, 200, 250, fill = 'ghostWhite'),
        Label('You Win!', 200, 125, size = 30),
        Label('Number of Tries', 200, 155, size = 20))
'''

slayList = ['INSPIRATION', 'GENIUS', 'MASTERMIND', 'EXPERT']
holder.slay = slayList[randrange(0, len(slayList))]

youWin = Group(Rect(100, 100, 200, 250, fill = 'ghostWhite', border='lightGrey'),
    Label('Statistics', 200, 125, size = 15),
    Label('Number of Tries', 200, 155, size = 20),
    Label("You're such a...", 200, 250, size = 15),
    Label(holder.slay, 200, 275, size = 18, bold=True)
    )
        

youWin.opacity = 0


suckList = ['DISAPPOINTMENT', 'FAILURE', 'LOSER', 'DISGRACE']
holder.suck = suckList[randrange(0, len(suckList))]

youLose = Group(Rect(100, 100, 200, 250, fill = 'lightCoral'),
        Label('You Lose!', 200, 125, size = 30),
        Label('Number of Tries', 200, 155, size = 20),
        Label("You're such a...", 200, 250, size = 15),
        Label(holder.suck, 200, 275, size = 18, bold=True)
        )
        
youLose.opacity = 0

#TO-DO LIST

    #BUG - incorrectly labels letters yellow
        #ex. if word is VALUE, but user types 'PIECE', it would label the first E as yellow
        
    #TODO: figure out how to make the redsqaures disappear after half a second
    
    #TODO: add win game/lose game logic
    #TODO: add Label at the top displaying used letters

redSquares = Group()

holder.timer = 0  

        
def fadeRedSquares(time):
    holder.timer = 0
    #initialTime = holder.timer
    while(holder.timer < time and redSquares.opacity > 10):
        redSquares.opacity -= 10
        
        print(holder.timer)
        print(time)
    
    print('clear')
    redSquares.clear()
        
    
    

#this code implements enter feature - only goes to next line if the user hits 'enter'
def onKeyPress(key):
    redSquares.clear()
    
    if len(key) == 1 or key == 'enter': #what's the point of the if len(key) == 1
        print(key) #TEST
        holder.greenCounter = 0
        if key == 'enter':
            if holder.x == 350: #press enter to input the guess (only when all five letters are present)
                holder.y += 50
                holder.x = 100
            
                for x in holder.my_Objects:
                    holder.inputWord = holder.inputWord + x.value
    
                for z in range(0, len(holder.word)):
                    if holder.word[z] == holder.inputWord[z]:
                        Rect(75 + z * 50, 75 + holder.turnCounter * 50, 50, 50, fill = 'green', opacity = 50)
                        holder.greenCounter += 1
                    elif holder.inputWord[z] in holder.wordSet:
                        Rect(75 + z * 50, 75 + holder.turnCounter * 50, 50, 50, fill = 'gold', opacity = 50)
                    else:
                        Rect(75 + z * 50, 75 + holder.turnCounter * 50, 50, 50, fill = 'grey', opacity = 50)
                holder.turnCounter += 1
                holder.my_Objects = []
                holder.inputWord = ''
                
                if(holder.greenCounter == 5):
                    print('won the game')
                    youWin.opacity = 100
                    youWin.toFront()
                    youWin.add(Label(holder.turnCounter, 200, 185, size = 40))
                    
                if(holder.turnCounter == 6 and not holder.greenCounter== 5):
                    youLose.opacity = 100
                    youLose.toFront()
                    youLose.add(Label(holder.turnCounter, 200, 185, size = 40))
                    youLose.add(Label(holder.word, 200, 325, size = 15))
                    
            else: #red box appears around empty squares for half a second

#WORKING HERE 
            #TODO how do you make it disappear after half a second?
                tempXPos = holder.x
                #redSquares = Group()
                
                for x in range(5 - int((holder.x - 100) / 50)):
                    square = Rect(tempXPos - 25, holder.y -25, 50, 50, fill='red', opacity = 20)
                    redSquares.add(square)
                    tempXPos += 50
                    #print('building squares')
                
                #wait half a second
                #fadeRedSquares(10)
                #redSquares.clear()
                
                
                
            
            
        elif key.isalpha() and (not key == 'enter') and holder.x < 350: #regularly add the letters
            
            key = key.upper()
            label = Label(key, holder.x, holder.y, size=18, font='monospace', bold=True)
            holder.my_Objects.append(label)
            Grid.add(label)
            #if not holder.x == 350: #changed from 300 to 350
            holder.x += 50
                
            print(holder.x) # TEST
                
            
    elif key == 'backspace' and not holder.x == 100:
        holder.inputWord = ''
        tempLabel = (holder.my_Objects[-1])
        Grid.remove(tempLabel)
        holder.my_Objects.pop(-1)
        holder.x -= 50
        
        
      
  
        





#ERIC'S ORIGINAL CODE (w/o enter features and other small features)
'''
def onKeyPress(key):
    if len(key) == 1 and key.isalpha():   
        key = key.upper()
        label = Label(key, holder.x, holder.y, size=18, font='monospace', bold=True)
        holder.my_Objects.append(label)
        Grid.add(label)
        if not holder.x == 300:
            holder.x += 50
        else :
            holder.y += 50
            holder.x = 100
        
            for x in holder.my_Objects:
                holder.inputWord = holder.inputWord + x.value

            for z in range(0, len(holder.word)):
                if holder.word[z] == holder.inputWord[z]:
                    Rect(75 + z * 50, 75 + holder.turnCounter * 50, 50, 50, fill = 'green', opacity = 50)
                elif holder.inputWord[z] in holder.wordSet:
                    Rect(75 + z * 50, 75 + holder.turnCounter * 50, 50, 50, fill = 'gold', opacity = 50)
                else:
                    Rect(75 + z * 50, 75 + holder.turnCounter * 50, 50, 50, fill = 'grey', opacity = 50)
            holder.turnCounter += 1
            holder.my_Objects = []
            holder.inputWord = ''
    elif key == 'backspace' and not holder.x == 100:
        holder.inputWord = ''
        tempLabel = (holder.my_Objects[-1])
        Grid.remove(tempLabel)
        holder.my_Objects.pop(-1)
        holder.x -= 50
        
'''




'''

#i don't think we should use this stuff down here
def onStep():
    
    
    #loseScreen
    #if(holder.turnCounter == 6 and holder.gameOver = false):
    
    
    
    
    
    #winScreen
    if(holder.gameWin == True):
        Label("Congrats Discoverer!!!", 200, 45, size=10, bold=True)
        
        #do the spinny thingy with the correct word if we have time
    
   # if(gameLo)
    
        
        
'''
