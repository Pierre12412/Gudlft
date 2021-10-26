# gudlift-registration

### 1. Pourquoi ?

Ce projet est une version 'light' de la plateforme de réservation de compétition, son but est de garder les choses aussi simples que possible, et utilise les retours des utilisateurs pour s'améliorer.
  
### 2. Démarrer

Pour commencer, assurez vous d'avoir Python v.3.9.4.

Téléchargez le contenu du github dans un dossier : https://github.com/Pierre12412/Gudlft.git

### 3. Installation :

-------------------------------------- WINDOWS --------------------------------------

* Tapez la commande WIN+R, tapez 'cmd' et Entrée puis rendez vous dans le dossier du clone

* Pour vous rendre dans le fichier du projet, tapez cd puis le chemin d'accès, 
ou aidez vous de la touche TABULATION 
  * Exemple:  
  ```C:\Users\Pierre> cd Desktop``` (Vous fera parvenir au bureau)

* Une fois dans le fichier du projet que vous avez téléchargé, créez un environnement virtuel avec la commande:  
```python -m venv virtualenv```

* Activez le ensuite avec la commande :  
```virtualenv\Scripts\activate.bat```

* Puis récupérez les packages Python de requirements.txt avec la commande suivante :  
```pip install -r requirements.txt```

* Enfin allumez le serveur en entrant : 
```
set FLASK_APP=server.py

flask run 
```
* Vous pouvez maintenant vous rendre sur le site dans un navigateur avec l'adresse http://127.0.0.1:5000/

* Pour arrêter le serveur, appuyez sur CTRL + C dans le terminal

-------------------------------------- MAC/OS --------------------------------------

* Allez dans l'application Terminal

* Si vous n'avez pas encore Python v3.9.4, installez le sur https://www.python.org/downloads/,  et tapez ```python``` dans le terminal pour vérifier (sortez de python avec 'exit()')
  * Tapez également ```python -V``` pour vérifier la version que vous utilisez

* Pour vous rendre dans le fichier du projet, tapez cd puis le chemin d'accès, ou aidez vous de la touche TABULATION  ou de la commande ls

  * Exemple :  
  ```~ cd Desktop``` (Vous fera parvenir au bureau)

* Une fois dans le fichier du projet que vous avez téléchargé, créez un environnement virtuel avec la commande :  
```python -m venv virtualenv```

* Activez le ensuite avec la commande :  
```source ~/virtualenv/bin/activate```

* Puis récupérez les packages Python de requirements.txt avec la commande suivante :  
```pip install -r requirements.txt```

* Enfin allumez le serveur en effectuant la commande : 
````
set FLASK_APP=server.py

flask run 
````
* Vous pouvez maintenant vous rendre sur le site dans un navigateur avec l'adresse http://127.0.0.1:5000/

* Pour arrêter le serveur, appuyez sur CTRL + C dans le terminal

### 4. Testing

- Pour tester le projet, lancer la commande :  
```python -m pytest``` (dans le clone du projet)

### 5. Rapport de performance

- Lancer la commande 'locust' et se rendre à l'url : localhost:8089
- Entrer le nombre d'utilisateur, leur taux d'apparition et l'adresse http://127.0.0.1:5000/
- Appuyer sur Start Swarming


