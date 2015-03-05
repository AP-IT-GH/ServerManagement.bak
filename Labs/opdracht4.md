# 4. Data management en backup

## 4.1. Archiefbestanden
Maak vier tar archiefbestanden met daarin alle bestanden die in de volgende folder staan:
 *  ``/etc``
 *  ``/usr/bin``
 *  ``/usr/src``
 
Gebruik telkens een andere compressiemethode (pas hiervoor de nodige flags in je commando aan)
 * geen compressie
 * gzip compressie
 * bzip2 compressie
 * LZMA2/XZ compressie

Vergelijk voor deze archieven de volgende eigenschappen:
 * compressieratio
 * benodigde tijd om het bestand aan te maken

Let op dat je filesystem niet voor 100% gevuld geraakt. 
De beschikbare schijfruimte op je "koding.com" server is immers zeer beperkt. 

Meer info:
 * http://linux.die.net/man/1/tar
 * http://linux.die.net/man/1/time
 * http://linux.die.net/man/1/du
 * http://linux.die.net/man/1/df
 * http://tukaani.org/xz/

## 4.2. Off-site backup
Vraag om een user account op de server van een klasgenoot. Dit is de "backup server".

Kopieer je kleinste archiefbestand uit opgave 4.1 naar je "backup server" m.b.v. rsync.
Hiervoor heb je een account op de target server nodig.
Vraag dus aan je klasgenoot om een extra account voor je op zijn/haar server aan te maken.
Deze user moet zonder paswoord via ssh kunnen inloggen op de backup server om de backup automatisch vanuit een script uit te kunnen voeren.

Maak een shell script dat je aanroept via cron om deze backup iedere 10 minuten automatisch uit te voeren.

Werking script:
 * aanmaken archiefbestand
 * archiefbestand versturen naar "backup server"
 * archiefbestand terug wissen op je eigen systeem

Meer info:
 * http://linux.die.net/man/1/rsync
 * http://www.thegeekstuff.com/2008/11/3-steps-to-perform-ssh-login-without-password-using-ssh-keygen-ssh-copy-id/
 * http://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/

## 4.3. Syslog reporting

Schrijf de status van je backup weg naar de systeemlog. (``/var/log/messages``)

Voorbeeld: 
 * ``Wed  5 12:07:10 myservername logger: MyBackupScript Backup finished: file size 34 MB, duration 0m3.747s``
 * ``Wed  5 12:15:10 myservername logger: MyBackupScript Backup failed``

Laat je backup falen:
 * door er voor te zorgen dat je geen backupbestand kan wegschrijven op je eigen server. Een snelle manier om dat te doen is door tijdelijk geen write rechten te geven aan jezelf.
 * door naar een onbestaande/onbeschikbare server een backup te maken.

Meer info:
 * http://www.cyberciti.biz/tips/howto-linux-unix-write-to-syslog.html

### 4.4 E-Mail reporting
Stuur de inhoud van de laatste 10 lijnen in de syslog (``/var/log/messages``) via e-mail naar jezelf wanneer de backup faalt.

Meer info:
 * http://bernaerts.dyndns.org/linux/75-debian/278-debian-sendmail-gmail-account
 * http://learn.koding.com/guides/enable-php-mail-function/

## Verslag & evaluatie
Screenshots met onderstaande gegevens en een kort woordje uitleg om toe te lichten wat er in de screenshot te zien is.
 * Antwoorden op de vragen i.v.m. gecomprimeerde archieven
 * Shell script, screenshots en een woordje uitleg voor opgave 4.2, 4.3 en 4.4
 * Noteer voor elke opgave aan welke configuratie bestanden je hebt aangemaakt/aangepast
 
De upload link kan je op Blackboard terugvinden.
