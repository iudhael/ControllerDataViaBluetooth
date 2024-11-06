# ControllerDataViaBluetooth
Connexion d’une manette (cas d'une manette PS4) à un ordinateur via Bluetooth, puis réception des valeurs des boutons et des sticks analogiques sur l'ordinateur.

Pour connecter une manette PS4 à un ordinateur Linux via Bluetooth et recevoir les valeurs des boutons et des sticks analogiques, suivez les étapes suivantes :

1.   Installez les dépendances nécessaires avec les commandes :
   ```bash
   sudo apt-get install python-dev python-pip gcc
   ```

2.   Installez la bibliothèque approxeng.input, qui permet de lire les entrées de la manette :
   ```bash
   pip install approxeng.input
   ```

   Cela configurera votre système pour recevoir les valeurs de la manette PS4 sur un système Linux.

3.   Si le système dispose déjà des dépendances Bluetooth : appariez la manette avec l'ordinateur via l'interface graphique.

4.   Si le système ne dispose pas des dépendances Bluetooth : installez-les avec les commandes suivantes :
   ```bash
   sudo apt-get install bluetooth libbluetooth3 libusb-dev
   sudo systemctl enable bluetooth.service
   sudo usermod -G bluetooth -a username
   ```

5.   Si vous préférez utiliser la console, suivez le guide d'appariage de manette sur Linux : [approxeng.input Bluetooth pairing guide.](https://approxeng.github.io/approxeng.input/bluetooth.html)
6.   Mapper les touches de la manette
Pour vous assurer que chaque touche (comme le triangle) est correctement mappée, suivez les instructions de profilage disponibles ici : [approxeng.input Profiling Guide.](https://approxeng.github.io/approxeng.input/profiling.html)

7.   Tester les contrôles
*   Une fois le mappage terminé, un fichier de configuration sera généré. Déplacez ce fichier dans le dossier ~/.approxeng.input/ en utilisant la commande suivante :
   ```bash
   mv <fichier_de_configuration> ~/.approxeng.input/
   ```

*   Ensuite, dans la console, exécutez la commande suivante pour tester le fonctionnement des axes et des boutons :
   ```bash
   approxeng_input_show_controls
   ```

Cela vous permettra de bouger les axes et appuyer sur les boutons pour vérifier que les touches sont correctement mappées.

8.   Récupérer et afficher les valeurs
*  Pour récupérer les valeurs des boutons et axes, lancez le fichier controller.py. Ce fichier vous permettra de récupérer et d'afficher en temps réel les valeurs des boutons et des axes de la manette.
Vous pouvez consulter ces détails [ici](https://approxeng.github.io/approxeng.input/simpleusage.html)






