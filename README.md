# Checker

Checker est un programme (ou un script) qui permet de rechercher une information dans un ensemble de fichiers et d'en ressortir tous les fichiers où apparait cette information.

## Exemple

- Je veux appliquer le RGPD et supprimer tous les documents qui contiennent mon nom (droit à l'oubli). Je donne le nom au script et il me sort une liste de tous les documents qui contiennent mon nom.

- Je cherche tous les documents qui parle d'un sujet X, il doit savoir me donner tous les documents qui en parle

## Contraintes

- Le script doit être documenté et facilement modifiable si on doit le faire évoluer
- Il faut un guide d'utilisation
- Il est préférable d'avoir des tests pour s'assurer que rien ne casse quand on l'évolue
- Ca doit tourner sur tous les OS (Windows, Linux, MacOS, ...)
- On doit savoir définir l'information que l'on recherche (un ou plusieurs mots) dans un fichier de config
- Le fichier de config reprendra les informations suivantes (au minimum)
    * Le(s) information(s) à rechercher
    * La racine du dossier de recherche
    * Les dossiers et fichiers exclus
- Le programme doit savoir effectuer sa recherche en local ou sur un drive (Google)
    * Ajouter des credentials au fichier de config (ou autre (clé d'accès, ...))
- Doit prendre en compte différents types de fichier :
    * .pdf
    * .docx / .odt
    * .xlsx
    * .pptx
    * .txt
    * .tex
    * .md
    * Document google docs, google sheet, google slide ...
    * [Facultatif] Si possible : .png / .jpg / .jpeg / .mov / .mp4
- Le fichier de sortie doit reprendre les infos suivantes : 
    * Chemin d'accès du fichier
    * Type de fichier
    * [Facultatif] Ou se trouve la donnée. Ex : pdf xxx.pdf - Page 5 (ce n'est peut être pas possible)

### Exemple de fichier de config

```json
{
    "dataToFind" : [
        "Name",
        "XXX"
    ],
    "root" : "/etc/checker/folder",
    "excluded" : [
        "/misc",
        "/vscode",
        "temp.txt"
    ],
    "credential" : {
        "login" : "root",
        "password" : "admin"
    }
}
```