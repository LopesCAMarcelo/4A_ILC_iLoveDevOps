import sys
from flask import Flask
from models.personne import Personne
from datetime import datetime
import csv

import hashlib

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
	return str(liste_to_show)
 
@app.route('/transaction-<p1>-<p2>-<somme>', methods=['PUT','GET'])
def transaction(p1,p2,somme):
	p1 = int(p1)
	p2 = int(p2)
	somme = int(somme)
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
		t = datetime.now()
		s = somme
		transac = (client1, client2, t, s)
		h = hashlib.sha256(str(transac).encode()).hexdigest()

		client1.solde -= s
		client2.solde += s
		liste_transaction_personnes.append([client1.id,client2.id,t,s,h])
		liste_transaction.append(client1.nom + " " + client1.prenom + " a envoye " + str(somme) + " a " + client2.nom + " " + client2.prenom + " hash: " + str(h) + ", t: "+ str(t) + ".")
		return "Transaction done !"
	elif doesClient1Exist and doesClient2Exist:
		return "Not enough money !"
	elif doesClient2Exist:
		return "Client 1 does not exist !"
	elif doesClient1Exist:
		return "Client 2 does not exist !"
	else:
		return "The clients does not exist !"

@app.route('/affiche-transactions', methods=['GET'])
def affichage_transactions():
	return str(liste_transaction)

@app.route('/affiche-transactions-<p>', methods=['GET','PUT'])
def affichage_transactions_client(p):
	p = int(p)
	liste_transaction_client_index = []
	liste_transaction_client = []
	for i in range(len(liste_transaction_personnes)):
		if liste_transaction_personnes[i][0]==p or liste_transaction_personnes[i][1]==p:
			liste_transaction_client_index.append(i)
	for index in liste_transaction_client_index :
		liste_transaction_client.append(liste_transaction[index])
	return str(liste_transaction_client)

@app.route('/affiche-solde-<p>', methods=['GET','PUT'])
def affichage_solde(p):
	p = int(p)
	for elt in liste_de_clients:
		if elt.id==p:
			return str(elt.solde)
	return "this client does not exist"


@app.route("/intégriteDesTransactions", methods=['GET'])
def intégriteDesTransactions():
	display = ""

	for transaction in liste_transaction:
		client1 = transaction[0]
		client2 = transaction[1]
		temps = transaction[2]
		somme = transaction[3]
		transac = (client1,client2,temps,somme)
		h = hashlib.sha256(str(transac).encode()).hexdigest()
		
		if h != transaction[4]:
			display += "La Transaction : " + str(transaction[4]) + " : " + " n'est pas valide !!!!!" + "\n"
		
	if display == "":
		display = "Toutes les transactions sont valides ! \n"
		
	return display

#permet de corriger le hash avec le temps actuelle 
def corectionHash(transaction):
	client1 = transaction[0]
	client2 = transaction[1]
	t = datetime.now()
	s = transaction[3]
	transac = (client1,client2,t,s)
	h = hashlib.sha256(str(transac).encode()).hexdigest()
	return h


if __name__ == '__main__':
	if len(sys.argv) > 1:
		if sys.argv[1] == "check_syntax":
			print("Build [ OK ]")
			exit(0)
		else:
			print("Passed argument not supported ! Supported argument : check_syntax")
			exit(1)
	app.run(debug=True)
