# UFAprovadesVsAvaluades
Forked from: [https://gist.github.com/jherna/56099f3a6f58a3e3f30ccfa3ee87d5e5](https://gist.github.com/jherna/56099f3a6f58a3e3f30ccfa3ee87d5e5).

_Script_ que, a partir de les actes en PDF descarregades de SAGA, compta el total d'UF aprovades i avaluades i calcula la ratio d'aprovades sobre el total en format de percentatge.

## Installation
Download the script. Place the PDF in the root folder.

## Requeriments
`pip install tika`

In case you have both Python versions, 2 and 3, installed in your computer:

`pip3 install tika`

Take into account the first time running the "tika" library it will need to download and install some libraries. This process may take a couple of minutes.

## Running
Run from Terminal:

`$ python path/to/UFAprovadesVsAvaluades.py path/to/Acta.pdf`

In case you have both Python versions, 2 and 3, installed in your computer:

`$ python3 path/to/UFAprovadesVsAvaluades.py path/to/Acta.pdf`
