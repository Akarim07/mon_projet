#Script qui demande à l'utilisateur de saisir une classe entre
#A, B et c. Le script affiche les infos réseau de la classe
classe=input("Entrer une classe entre A, B ou C : ")
if classe=="A" or classe=="a":
    print("Informations Adresses Classe A")
    print(' - - -'*10)
    print("Premiere Adresse Utilisable 0.0.0.1")
    print("Dernière Adresse Utilisable A 126.255.255.254")
    print("Adresse de diffusion Classe A 126.255.255.255")
    print("Adresse Masque Classe A 255.0.0.0")
    print(' - - -'*10)
elif classe=="B" or classe=="b":
    print(' - - -'*10)
    print("Premiere Adresse Utilisable 128.0.0.1")
    print("Dernière Adresse Utilisable B 191.255.255.254")
    print("Adresse de diffusion Classe B 191.255.255.255")
    print("Adresse Masque Classe B 255.255.0.0")
    print(' - - -'*10)
elif classe=="C" or classe=="c":
    print(' - - -'*10)
    print("Premiere Adresse Utilisable 192.0.0.1")
    print("Dernière Adresse Utilisable B 223.255.255.254")
    print("Adresse de diffusion Classe B 223.255.255.255")
    print("Adresse Masque Classe B 255.255.255.0")
    print(' - - -'*10)
else:
    print("La classe n'est pas définie sur la liste ")
