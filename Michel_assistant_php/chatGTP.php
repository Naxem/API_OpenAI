<?php
    // Récupérer l'entrée utilisateur depuis le formulaire
    $userInput = $_POST["user_input"];

    // Chemin vers le fichier Python à exécuter
    $pythonScript = 'main.py';

    // Commande pour exécuter le script Python avec l'entrée utilisateur
    //$command = 'C:/Users/maxen/AppData/Local/Programs/Python/Python311/python.exe ' . $pythonScript . ' "' . $userInput . '" 2>&1';
    $command = 'python ' . $pythonScript . ' "' . $userInput . '" 2>&1';

    // Exécution de la commande et récupération de la sortie
    $output = shell_exec($command);

    // Affichage de la sortie
    echo $output;
?>