def dire_bonjour(nom):
    print(f"Bonjour, {nom} !")

def dire_aurevoir(nom):
    print(f"À bientôt, {nom} !")

if __name__ == "__main__":
    nom = input("Ton nom : ")
    dire_bonjour(nom)
    dire_aurevoir(nom)
