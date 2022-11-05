<?php
  // Vérifie qu'il provient d'un formulaire
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $host = "fic-ex-machina.fr";
    $username = "amaury";
    $password = "****";
    $database = "PJ";

    $personnage = $_POST["personnage"]; 
    $password_character = $_POST["password"];
    
    if (!isset($personnage)){
      die("Nom de votre personnage");
    }
    if (!isset($password)){
      die("Mot de passe");
    }
    
    $mysqli = new mysqli($host, $username, $password, $database);
    
    if ($mysqli->connect_error) {
      die('Error : ('. $mysqli->connect_errno .') '. $mysqli->connect_error);
    }  
    
    $statement = $mysqli->prepare("INSERT INTO `personnages` (`personnage`, `password`) VALUES(?, ?)"); 
    $statement->bind_param('ss', $personnage, $password_character); 
    
    if($statement->execute()){
      print "Bienvenue " . $personnage . "!";
    }else{
      print $mysqli->error; 
    }
  }
?>