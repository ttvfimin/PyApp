class hangman:
  def titleScreen(words, asciiArt, HANGMANPICS):
    import time as t
    import random as r
    from colored import fg, bg
    import platform as p
    import os
    hangman.clear(p.system()) #Calls our clear function.
    asciiANum = r.randint(0,(len(asciiArt)-1)) #Chooses a random ascii art title screen
    asciiArt = asciiArt[asciiANum] #makes the title screen just one item

    print("%s :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" % (fg(116))) #fancy print
    try:
      print(asciiArt % (fg(206)))
    except Exception as e:
      print("HANGMAN")
    print("%s :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" % (fg(116))) # fancy print

    whatToDo = input("%s1) Start\n2) Credits\n3) Exit\n>" % (fg(85))) #menu code
    #Lines 20 - 39 - Not TOO efficent. Could use a switch statement.

    if whatToDo == "1":
      hangman.hangManStart(words, asciiArt, HANGMANPICS) #start the game
    elif whatToDo == "2":
      hangman.credits(words, asciiArt, HANGMANPICS) #print credits
    elif whatToDo == "3":
      return True # quits game
    elif whatToDo == "4":
      hangman.clear(p.system())
      print(hangman.clear("VersionCallback"))
      for art in ascii:
        print(art)
      for pic in HANGMANPICS:
        print(pic)
      t.sleep(10)
      hangman.titleScreen(words, ascii, HANGMANPICS)
      #debug code. doesnt really need to be fancy or anything.
    elif whatToDo == "5":
      print(words)
      t.sleep(7)
      hangman.titleScreen(words, ascii, HANGMANPICS)
    elif whatToDo == "6":
      hangman.wordSplitter()
      hangman.titleScreen(ascii)
    else:
      hangman.clear(p.system())
      print("Choose 1, 2 or 3 on the main menu.")
      t.sleep(3)
      hangman.titleScreen(ascii)
      #just catches anything other than menu items.

  def wordSplitter():
    words = open("wordsList.txt", "r")
    wordsL = ""
    temp = words.read().splitlines()
    for word in temp:
      wordsL = wordsL + word + " "
    file = open("wordsDone.txt", "w+")
    print(wordsL)
    file.write(wordsL)
    file.close()
    words.close()



  def hangManStart(words, ascii, HANGMANPICS):
    import platform as p
    import random as r
    hangman.clear(p.system())
    randomChoice = words[r.randint(0,len(words)-1)]
    hangman.hangManGuess(words, HANGMANPICS, randomChoice, ascii)
    
  def hangManGuess(words, HANGMANPICS, rChoice, ascii):
    import platform as p
    notToGuess = False
    numberWrong = 0
    word = list(rChoice)
    letters = []
    lettersTwo = []
    gameRunning = True
    guessArray = []
    wordUnedited = word.copy()
    
    print(wordUnedited)
    
    for letter in word:
      guessArray.append("_")

    while gameRunning == True:
      notToGuess = False

      for letter in guessArray:
        print(letter, end=" ")
      print()

      if len(word) == 0:
        hangman.gameWon(rChoice, ascii, HANGMANPICS, words)
        gameRunning = False

      print(HANGMANPICS[numberWrong])
      guess = input(">")
      hangman.clear(p.system())

      if guess.lower() == "whats the word":
        print(rChoice)
        notToGuess = True

      if guess in letters or guess in lettersTwo:
        print("Already guessed!")
        notToGuess = True
        for i in range(0, 25):
          try:
            word.remove(guess)
          except Exception:
            a = "lmao"

      if len(guess) >= 2 or len(guess) <= 0:
        print("Please type in one letter.")
        notToGuess = True

      if guess in rChoice and notToGuess == False:
        for i in range(0,25):
          try:
            arrayPiece = wordUnedited.index(guess)
            guessArray[arrayPiece] = guess
          except Exception as e:
            a = "lmao"
        for letter in letters:
          print(letter, end = " | ")
        lettersTwo.append(guess)
        for i in range(0,25):
          try:
              word.remove(guess)
          except Exception:
              a = "lmao"
              
      elif guess not in rChoice and notToGuess == False:
        for letter in letters:
          print(letter, end = " | ")
        print(guess)
        numberWrong += 1
        if numberWrong == 7:
          hangman.endGame(rChoice, words, ascii, HANGMANPICS)
          break
        letters.append(guess)





  def gameWon(word, ascii, HANGMANPICS, words):
    from colored import fg, bg
    print("%s " % (fg(208)))
    import platform as p
    hangman.clear(p.system())
    import time as t

    gameWonASCII = """
  ___  ___      .--.      ___  ___       ___  ___  ___     .--.      ___ .-.   
  (   )(   )    /    \    (   )(   )     (   )(   )(   )   /    \    (   )   \  
  | |  | |    |  .-. ;    | |  | |       | |  | |  | |   |  .-. ;    |  .-. .  
  | |  | |    | |  | |    | |  | |       | |  | |  | |   | |  | |    | |  | |  
  | '  | |    | |  | |    | |  | |       | |  | |  | |   | |  | |    | |  | |  
  '  `-' |    | |  | |    | |  | |       | |  | |  | |   | |  | |    | |  | |  
    `.__. |    | '  | |    | |  ; '       | |  ; '  | |   | '  | |    | |  | |  
    ___ | |    '  `-' /    ' `-'  /       ' `-'   `-' '   '  `-' /    | |  | |  
  (   )' |     `.__.'      '.__.'         '.__.'.__.'     `.__.'    (___)(___) 
    ; `-' '                                                                     
    .__.'                                                                      
                                                              
    """
    print(gameWonASCII)
    print("Well done! You guessed the word", word)
    t.sleep(6)
    hangman.titleScreen(words, ascii, HANGMANPICS)





  def endGame(word, words, ascii, HANGMANPICS):
    import platform as p
    import time as t
    gameOverASCII = """
    
  ______       ______       __    __       ______         ______       __   __    ______       ______    
  /\  ___\     /\  __ \     /\ "-./  \     /\  ___\       /\  __ \     /\ \ / /   /\  ___\     /\  == \   
  \ \ \__ \    \ \  __ \    \ \ \-./\ \    \ \  __\       \ \ \/\ \    \ \ \\'/    \ \  __\     \ \  __<   
  \ \_____\    \ \_\ \_\    \ \_\ \ \_\    \ \_____\      \ \_____\    \ \__|     \ \_____\    \ \_\ \_\ 
    \/_____/     \/_/\/_/     \/_/  \/_/     \/_____/       \/_____/     \/_/       \/_____/     \/_/ /_/ 
                                                                                                          

    """
    hangman.clear(p.system())
    from colored import fg, bg
    print("%s "  % (fg(160)))
    print(gameOverASCII)
    print("Your word was:", word)
    t.sleep(6)
    hangman.titleScreen(words, ascii, HANGMANPICS)

  def clear(v):
    import os
    import platform as p
    if v == "Windows":
      os.system("cls")
    elif v == "VersionCallback":
      v = p.system()
      if v == "Windows":
        word = "Version: " + v + "- therefore caling os.system('cls')"
      else:
        word = "Version: " + v + "- therefore caling os.system('clear')"
      return word
    else:
      os.system("clear")

  def credits(words, ascii, HANGMANPICS):
    import platform as p
    hangman.clear(p.system())
    nathan = """
                    _     _                     
                    | |   | |                    
    _ __     __ _  | |_  | |__     __ _   _ __  
    | '_ \   / _` | | __| | '_ \   / _` | | '_ \ 
    | | | | | (_| | | |_  | | | | | (_| | | | | |
    |_| |_|  \__,_|  \__| |_| |_|  \__,_| |_| |_| 
    """
    andAscii = """
    &
    """
    ben = """
    ,---.     ,---.    .-. .-.  
    | .-.\    | .-'    |  \| |  
    | |-' \   | `-.    |   | |  
    | |--. \  | .-'    | |\  |  
    | |`-' /  |  `--.  | | |)|  
    /( `--'   /( __.'  /(  (_)  
    (__)      (__)     (__) 
    """
    from colored import fg, bg
    print("%sa" % (fg(121)))
    hangman.clear(p.system())

    print("Credits: Made by: ", nathan, "\n", andAscii, "\n", ben, "\nBen: Github\\ttvfimin\nNathan: Repl.it\\G0ldC0ins123")
    
    import time as t
    t.sleep(5)
    hangman.clear(p.system())
    hangman.titleScreen(words, ascii, HANGMANPICS)

  def start():
    import os
    import time as t
    import random as r
    from colored import fg, bg
    import platform as p
    #START MAKING WORDS
    words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra chocolate computer science english welsh maths game gaming abruptly absurd abyss affix askew avenue awkward axiom azure bagpipes bandwagon banjo bayou beekeeper bikini blitz blizzard boggle bookworm boxcar boxful buckaroo buffalo buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt curacao cycle daiquiri dirndl disavow dizzying duplex dwarves embezzle equip espionage euouae exodus faking fishhook fixable fjord flapjack flopping fluffiness flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo giaour gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen iatrogenic icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk jazziest jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kitsch kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays numbskull nymph onyx ovary oxidize oxygen pajama peekaboo phlegm pixel pizazz pneumonia polka pshaw psyche puppy puzzling quartz queue quips quixotic quiz quizzes quorum razzmatazz rhubarb rhythm rickshaw schnapps scratch shiv snazzy sphinx spritz squawk staff strength strengths stretch stronghold stymied subway swivel syndrome thriftless thumbscrew topaz transcript transgress transplant triphthong twelfth twelfths unknown unworthy unzip uptown vaporize vixen vodka voodoo vortex voyeurism walkway waltz wave wavy waxy wellspring wheezy whiskey whizzing whomever wimpy witchcraft wizard woozy wristwatch wyvern xylophone yachtsman yippee yoked youthful yummy zephyr zigzag zigzagging zilch zipper zodiac zombie').split()

    #DEFINE ASCII ART ARRAY
    ascii = ["""%s             
    _   _    ___    _   _   _____  ___  ___   ___    _   _ 
    | | | |  / _ \  | \ | | |  __ \ |  \/  |  / _ \  | \ | |
    | |_| | / /_\ \ |  \| | | |  \/ | .  . | / /_\ \ |  \| |
    |  _  | |  _  | | . ` | | | __  | |\/| | |  _  | | . ` |
    | | | | | | | | | |\  | | |_\ \ | |  | | | | | | | |\  |
    \_| |_/ \_| |_/ \_| \_/  \____/ \_|  |_/ \_| |_/ \_| \_/


    """,
    """%s
      /_     __,      ,__,      __      ,____,     __,      ,__,
    _/ (_   (_/(_   _/ / (_   _(_/_   _/ / / (_   (_/(_   _/ / (_
                              _/_                              
                              (/
    ""","""%s                                   
    . .    .    . .  .-.  .  .    .    . .
    |-|   /_\   |\|  |-.  |\/|   /_\   |\|
    ' '  '   '  ' '  '-'  '  '  '   '  ' '"""]

    HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
    /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
    /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
    /|\  |
    /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
    /|\  |
    / \  |
          |
    =========''']
    hangman.titleScreen(words, ascii, HANGMANPICS)