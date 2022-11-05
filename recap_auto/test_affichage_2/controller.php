<?php
  // Vérifie qu'il provient d'un formulaire
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"]; 
    $email = $_POST["email"];
    
    if (!isset($personnage)){
      die("Nom de votre personnage");
    }
    if (!isset($password)){
      die("Mot de passe");
    }
    
    print "Salut " . $name . "!, votre mot de passe est ". $password;
  }
?>