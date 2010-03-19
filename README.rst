=============================
Enostavna Django kartografija
=============================

Uvod
----

Geodetska uprava RS daje na voljo nekatere `brezplacne podatke`_, ki jih lahko
prenesete prek spleta. Zal so ti podatki v surovi obliki nekoliko neuporabni;
delno zaradi formata (Shape datoteke), delno pa zaradi Slovenskega koordinatnega
sistema. Ta projekt skusa to tezavo narediti trivialno premostljivo in stremi k
temu, da bi zmanjsalo tehnicno znanje, ki je potrebno, da se ti podatki koristno
uporabijo.

Ceprav so podatki brezplacni, pa so licenca in `pogoji uporabe`_ vsebujejo kar
pogojev, tako da si jih je potrebno prebrati in shraniti kopijo.

.. _`brezplacne podatke`: http://e-prostor.gov.si/index.php?id=263&no_cache=1&tx_simpltabs_pi1[tab]=561#tabs
.. _`pogoji uporabe`: http://e-prostor.gov.si/index.php?id=263&no_cache=1&tx_simpltabs_pi1[tab]=564#tabs

Opombe
------

Slovenija ima svoj koordinatni sistem, ki je v primerjavi z WGS 84 (GPS, SRID
4326) koordinatami zamaknjen za priblizno 1 sekundo in 17 sekund po drugi osi.
To so priblizne stevilke, prave enacbe pa se nimam. Če jo poznas, prosim
pomagaj.

Nastavitev projekta
-------------------

Nastavitev projekta je naceloma zelo podobna ostalim Django aplikacijam, v
kolikor boste sledili temu vrstnemu redu:

 1. git clone
 2. nastavitev podatkovne baze v settings.py (brez syncdb!)
 3. ./sigeo/shp2sql.sh OB.shp > obcine.sql
 4. psql dbname < obcine.sql
 5. ./manage.py sigeo_sync_srid
 6. ./manage.py syncdb
 7. ./manage.py runserver
 8.  obisci http://localhost:8000/obcine/

