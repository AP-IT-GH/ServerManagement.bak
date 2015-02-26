# Monitoring en logging

## Analyse logbestanden
Logbestanden vind je op Linux systemen terug in de map "/var/log".

In deze folder staan de logbestanden van verschillende services.
Voor enkele services kan je de bestanden in een aparte folder terugvinden. (bijv. 'apache2', 'mysql', 'squid',...)
Welke folders en bestanden hier beschikbaar zijn hangt af van de geïnstalleerde software op je systeem.

Jammer genoeg is er niet één exact formaat waarin alle logfiles worden neergeschreven, maar de meeste logbestanden volgen wel een relatief vast stramien qua naamgeving.

De meeste processen hebben een aantal verschillende logbestanden.
 * .err / error.log: foutmeldingen (fouten bij werking van een service, fouten bij opstarten,...)
 * .info / info.log: informatieve boodschappen (om te zien wat een service doet tijdens de normale werking)
 * .warn / warning.log: waarschuwingen

De recente logbestanden zijn steeds rechtstreeks te lezen als tekstbestand.
Als je systeem al een langere tijd actief is zullen er gecomprimeerde archieven van de oude logbestanden aangemaakt worden. (bijv. 'daemon.log.2.gz')
 * Meer info: http://www.debianhelp.co.uk/logwatch.htm
 
Meer info:
 * https://help.ubuntu.com/community/LinuxLogFiles
 * http://askubuntu.com/questions/186276/where-are-all-the-major-log-files-located
 
Zoek volgende informatie op in de logbestanden van je server.
Moesten deze events nog niet zijn opgetreden, doe dit dan even zelf of vraag aan een collega student om dit voor je te doen.
 * Wie heeft je website bezocht? (wanneer?, welke pagina's)
 * Wie heeft geprobeerd een niet-bestaande pagina op je website te openen?
 * Wanneer is de laatste login via ssh gebeurd?
 * Zijn er al pogingen tot inbraak op je systeem via ssh opgetreden? (een 'onbekende' die probeert je wachtwoord te raden)

## Live Monitoring tools
Installeer "htop", "iftop" en bekijk de activiteit van je systeem.

Genereer zelf een aantal events zodat de grafieken nuttige informatie tonen.
 * Verhoog CPU/RAM gebruik door een programma te draaien dat de CPU/RAM zwaar belast [cpu.py](/Software/cpu.py), [ram.py](/Software/ram.py)
 * Genereer internet trafiek door bestanden te downloaden. [download.py](/Software/download.py)

## Logging tools
Installeer Nagios en maak grafieken van:
 * CPU gebruik
 * RAM gebruik
 * Internet trafiek

Zorg er voor dat de grafieken voldoende informatie tonen.
Zorg er voor dat je machine niet wordt afgesloten door het volgende script in een aparte tab uit te voeren in de web interface. [awake.py](/Software/awake.py)

## DOS aanval
Werk met drie personen samen om een DOS aanval uit te voeren op één van je Apache servers.
Zorg er zo veel gelijktijdige dataconnecties naar de webserver worden geopend dat hij geen extra connecties meer zal toelaten.
Het gevolgd zal zijn dat de target server niet meer bereikbaar is.


## Verslag & evaluatie
Screenshots met onderstaande gegevens en een kort woordje uitleg om toe te lichten wat er in de screenshot te zien is.
 * Antwoorden op de vragen i.v.m. logbestanden (licht voor elke regel in twee zinnen toe waar de informatie staat en hoe je deze kan interpreteren)
 * Screenshot van htop en iftop met CPU/RAM/netwerk load
 * Screenshot van Nagios en iftop met CPU/RAM/netwerk load

De upload link kan je op Blackboard terugvinden.
