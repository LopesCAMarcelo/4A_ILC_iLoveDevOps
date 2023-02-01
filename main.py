from flask import Flask
from models.personne import Personne
import csv

app = Flask(__name__)

#Notre liste de clients qui évoluera au fil du temps
liste_de_clients = []
#On ajoute quelques personnes (toute ressemblance fortuite à une personne existante est le fruit du hasard)
with open('clients.csv') as csv_file:
	csvFile = csv.reader(csv_file, delimiter=',')
	i = 0
	for row in csvFile:
		if i != 0:
			id = int(row[0])
			nom = row[1]
			prenom = row[2]
			solde = int(row[3])
			liste_de_clients.append(Personne(id,nom,prenom,solde))
		i+=1
liste_transaction = []
liste_transaction_personnes = []

@app.route('/')
def hello_dear_user():
	return "Hello dear master, tell me your transaction <3"

@app.route('/showMeTheCSV', methods=['GET'])
def easyFunc():
	liste_to_show = []
	for elt in liste_de_clients:
		liste_to_show.append(str(elt.id) + " -> " + elt.nom + " " + elt.prenom + " possede " + str(elt.solde) + "euros.\n")
	return liste_to_show
 
@app.route('/transaction-<p1>-<p2>-<somme>', methods=['PUT'])
def transaction(p1,p2,somme):
	doesClient1Exist = False
	doesClient2Exist = False
	for elt in liste_de_clients:
		if elt.id == p1:
			client1 = elt
			doesClient1Exist = True 
		elif elt.id == p2:
			client2 = elt
			doesClient2Exist = True
	if doesClient1Exist and doesClient2Exist and client1.solde > somme:
		client1.solde -= somme
		client2.solde += somme
		liste_transaction_personnes.append([p1,p2])
		liste_transaction.append(p1.nom + " " + p1.prenom + " a envoyé " + str(somme) + " à " + p2.nom + " " + p2.prenom + ".")
		return "Transaction done !!!"
	elif doesClient1Exist and doesClient2Exist:
		return "Not enough money !!!"
	elif doesClient2Exist:
		return "Client 1 does not exist !!"
	elif doesClient1Exist:
		return "Client 2 does not exist !!"
	else:
		return "The clients does not exist !!"

@app.route('/affiche-transactions', methods=['GET'])
def affichage_transactions():
	return liste_transaction

@app.route('/affiche-transactions-<p>', methods=['GET'])
def affichage_transactions_client(p):
	liste_transaction_client_index = []
	liste_transaction_client = []
	for i in range(len(liste_transaction_personnes)):
		if liste_transaction_personnes[i][0]==p or liste_transaction_personnes[i][1]==p:
			liste_transaction_client_index.append(i)
	for index in liste_transaction_client_index :
		liste_transaction_client.append(liste_transaction[index])

@app.route('/affiche-solde-<p>', methods = ['GET'])
def affichage_solde(p):
	return p.solde	


if __name__ == '_main_':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax":
			print("Build [ OK ]")
			exit(0)
		else:
			print("Passed argument not supported ! Supported argument : check_syntax")
			exit(1)
	app.run(debug=True)
