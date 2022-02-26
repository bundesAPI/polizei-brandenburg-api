# Polizei Brandenburg API

Nachrichten, Hochwasser-, Verkehrs- und Waldbrandwarnungen der Polizei Brandenburg.


## Pegelstände

**URL:** https://polizei.brandenburg.de/ipa_api/pegel/version/1
	
Die API ermöglicht Zugriff auf aktuelle Pegelstände unterschiedlicher Gewässer über einen einfachen GET-request.


## Nachrichten und Suchmeldungen

**URL:** https://polizei.brandenburg.de/ipa_api/news/version/1
	
Die API ermöglicht Zugriff auf aktuelle Nachrichten und Suchmeldungen der Polizei Brandenburg, gefiltert über folgende GET-Parameter:


**Parameter:** *count* (Optional)

Anzahl angefragter Ergebnisse (z.B. 5000)


**Parameter:** *category* (Optional)

Kategorie (z.B. 8).


**Parameter:** *district* (Optional)

Distrikt (z.B. 500).


## Reviere

**URL:** https://polizei.brandenburg.de/ipa_api/reviere/version/1

Die API ermöglicht Zugriff auf eine Liste aller Reviere der Polzei Brandenburg über einen einfachen GET-request.


## Verkehrswarnungen

**URL:** https://polizei.brandenburg.de/ipa_api/vwd/version/1

Die API ermöglicht Zugriff auf aktuelle Verkehrswarnungen der Polzei Brandenburg über einen einfachen GET-request.


## Waldbrandwarnungen

**URL:**  https://polizei.brandenburg.de/ipa_api/waldbrand/version/1

Die API ermöglicht Zugriff auf aktuelle Waldbrandwarnungen in Brandenburg über einen einfachen GET-request.


## Beispiel

```bash
news=$(curl -m 60 'https://polizei.brandenburg.de/ipa_api/news/version/1?count=10')
```
