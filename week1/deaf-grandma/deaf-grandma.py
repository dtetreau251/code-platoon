
words = input("Talk to grandma: ")

def speak(words):
    if words == "":
        print("WHAT?!")
        words = input("Talk to grandma: ")
        speak(words)
    elif words == "GOODBYE!":
        goodbye = input("LEAVING SO SOON? ")
        if goodbye == "GOODBYE!":
            print("LATER, SKATER!")
        else:
            words = input("Talk to grandma: ")
            speak(words)
    elif words == words.upper():
        print("NO, NOT SINCE 1946!")
        words = input("Talk to grandma: ")
        speak(words)
    elif words != words.upper():
        print("SPEAK UP, KID!")
        speak(input("Talk to grandma: "))

speak(words)