# import required module

import os

print("")
print("")
print("")

print("\n	 (YOU CAN USE NUMBER OR YOU CAN DO CHAT LIKE 'OPEN NOTEBOOK' etc....)")
print("BE AWARE THAT THIS CANNOT OPEN SOME APPS DUE TO THE OPERATING SYSTEM YOUR ON. ")
print("\n ============================================ Welcome To My Tools ============================================")
print("Welcome to my tools")
print("")
print("")

print("chat with me with your requirements")

while True:
    # take input
    print(" CHAT WITH ME WITH YOUR REQUIREMENTS -open-: ", end='')
    p = input("")
    p = p.upper()
    print(p)

    if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
        print("Type Again")
        print(".")
        print(".")
        continue

    # assignments for different applications in the menu
    elif ("GOOGLE" in p) or ("SEARCH" in p) or ("WEB BROWSER" in p) or ("CHROME" in p) or ("BROWSER" in p) or ("4" in p):
        print("Opening")
        print("GOOGLE CHROME")
        print(".")
        print(".")
        os.system("chrome")

    elif ("IE" in p) or ("MSEDGE" in p) or ("EDGE" in p) or ("8" in p):
        print("Opening")
        print("MICROSOFT EDGE")
        print(".")
        print(".")
        os.system("msedge")

    elif ("FF" in p) or ("FFOX" in p) or ("MOZZILA" in p) or ("FIREFOX" in p):
        print("Opening")
        print("FIRE-FOX")
        print(".")
        print(".")
        os.system("firefox")

    elif ("PC" in p) or ("PCHARM" in p) or ("PYCHARM" in p) or ("PYCH" in p):
        print("Opening")
        print("PYCHARM (COMMUNITY) EDITION")
        print(".")
        print(".")
        os.system("pycharm")

    elif ("NOTE" in p) or ("NOTES" in p) or ("NOTEPAD" in p) or ("EDITOR" in p) or ("9" in p):
        print("Opening")
        print("NOTEPAD")
        print(".")
        print(".")
        os.system("Notepad")

    elif ("VID" in p) or ("VIDEOS" in p) or ("VIDS" in p) or ("PLAYER" in p) or ("9" in p):
        print("Opening")
        print("VIDEOS")
        print(".")
        print(".")
        os.system("Videos")



    elif ("VLCPLAYER" in p) or ("PLAYER" in p) or ("VIDEO PLAYER" in p) or ("5" in p):
        print("Opening")
        print("VLC PLAYER")
        print(".")
        print(".")
        os.system("VLC")

    elif ("ILLUSTRATOR" in p) or ("AI" in p) or ("6" in p):
        print("Opening")
        print("ADOBE ILLUSTRATOR")
        print(".")
        print(".")
        os.system("illustrator")

    elif ("PHOTOSHOP" in p) or ("PS" in p) or ("PHOTOSHOP CC" in p) or ("7" in p):
        print("Opening")
        print("ADOBE PHOTOSHOP")
        print(".")
        print(".")
        os.system("photoshop")

    elif ("TELEGRAM" in p) or ("TG" in p) or ("10" in p):
        print("Opening")
        print("TELEGRAM")
        print(".")
        print(".")
        os.system("telegram")

    elif ("EXCEL" in p) or ("MSEXCEL" in p) or ("SHEET" in p) or ("WINEXCEL" in p) or ("3" in p):
        print("Opening")
        print("MICROSOFT EXCEL")
        print(".")
        print(".")
        os.system("excel")

    elif ("SLIDE" in p) or ("MSPOWERPOINT" in p) or ("PPT" in p) or ("POWERPNT" in p) or ("2" in p):
        print("Opening")
        print("MICROSOFT POWERPOINT")
        print(".")
        print(".")
        os.system("powerpnt")

    elif ("WORD" in p) or ("MSWORD" in p) or ("1" in p):
        print("Opening")
        print("MICROSOFT WORD")
        print(".")
        print(".")
        os.system("winword")

    # close the program
    elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" in p):
        print("Exiting")
        break

    # for invalid input
    else:
        print(p)
        print("Is Invalid,Please Try Again")
        print("is Invalid,Please try again")
        print(".")
        print(".")
