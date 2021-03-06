# Minigolf

Tämä on simppeli 2D-versio minigolfista, joka on toteutettu Pythonilla.

Peli on Ohjelmistotekniikka-kurssiin kuuluva projektityö, joka kasvaa pikkuhiljaa kurssin edetessä.

Peli toimii Python-versiolla `3.6` tai uudemmalla.

## Lataa sovellus täältä

[Valmiin sovelluksen release](https://github.com/makeri89/Ohjelmistotekniikka/releases/tag/1.0.0)

## Dokumentaatio

- [Vaatimusmäärittely](vaatimusmaarittely)
- [Työaikakirjanpito](tyoaikakirjanpito)
- [Arkkitehtuurikuvaus](arkkitehtuuri)
- [Käyttöohje](kayttoohje)
- [Testausdokumentti](testaus)

## Asennus

1. Siirry komentorivillä minigolf-game kansioon

2. Asenna riippuvuudet komennolla

```
poetry install
```

3. Ensimmäisellä suorituskerralla alusta tietokanta tulosten tallennusta varten

```
poetry run invoke build
```

4. Käynnistä sovellus komennolla

```
poetry run invoke start
```

## Komentorivikomennot

### Ohjelman voi suorittaa komennolla

```
poetry run invoke start
```

### Ohjelman testit voi suorittaa komennolla

```
poetry run invoke test
```

### Testikattavuusraportin saa luotua komennolla

```
poetry run invoke coverage-report
```

tai selkeämmin luettava raportti

```
poetry run invoke coverage-html
```

Raportin saa avattua Firefox-selaimeen komennolla

```
poetry run invoke view-report
```

### Sovellukselle on myös määritelty pylint tarkistus komennolla

```
poetry run invoke lint
```
