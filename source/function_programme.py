
import json
import os
from main import menu_principal
data=json.load(open('base.json'))

def afficher_pays():
     for i in data:
          print("\t \t code: " +i+ " \t Nom: "+data[i]["nom"]+" \t Capital:" +data[i]["capital"]+ " .")
     
     input("\n\t Operation Reussie! \n \t appuyer sur entrer pour revenir au menu principal")
     menu_principal()

def effacer_pays():
     global data
     os.system("cls")
     print("\t - - SUPPRIMER UN PAYS - -")
     print("\tLes codes disponibles : \n")
     for i in data:
          print("\t "+ i, end="")

     code = input("\t Saisir le code du pays a supprimer : ")
     print("\n")
     data.pop(str(code))
     out_file = open("data.json",'w');
     json.dump(data,out_file,indent=5)
     out_file.close()
     input("\n\t Operation Reussie! \n \t appuyer sur entrer pour revenir au menu principal")
     menu_principal()


def modifier_pays():
     global data
     os.system("cls")
     print("\t - - MODIFIER UN PAYS - -")
     print("\t Les codes disponibles : \n")
     for i in data:
          print("\t "+ i, end="")

     code = input("\t Saisir le code du pays a modifier : ")
     print("\n")
     nom = input("\t Modifier le nom du pays "+ str(code) + "- Ancien = " + str(data[code]['nom']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if nom == "":
          nom = data[code]["nom"]

     capital = input("\t Modifier la capital du pays "+ str(code) + "- Ancien = " + str(data[code]['capital']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if capital == "":
          capital = data[code]["capital"]

     population = input("\t Modifier la population du pays "+ str(code) + "- Ancien = " + str(data[code]['population']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if population == "":
          population = data[code]["population"]

     langue = input("\t Modifier la langue du pays "+ str(code) + "- Ancien = " + str(data[code]['langue']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if langue == "":
          langue = data[code]["langue"]

     superficie = input("\t Modifier le superficie du pays "+ str(code) + "- Ancien = " + str(data[code]['superficie']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if superficie == "":
          superficie = data[code]["superficie"]

     independance = input("\t Modifier la date d'independance du pays "+ str(code) + "- Ancien = " + str(data[code]['independance']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if independance == "":
          independance = data[code]["independance"]

     president = input("\t Modifier le president du pays "+ str(code) + "- Ancien = " + str(data[code]['president']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if president == "":
          president = data[code]["president"]

     pib = input("\t Modifier le pib du pays "+ str(code) + "- Ancien = " + str(data[code]['pib']+ "\n Laisser vide si vous ne voullez pas modifier : "))
     if pib == "":
          pib = data[code]["pib"]

          
     data[code] = {
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
     json.dump(data,out_file,indent=5)
     out_file.close()
     input("\n\t Operation Reussie! \n \t appuyer sur entrer pour revenir au menu principal")
     menu_principal()



def ajouter_pays():
     global data
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
     data[code] = {
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
     json.dump(data,out_file,indent=5)

     out_file.close()
     content=json.load(open("data.json"))
     input("\t Operation Reussie! \n appuyer sur entrer pour revenir au menu principal")
     menu_principal()
