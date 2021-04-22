# OC 2020 : Création d'un Jeu 

## Introduction

Le but de ce travail est de créer un jeu en python, en utilisant la bibliothèque pygame, à l'aide des notions apprises en cours.


## Présentation de notre jeu

### Type de jeu
Notre jeu est un remake de Pokémon dans lequel le but est de constituer l'équipe la plus puissante possible afin de battre des dresseurs de pokémon de plus en plus puissants. Pour ce faire des pokémons pourront être capturés avec des capsules appelées "pokéballs".


### Comment jouer à ce jeu
Il s'agit d'un jeu comportant deux phases qui sont respectivement la phase combat et la phase de déplacement dans le monde des pokémons.

Pour la phase de combat il y'aura un choix entre quatre attaques disponibles afin de faire des dégats au pokémon adverse. Il y aura egalement la possibilité de fuir un combat lorsque le combat est engagé par un pokemon sauvage, à noter que cette dernière fonctionalité ne fonctionne pas lors d'un combat avec un dresseur adverse. Il y a également la possibilité de changer de pokémon ou bien encore de le soigner à l'aide de potions.

Pour la phase de déplacement, le personnage sera déplaçable avec avec les flèches, et il pourra intéragir avec des élements de la map en appuyant sur la touche "a". Dans le but de rencontrer des pokémons sauvages, le joueur devra se déplacer dans des fourrés afin de faire progresser son pokemon ou alors d'en capturer de nouveaux. Il faudra néanmoins faire attention aux autres dresseurs qui vous barreront la route et qui voudront vous combattre !


### Stucture interne de notre jeu
Notre jeu est principalement basé sur l'usage de classes. En effet c'est la méthode la plus simple pour créer rapidement et facilement un grand nombre de pokemons, de types , d'attaques et plus encore.
![2021-04-21 19_15_08-Thonny  -  C__Users_matte_Desktop_OC20 Maxime_oc20_game_test_class py  @  99 _ 3](https://user-images.githubusercontent.com/77661971/115594376-f52c7f80-a2d5-11eb-9436-9a0a06ee56df.png)

Voici notamment un exemple de notre classe attaque. 


### Classes contenues dans notre jeu

Comme cité auparavant notre jeu contient de nombreuses classes que vous pouvez voir ci-dessous :

![diagramclass](https://user-images.githubusercontent.com/77661971/115594923-99aec180-a2d6-11eb-92c5-4389971a0620.JPG)

Bien entendu ces classes ainsi que leurs attributs et méthodes ne sont pas définitives : comme un grand nombre d'idées continue d'affluer, certaines classes pourront disparaître ou être créées, d'autres se compléter ou deux classes pourront converger pour qu'une classe hérite d'une autre. Nous ne somme qu'au début du projet, qui va sûrement encore évoluer.

