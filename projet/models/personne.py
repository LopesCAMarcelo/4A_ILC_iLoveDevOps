class Personne:
	nom = ""
	prenom = ""
	solde = 0
	id = 0		
	def __init__(self, id, nom, prenom, solde):
		self.id = id
		self.nom = nom
		self.prenom = prenom
		self.solde = solde
