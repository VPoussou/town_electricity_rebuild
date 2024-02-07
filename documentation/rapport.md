

**Premières réflexions**

Pour bien comprendre le problème, il faut que je commence par regarder les données fournies, d'abord leur structure, puis si possible identifier des particularités.
Pour bien commencer ce processus réfléchissons un peu à ce qu'on cherche à faire. On souhaite finalement minimiser un coût. Qui doit dépendre de façon assez linéaire de la longueur de cable installée. La complexité réside donc dans la connaissance pour chaque ***x*** mètres/mm du cable du nombre de maisons qu'il va aider à raccorder.
Sauf que dans l'énoncé se cache quelque chose d'intéressant. Comme il faut ***rapidement*** rétablir la connection pour ***le plus grand nombre de logements*** possible, avec le minimum de ***coûts***, cela signifie que le projet a en réalité au moins deux phases. Une phase d'action rapide à fort impact, et une phase où l'on raccorde touts les logements, dans l'ordre du moins coûteux au plus coûteux.
Je ne suis pas certain que cette réflexion soit intéressante à terme. Il est possible que ces deux phases se chevauchent naturellement en établissant un ordre de priorité pour les segments de cable à installer.
QGIS est en cours d'installation pour regarder les Shapefiles. En attendant je vais regarder le CSV.

**Deuxième phase**

Un des éléments structurels du problème, c'est que comme c'est un réseau électrique, l'électrécité arrive de quelque part. Elle peut avoir un ou plusieurs points d'entrée, mais c'est forcément depuis ces endroits là que ça a du sens de reconstruire les infrastructure puisque l'objectif est que les usagers soient de nouveau raccordés le plus rapidement possible

**Lecture des données**

Tout ça ressemble diablement à un BFS relié à une DF exportée en CSV. Sinon du coup la première chose c'est qu'on peut transformer le statut des infras en un booléan "broken". Ensuite l'autre chose qui est bien plus intéressante c'est la récurrence des infras par rapportx au bâtiments. Enfin pour être plus clair, le fait que une et une seule infrastructure peut relier de nombreux bâtiments entre eux.
À l'étape où l'on va regarder combien de logements une infra peut relier il va falloir faire attention à ça. Avant de prendre en compte la longeur bien sur.