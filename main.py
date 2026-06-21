# -Variables-

langue = "a"
unite = "a"
valeur = "a"
exit = "a"
langue2 = "a"

# -Fonctions-

while True:
    try:
        
        # -Langue-
        
        while True:
            try:
                langue = int(input("0 pour le français, 1 for english."))
                if langue == 0 or 1:
                    langue2 = langue
                    break
            except ValueError:
                print("Entre un chiffre correct / Enter a valid number.")
                
        # -FR-
        
        if langue == 0:        
            while True:
                try:
                    unite = int(input("0 pour Ko, 1 pour KB."))
                    if unite == 0 or 1:
                        break
                except ValueError:
                    print("Entre un chiffre correct.")
                    
        if unite == 0:
            while True:
                try:
                    valeur = int(input("Combien de Ko ?"))
                    print(valeur, "Ko est égale à", valeur * 8,"KB")
                    unite = "a"
                    break
                except ValueError:
                    print("Entre un chiffre correct.")
                    
        if unite == 1:
            while True:
                try:
                    valeur = int(input("Combien de KB ?"))
                    print(valeur, "KB est égale à", valeur / 8,"Ko")
                    unite = "a"
                    break
                except ValueError:
                    print("Entre un chiffre correct.")
                    
        # -EN-

        if langue == 1:
            while True:
                try:
                    unite = int(input("0 for Ko, 1 for KB."))
                    if unite == 0 or 1:
                        break
                except ValueError:
                    print("Enter a valid number.")
                    
        if unite == 0:
            while True:
                try:
                    valeur = int(input("How many Ko?"))
                    print(valeur, "Ko is equal to", valeur * 8, "KB")
                    unite = "a"
                    break
                except ValueError:
                    print("Enter a valid number.")
                    
        if unite == 1:
            while True:
                try:
                    valeur = int(input("How many KB?"))
                    print(valeur, "KB is equal to", valeur / 8, "Ko")
                    unite = "a"
                    break
                except ValueError:
                    print("Enter a valid number.")
                    
        # -Exit or continue-
                    
        if langue2 == 0:
            exit = int(input("Entre 0 pour continuer, 1 pour quitter."))
        else:
            exit = int(input("Enter 0 to continue, 1 to exit."))
            
        if exit == 1:
            break
        
    except ValueError:
        print("Entre un chiffre correct / Enter a valid number.")
