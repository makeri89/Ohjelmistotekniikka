# Minigolf

Tämä on simppeli 2D-versio minigolfista, joka on toteutettu Pythonilla.

Peli on Ohjelmistotekniikka-kurssiin kuuluva projektityö, joka kasvaa pikkuhiljaa kurssin edetessä.

Peli toimii Python-versiolla `3.6` tai uudemmalla.

### Dokumentaatio

- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](/dokumentaatio/tyoaikakirjanpito.md)
- [Arkkitehtuurikuvaus](/dokumentaatio/arkkitehtuuri.md)

### Asennus

1. Siirry komentorivillä minigolf-game kansioon

2. Asenna riippuvuudet komennolla

```
poetry install
```

3. Käynnistä sovellus komennolla

```
poetry run invoke start
```

Pelin päävalikosta voi aloittaa uuden pelin myös edellisen pelin päätyttyä, mutta menu toimii tällä hetkellä vasta muutaman sekunnin viiveellä pelin päättymisestä.

### Komentorivikomennot

#### Ohjelman voi suorittaa komennolla

```
poetry run invoke start
```

#### Ohjelman testit voi suorittaa komennolla

```
poetry run invoke test
```

#### Testikattavuusraportin saa luotua komennolla

```
poetry run invoke coverage-report
```

tai selkeämmin luettava raportti

```
poetry run invoke coverage-html
```

#### Sovellukselle on myös määritelty pylint tarkistus komennolla

```
poetry run invoke lint
```
