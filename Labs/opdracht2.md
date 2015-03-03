# 2. Basis webserver

## Registratie Koding.com
Maak een account aan op de website: "koding.com" (moest je dat nog niet gedaan hebben in opgave 1)

## 2.1. Updates
Installeer alle beschikbare updates voor de reeds geïnstalleerde software packages op je systeem:
 * ``aptitude update``
 * ``aptitude upgrade``

Doe dit best bij aanvang van elk labo en ook steeds wanneer je software installeert.
Hierdoor voorkom je eventuele problemen veroorzaakt door conflicterende software versies.

### dpkg-reconfigure
Indien je problemen tegenkoment omdat een bepaalde package niet correct geinstalleerd is kan je deze met dpkg-reconfigure oplossen.
Dit is nodig wanneer de package manager is in een error-state afgesloten werd.

Meer info:
 * http://www.linux-magazine.com/Issues/2013/155/Command-Line-dpkg-reconfigure

## 2.2. Firewall
Installeer en configureer de firewall op je machine: http://learn.koding.com/guides/enable-ufw/

Laat volgende services toe:
 * secure shell: zodat je later via ssh kan inlogggen
 * webserver: http en https
 * FTP server

Zorg er voor dat je alleen via ssh kan inloggen via locaties waar je zelf vaak komt:
 * op onze campus (AP-wifi en eduroam)
 * via je internetverbinding thuis (zoek op welke IP ranges je provider gebruikt)

## 2.3 Secure shell
Log op je server in via secure shell: http://learn.koding.com/guides/ssh-into-your-vm/

Gebruik hiervoor Cygwin of MobaXterm.

## 2.4. FTP: ProFTPd
Installeer ProFTPd met behulp van apt-get: http://learn.koding.com/guides/setting-up-ftp-on-koding/
 * Maak drie user accounts aan om via FTP bestanden te uploaden: 'blog', 'tandarts', 'webshop'
 * Zorg er voor dat deze drie users een aparte folder op je systeem hebben waar ze documenten kunnen uploaden.

## 2.5. Configuratie Apache
Configureer drie subdomeinen zodat je via volgende url's naar drie verschillende websites kan gaan.
 * blog.username.koding.io
 * tandarts.username.koding.io
 * webshop.username.koding.io
Maak deze websites aan door via FTP enkele HTML bestanden te uploaden.

Meer info: http://learn.koding.com/guides/vhosts-and-subdomains/

## Verslag & evaluatie
Screenshots met onderstaande gegevens en een kort woordje uitleg om toe te lichten wat er in de screenshot te zien is.
 * Overzicht van je firewall rules (licht voor elke regel in één zin toe waarvoor hij dient)
 * Werkende SSH toegang
 * Werkende FTP toegang
 * De drie websites

De upload link kan je op Blackboard terugvinden.