# Projet 5: utiliser les données publiques d'Open Food Facts
Programmes ecrits en Python3

## **1. Présentation:**

Le but de cette application est de proposer à l'utilisateur une solution pour substituter un produit alimentaire de meilleur qualité à un autre.
Pour cela, l'utilisateur est amené à sélectionner un produit dans une catégorie et l'application lui propose un produit de la même catégorie dont le nutriscore possède la note "a" ou "b" 

## **2. Prérequis :**

Installer les dépendances : "pip install -r requirements.txt"

Liste des librairies :
<ul> 
<li>requests</li>
<li>pyqt5</li>
<li>wheel</li>
</ul>

Télécharger le connecteur mysqlclient-1.4.6-cp38-cp38-win32.whl et l'installer  : "pip install mysqlclient-1.4.6-cp38-cp38-win32.whl".

Utiliser python 3

## **3. Paramétrage :**

**Serveur MySql :**

Pour utiliser ce programme , il faudra au préalable avoir créer un serveur MySql et reporté les données de connexion dans le fichier settings.py
L'utilisateur spécifié devra avoir accès au serveur.

**Fichier settings :**

* **Limite d'éléments à afficher dans les combobox** 
  * **NB_OF_CATEGORY_TO_SHOW :** Nombre de catégories à afficher.
  * **NB_OF_PRODUCT_TO_SHOW :** Nombre de produits à afficher.
  * **NB_OF_SUBSTITUTE_TO_SHOW :** Nombre de substituts à afficher.
  * **NB_OF_FAVORITE_SUBSTITUTE_TO_SHOW :** Nombre de substituts favoris à afficher.
* **Informations de connexion à la base de données** 
  * **DATABASE_HOST :** Host de la base de données.
  * **DATABASE_NAME :** Nom de la base de données.
  * **DATABASE_USER :** utilisateur de la base de données.
  * **DATABASE_PWD :** Mot de passe de la base de données.
  * **DATABASE_ACCESS_PORT :** Port d'accès à la base de données.
* **PLAIN_TEXT_BACKGROUND_COLOR :** Couleur de fond du PlainText Widget

## **4. Démarrage :**
**Création de la base de données : create_database_alimentation.sql**

Lors de la première utilisation de l'application, ce script crée la structure de la base qui contient trois tables : 
<ul> 
<li>product</li>
<li>category</li>
<li>favorite</li>
</ul>

## **5. Utilisation :**

**Substituer un produit :**
L'interface graphique permet à l'utilisateur de sélectionner dans l'ordre :

<ul> 
 
**<li>la source de recherche</li>**
 
L'utilisateur peut choisir entre rechercher dans la base de données et sur l'API d'OpenFoodFact.
Le programme charge alors les catégories présentent dans le support sélectionné.
**<li>la catégorie du produit</li>**

L'utilisateur sélectionne la catégorie de produit désirée. 
Le programme cherche alors les produits associés dans le support sélectionné.
Si la recherche dans la base de données a été selectionnée et qu'il n'y a pas d'enregistrement, l'application cherchera automatiquement sur l'API.
**<li>le produit qu'il souhaite substituer</li>**

L'utilisateur sélectionne le produit qu'il souhaite substituer.
Les informations associées au produit sélectionné sont affichées dans une table.
Le programme cherche alors les substituts associés dans le support sélectionné.
Si la recherche dans la base de données a été selectionnée et qu'il n'y a pas d'enregistrement, l'application cherchera automatiquement sur l'API.
**<li>le substitut qu'il souhaite utiliser</li>**

L'utilisateur sélectionne le substitut qu'il souhaite utiliser. 
Les informations associées au substitut sélectionné sont affichées dans une table.
</ul>

**Naviguer dans les différents éléments des combobox**

Afin de ne pas surcharger les listes présentes dans les combobox, une limite, configurable depuis le fichier settings.py, a été créée.
Pour naviguer sur les prochains/précédents éléments des listes, il suffit d'utiliser les bouttons next/last.

**Sauvegarder un couple substitut/produit :**

Une fois que l'utilisateur a sélectionner un produit et un substitut, ce couple peut être enregistré dans une liste de favoris afin de pouvoir y accéder de nouveau même après la fermeture de l'application

Lors d'un enregistrement, l'application vérifie que :

<ul> 
<li>la catégorie éxiste dans la base de données</li>
Sinon, celle-ci est enregistrée dans la base.
<li>le produit éxiste dans la base de données</li>
Sinon, celui-ci est enregistré dans la base.
<li>le substitut éxiste dans la base de données</li>
Sinon, celui-ci est enregistré dans la base.
</ul>

## **6. Lancement de l'application :**

Pour lancer l'application, il suffit de lancer le fichier *app.py*.