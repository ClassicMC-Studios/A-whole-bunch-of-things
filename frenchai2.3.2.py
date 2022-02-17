import time
import random
print("---French Practice Ai Development test---")
print("---------Copyright ClassicMC 2021--------")
print("------------------v2.3.2-----------------")
print("-----Please answer in full sentences-----")


bonjour =input("Bonjour! ")
if bonjour =='Bonjour! Comment tu t\'appelles?'or bonjour =='Bonjour. Comment tu t\'appelles?':
    print("Je M'apelles Ai DevTest.")
    enchant = input("Enchanté. ")
    if enchant =='Enchante.'or enchant =='Enchante!':
        age = input("Tu as kell agé? ")
        if age =='J\'ai treize ans.'or age =='J\'ai douze ans.':
            print("Jai un semaine age.")
            day = input("C'est quel jour?")
            if day == 'Aujourd\'hui c\'est lundi.'or day == 'Aujourd\'hui c\'est mardi.'or day == 'Aujourd\'hui c\'est mercredi.'or day == 'Aujourd\'hui c\'est jeudi.'or day == 'Aujourd\'hui c\'est vendredi.'or day == 'Aujourd\'hui c\'est samedi.'or day == 'Aujourd\'hui c\'est dimanche.':
                print("Oui!")
                print("--You have reached the end of the--")
                print("--------French Practice Ai---------")
                print("--------------Credits--------------")
                print("~Made by, ClassicMC")
                print("~Developed using Python")
                print("~Written on Online Python BETA")
                print("~Some code wirtten on Programiz")
                print("~Made for the use of French 1 students")
                print("~Also made for the use of French 1 teachers.")
                print("~Thanks to online documentation for Some help spelling")
                print("This program is only usable with given access.")
                print("Any use of this program without written acess is disallowed")
                print("This is v2.3.1 of the French Develpment AI.")
                print("--------------The-End---------------")
                print("------------------------------------")
                
                adb =input("Activate debugger ")
                while adb == 'yes':
                    printNum = random.randint(0, 2)
                    print(printNum)
                    time.sleep(0.1)
            else:
                print("-----------------------------------------")
                print("Traceback (most recent call):")
                print(" File <main.py>, line 4 in <module>")
                print(f"FrenchSyntaxError: {day} is not defined.") 
        else:
            print("-----------------------------------------")
            print("Traceback (most recent call):")
            print(" File <main.py>, line 3 in <module>")
            print(f"FrenchSyntaxError: {age} is not defined.")        
    else:
        print("-----------------------------------------")
        print("Traceback (most recent call):")
        print(" File <main.py>, line 2 in <module>")
        print(f"FrenchSyntaxError: {enchant} is not defined.")    
else:
    print("-----------------------------------------")
    print("Traceback (most recent call):")
    print(" File <main.py>, line 1 in <module>")
    print(f"FrenchSyntaxError: {bonjour} is not defined.")
