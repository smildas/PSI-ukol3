#Popis implementace

Jednoduchý skript získvající údaje o pozici satelitu ISS a informace o východu a západu slunce na pozici satelitu. 
Ze získaných údajů se vyhodnocuje jestli se satelit pohybuje nad osvětlenou části zeměkoule nebo nad temnou.
Skript toto oznamuje výpisem "Den" nebo "Noc".
V poslední řadě se vy skriptu vyhodnotí jestli je pozice satelitu vhodná pro pozorování. Pozice je vhodná pokud je satelit
nad zemským povrchem kdy v danné lokalitě je 60 až 120 před východem slunce nebo naopak 60 až 120 po západu slunce.
Je-li satelit na vhodné poloze je to oznámeno výpisem "Vhodna pozice pro pozorovani" naopak "Spatna pozice pro pozorovani".

#Spuštení

Pro spuštení je po potřeba mít naistalované následující balíčky: 
* request
* json
* datetime
* pytz

Skript se spouští příkazem 

```shell
python satelit.py
```
