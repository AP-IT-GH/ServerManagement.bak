# 4. Data management en backup

## 4.1. Archiefbestanden
Maak vier tar archiefbestanden met daarin alle bestanden die in de volgende folder staan:
 *  ``/etc``
 *  ``/usr/bin``
 *  ``/usr/src``
 
Gebruik telkens een andere compressiemethode
 * geen compressie
 * gzip compressie
 * bzip2 compressie
 * LZMA2 compressie

Vergelijk voor deze archieven de volgende parameters:
 * compressieratio
 * benodigde tijd om het bestand aan te maken

Let op dat je filesystem niet voor 100% gevuld geraakt. De beschikbare schijfruimte op je "koding.com" server is immers zeer beperkt. 

Meer info:
 * http://linux.die.net/man/1/tar
 * http://linux.die.net/man/1/time
 * http://linux.die.net/man/1/du
 * http://linux.die.net/man/1/df

## 4.2. Off-site backup
Vraag om een user account op de server van een klasgenoot. Dit is de "backup server".

Kopieer je kleinste archiefbestand naar je "backup server" m.b.v. rsync.

Maak een shell script dat je aanroept via cron om deze backup iedere 10 minuten automatisch uit te voeren.

Werking script:
 * aanmaken archiefbestand
 * archiefbestand versturen naar "backup server"

Meer info:
 * http://linux.die.net/man/1/rsync
 * http://www.thegeekstuff.com/2008/11/3-steps-to-perform-ssh-login-without-password-using-ssh-keygen-ssh-copy-id/
 * http://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/
 
## Verslag & evaluatie
Screenshots met onderstaande gegevens en een kort woordje uitleg om toe te lichten wat er in de screenshot te zien is.
 * Antwoorden op de vragen i.v.m. gecomprimeerde archieven
 * Shell script voor opgave 2
 * Screenshots + een woordje uitleg over opgave 2
 
De upload link kan je op Blackboard terugvinden.
