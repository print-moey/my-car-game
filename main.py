# Auto detect text files and perform LF normalization 

i = 0

def helper():
    print("""Commands:
Start = starts the car
Stop = stops the car
Quit = stops the game
Type on '>' to make commands""")

helper()
while i == 0:
       i = 1
       question = input(">").upper()
       if question == ("START"):
           command = ("START")
           print("Car has started..")
       if question == ("STOP"):
           command = ("STOP")
           print("Car has stopped..")
       if question == ("HELP"):
               helper()
       if question == ("QUIT"):
           exit()
       if question.upper() not in ["QUIT", "STOP", "START", "HELP"]:
           print("Uh-Oh..I dont recognise that..")
       i = 0 
