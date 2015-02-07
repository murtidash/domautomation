#!/bin/bash

cd /var/dom4/savedgames/{{ game.servername }}

/var/dom4/scripts/turntrack.py
/var/dom4/scripts/makettweb.py

cp TurnT*.html /var/www/dom3/TurnTrack/

/var/dom4/scripts/ttindex.py

