import json
# OPERATING SYSTEM
import os 

# IMPORTER LES DONNEES
content = json.load(open("data.json"))

def afficher_pays():
     for i in content:
          print(" code: " +i
          +"  Nom: "+content[i]["nom"]
          +"  Capital:" +content[i]["capital"]
          +"  Langue:" +content[i]["langue"]
          +"  Population:" +str(content[i]["population"])
          +"  Superficie:" +str(content[i]["superficie"])
          +"  Independance:" +content[i]["independance"]
          +"  President:" +content[i]["president"]
          +"  Pib:" +str(content[i]["pib"])
          
          )
     
     input("\n\t Operation Reussie! \n \t appuyer sur entrer pour revenir au menu principal")
     menu_principal()

def effacer_pays():
     global content
     os.system("cls")
     print("\t - - SUPPRIMER UN PAYS - -")
     print("\tLes codes disponibles : \n")
     for i in content:
          print("\t "+ i, end="")

     code = input("\t Saisir le code du pays a supprimer : ")
     print("\n")
     content.pop(str(code))
     out_file = open("data.json",'w');
     json.dump(content,out_file,indent=5)
     out_file.close()
     input("\n\t Operation Reussie! \n \t appuyer sur entrer pour revenir au menu principal")
     menu_principal()


def modifier_pays():
     global content
     os.system("cls")
     print("\t - - MODIFIER UN PAYS - -")
     print("\t Les codes disponibles : \n")
     for i in content:
          print("\t "+ i, end="")

     code = input("\t Saisir le code du pays a modifier : ")
     print("\n")
     nom = input("\t Modifier le nom du pays "+ str(code) + "- Ancien = " + str(content[code]['nom']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if nom == "":
          nom = content[code]["nom"]

     capital = input("\t Modifier la capital du pays "+ str(code) + "- Ancien = " + str(content[code]['capital']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if capital == "":
          capital = content[code]["capital"]

     population = input("\t Modifier la population du pays "+ str(code) + "- Ancien = " + str(content[code]['population']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if population == "":
          population = content[code]["population"]

     langue = input("\t Modifier la langue du pays "+ str(code) + "- Ancien = " + str(content[code]['langue']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if langue == "":
          langue = content[code]["langue"]

     superficie = input("\t Modifier le superficie du pays "+ str(code) + "- Ancien = " + str(content[code]['superficie']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if superficie == "":
          superficie = content[code]["superficie"]

     independance = input("\t Modifier la date d'independance du pays "+ str(code) + "- Ancien = " + str(content[code]['independance']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if independance == "":
          independance = content[code]["independance"]

     president = input("\t Modifier le president du pays "+ str(code) + "- Ancien = " + str(content[code]['president']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if president == "":
          president = content[code]["president"]

     pib = input("\t Modifier le pib du pays "+ str(code) + "- Ancien = " + str(content[code]['pib']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if pib == "":
          pib = content[code]["pib"]

          
     content[code] = {
          "nom": nom,
          "capital": capital,
          "population": population,
          "langue": langue,
          "superficie": superficie,
          "independance": independance,
          "president": president,
          "pib": pib
     }
     out_file = open("data.json",'w');
     json.dump(content,out_file,indent=5)
     out_file.close()
     input("\n\t Operation Reussie! \n \t appuyer sur entrer pour revenir au menu principal")
     menu_principal()



def ajouter_pays():
     global content
     os.system("cls")
     print("\t - - AJOUTER UN PAYS - -")
     code = input("\t Saisir le code du pays : ")
     try:
          int(code)
     except:
          print("\t Le code doit etre un entier")
          code = input("\t Saisir le code du pays : ")
     print("\n")
     nom = input("\t Veuillez saisir le nom du pays :")
     capital = input("\t Veuillez saisir le capital du pays :")
     langue = input("\t Veuillez saisir le langue du pays :")
     president = input("\t Veuillez saisir le president du pays :")
     population = input("\t Saisir la population du pays : ")
     superficie = input("\t Saisir la superficie du pays : ")
     pib = input("\t Saisir le pib du pays : ")
     date = input("\t Saisir le date d'independance du pays, format: JJ-MM-AAAA : ")
     content[code] = {
        "nom":nom,
        "capital":capital,
        "population":population,
        "langue":langue,
        "superficie":superficie,
        "independance":date,
        "president":president,
        "pib":pib
    }
     out_file = open("data.json",'w')
     json.dump(content,out_file,indent=5)

     out_file.close()
     content=json.load(open("data.json"))
     input("\t Operation Reussie! \n appuyer sur entrer pour revenir au menu principal")
     menu_principal()


def menu_principal():
     os.system("cls")
     print("\t - - MENU PRINCIPALE - - \t")
     print("\t 1. LISTE DES PAYS")
     print("\t 2. AJOUTER UN PAYS")
     print("\t 3. MODIFIER UN PAYS")
     print("\t 4. SUPPRIMER UN PAYS")
     print("\t 5. QUITTER")

     choix = input("\t - - Veuillez Choisir ? - - \n \t >")
     try :
          int(choix)
     except :
          print("\t Veuillez Reessayer")
          
     choix = int(choix)
     if(choix == 1):
          afficher_pays()
     elif(choix == 2):
          ajouter_pays()
     elif(choix == 3):
          modifier_pays()
     elif(choix == 4):
          effacer_pays()
     
     else:
          os.system("exit")


if __name__ == "__main__":
     menu_principal()