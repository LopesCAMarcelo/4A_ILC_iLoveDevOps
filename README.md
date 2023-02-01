# 4A_ILC_iLoveDevOps #

## Equipe du projet : ## 

__Peyron Calvin__
__Lopes Marcelo__
*Spécialité : ILC*

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Buymeacoffee](https://badgen.net/badge/icon/buymeacoffee?icon=buymeacoffee&label)](https://https://www.buymeacoffee.com/)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)

## Brève explication du sujet : ##
Ce projet est une API dont le but est de simuler des transactions bancaires entre des clients fictifs.

Notre API utilise python, un langage de programmation interprété de haut niveau, facile à lire et à écrire. Il est souvent utilisé pour le développement web, la science des données, l'apprentissage automatique et la création de scripts système. Il a une grande communauté de développeurs et offre de nombreuses bibliothèques utiles. Bien qu'il ne soit pas le plus rapide, il est suffisamment rapide pour la plupart des tâches.

Les librairies utilisées sont csv et Flask. Celles-ci nous permettent respectivement de lire et traiter un fichier csv et de créer une application WEB avec Python.

Dans un soucis de compréhension, nous avons choisi ce sujet qui nous semblait le plus à même de nous apporter des connaissances nécessaires à la création d'une API.

## Fonctionnement de l'API : ##

* Création d'objets de la classe Personne : Une personne est définie par un nom (String), un prénom (String), un solde (int) et un id (int). *
* Lecture d'un fichier csv contenant une liste de client initiale, ces clients sont stockés dans une liste. *
* Création de deux listes vides qui serviront à contenir les transactions (texte qui dérit l'expéditeur, la somme et le receveur) pour la première et les tuples de personne effetuant les transactions pour la deuxième. *
* Explication des routes:
	* "/": racine de l'application WEB, affiche simplement un message d'accueil.
	* "/showMeTheCSV": permet de voir le contenu du ficher CSV.
	* "/transaction-<p1>-<p2>-<somme>": permet d'effectuer une transaction entre deuw personnes si les conditions requises sont vérifiées, prend en entrée 3 arguments qui sont l'id de la première et de la deuxième personne ainsi que la somme de la transaction.
	* "/affiche-transactions": affiche toutes les transactions effectuées à ce jour.
	* "/affiche-transaction-<p>": affiche pour une personne donnée toutes les transactions dont elle est soit émettrice, soit receveuse, prend en paramètre 1 argument qui est l'id de la personne.
	* "/affiche-solde": affiche pour une personne donnée son solde, prend en paramètre 1 argument qui est l'id de la personne.

## Hachage: ##

Nous avons choisi d'utiliser SHA-256 pour plusieurs raisons:
* Il est le premier à apparaître sur la documentation de la librairie (RTFM)
* Il est l'un des plus documentés
* Il est grandement accepté et utilisé
* Il présente de très bonnes caractéristiques que ce soit en sécurité et en efficacité


### We are successful: ###

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)
[![forthebadge](https://forthebadge.com/images/badges/contains-cat-gifs.svg)](https://forthebadge.com)
[![ForTheBadge winter-is-coming](http://ForTheBadge.com/images/badges/winter-is-coming.svg)](http://ForTheBadge.com)
