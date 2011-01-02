=============================
Enostavna Django kartografija
=============================

Uvod
----

Geodetska uprava RS daje na voljo nekatere `brezplačne podatke`_, ki jih lahko
prenesete prek spleta. Žal so ti podatki v surovi obliki nekoliko neuporabni;
delno zaradi formata (Shape datoteke), delno pa zaradi Slovenskega koordinatnega
sistema. Ta projekt skuša to težavo narediti trivialno premostljivo in stremi k
temu, da bi zmanjšalo tehnično znanje, ki je potrebno, da se ti podatki koristno
uporabijo.

Čeprav so podatki brezplačni, pa licenca in `pogoji uporabe`_ vsebujejo kar
nekaj pogojev, tako da si jih je potrebno prebrati in shraniti kopijo.

.. _`brezplačne podatke`: http://e-prostor.gov.si/index.php?id=263&no_cache=1&tx_simpltabs_pi1[tab]=561#tabs
.. _`pogoji uporabe`: http://e-prostor.gov.si/index.php?id=263&no_cache=1&tx_simpltabs_pi1[tab]=564#tabs

Opombe
------

Zaradi zgodovinskih zapletov ima Slovenija v PostGISu zaveden napačen
prostorski referenčni sistem. Sistem je sicer EPSG:3787 znan tudi kot MGI, ki
je po razpadu Avstro-Ogrske razpadel na dve inačici: Avstrija je privzela, da
se otok Hierro, ki specificira refernčni poldnevnik, nahaja na 17° 40′ 00″,
Madžarska in Jugoslavija pa sta privzeli, da ta otok leži na 17° 39′ 46”.
Ob tem je nastalo 14" sekund razlike, ta razlika pa se zdaj pri `uvozu podatkov
pravilno upošteva`_.

.. _`uvozu podatkov pravilno upošteva`: https://github.com/zejn/sigeo/blob/master/sigeo/preprocessing.py

Nastavitev projekta
-------------------

Nastavitev projekta je načeloma zelo podobna ostalim Django aplikacijam, v
kolikor boste sledili temu vrstnemu redu:

 1. git clone
 2. nastavitev podatkovne baze v settings.py (brez syncdb!)
 3. ./manage.py syncdb
 4. ./sigeo/manage.py sigeo_load_obcine OB.shp --drop
 5. ./manage.py runserver
 6.  obišči http://localhost:8000/obcine/

