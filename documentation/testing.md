# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Yksikkö- ja integraatiotestaus

### Database

The database is the most crucial test subject. It is being tested through the [database_test.py](https://github.com/ni-eminen/ReactComponentViewer/blob/main/ReactComponentViewer/src/tests/database_test.py) class, which creates a mock database utilizing the [database class](https://github.com/ni-eminen/ReactComponentViewer/blob/1673ee6c6c06e25db945c7dd3fba257648143737/ReactComponentViewer/src/database.py#L10). A test user is added before testing. Crucial functions such as adding and deleting of users and components is tested among other things.

### Utilities

Utilities are the two most important function of this project. They are tested in [util_test.py](https://github.com/ni-eminen/ReactComponentViewer/blob/main/ReactComponentViewer/src/tests/util_test.py). The most important one being render_component. render_component sends the user-written React component to the back-end, which then builds it into an actual React application that is then bundled into a single HTML file and returned. A delicate process, which can be tested by querying if the returned file is indeed an HTML file by doctype. The test itself is very short and can be found [here](https://github.com/ni-eminen/ReactComponentViewer/blob/1673ee6c6c06e25db945c7dd3fba257648143737/ReactComponentViewer/src/tests/util_test.py#L12).

### Testauskattavuus

Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haarautumakattavuus on 95%

![](./kuvat/testikattavuus.png)

Testaamatta jäivät _build.py_- ja _initialize_database.py_-tiedostojen suorittaminen komentoriviltä. Nämä olisi myös voinut jättää testikattavuuden ulkopuolelle. Lisäksi testaatamatta jäivät mm. tilanteet, joissa haetaan kirjautumattoman käyttäjän tekemättömät tehtävät ja uloskirjautuminen.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeen](./kayttoohje.md) kuvaamalla tavalla sekä macOS- että Linux-ympäristöön. Testauksessa on käytetty myös eri konfiguraatioita _.env_-tiedoston kautta.

Sovellusta on testattu sekä tilanteissa, joissa käyttäjät ja työt tallettavat tiedostot ovat olleet olemassa ja joissa niitä ei ole ollut jolloin ohjelma on luonut ne itse.

### Toiminnallisuudet

Kaikki [määrittelydokumentin](./vaatimusmaarittely.md#perusversion-tarjoama-toiminnallisuus) ja käyttöohjeen listaamat toiminnallisuudet on käyty läpi. Kaikkien toiminnallisuuksien yhteydessä on syötekentät yritetty täyttää myös virheellisillä arvoilla kuten tyhjillä.

## Sovellukseen jääneet laatuongelmat

Sovellus ei anna tällä hetkellä järkeviä virheilmoituksia, seuraavissa tilanteissa:

- Konfiguraation määrittelemiin tiedostoihin ei ole luku/kirjoitusoikeuksia
- SQLite tietokantaa ei ole alustettu, eli `python -m poetry run invoke build`-komentoa ei ole suoritettu
