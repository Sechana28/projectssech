print("Hello , Welcome to Hotel Paradise")
print("One of your family member is a owner of this Big Hotel , after he died he left this hotel to you")
print("Now as you visit the hotel ,do you want to enter the dining hall or DJ hall?")

answer = input(">")

if(answer == "dining hall"):
    print("you enter the dining hall , and you see a robot protecting money.")
    print("Do you want to steal the money from the robot?")

    robotanswer = input(">")

    if(robotanswer == "yes"):
        print("You attempt to steal the money , but as you touch it harms u with an electric shock")
        print("You are now dead.:(")
    elif(robotanswer == "no"):
        print("You decide not to steal the money.")
    else:
        print("Invalid choice. Please enter yes or no")
elif(answer == "DJ hall"):
    print("As you enter the DJ hall , you see a cupboard ")
    print("Do you want to open the cupboard?")

    cupboardanswer = input(">")

    if(cupboardanswer == "yes"):
        print("You open the cupboard and see a dead body!")
        print("do you want to inform the issue to the police?")

        policeanswer = input(">")

        if(policeanswer == "yes"):
            print("Great , You helped the police to catch the criminal.")
        elif(policeanswer == "no"):
            print("Oh no! , the culprit was right there and you are helpless now.")
    elif(cupboardanswer == "no"):
        print("You made a firm decision not to open the cupboard")
        print("As you turn to leave , you hear a cracking sound ")
        print("Now you feel uncomfortable , and slowly open your eyes....  You wake up in your bed.it was all a DREAM")
    else:
        print("Invalid choice. please enter yes or no.")
else:
    print("Invalid choice.Please enter dining hall or DJ hall.")