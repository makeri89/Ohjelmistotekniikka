# Vaatimusmäärittely

## Sovelluksen tarkoitus

Käyttäjä voi pelata simppeliä 2D-minigolfia, joka on ulkonäöltään jo alasajetun Aapeli-pelisivuston Minigolfin kaltainen.

## Pelaajat

Peliä voi pelata yksinpelinä eli pelin tavoite on ainoastaan saada pallo reikään mahdollisimman vähillä lyönneillä. Peliin voidaan myöhemmin lisätä mahdollisuus pelata joko tietokonetta tai toista pelaajaa vastaan.

## Pelin erilaiset komponentit

Pelikentiltä voi löytyä seuraavia elementtejä:

- ruohoa
- vettä
- hiekkaa
- seinäesteitä

## Toiminnallisuus

Pelaaja voi

- asettaa itselleen peliin nimimerkin ✔️
- pelata pelin minigolfia ✔️
- vaihtaa pallonsa väriä ✔️
- tarkastella aiempia tuloksiaan eri kentillä
  - pelin tulokset tallentuvat tietokantaan ✔️
  - pelattuja pelejä tietokannassa saa tarkasteltua ✔️
  - tietyn pelaajan tuloksia saa tarkasteltua ✔️
  - tietyn kentän tuloksia saa tarkasteltua ✔️
  - tuloksien tarkastelu onnistuu graafisella käyttöliittymällä ✔️

Elementtien vaikutukset palloon

- vesi palauttaa pallon lyöntipaikkaan ✔️
- seinästä pallo kimpoaa poispäin ✔️
- hiekka hidastaa palloa
  - vaalea hiekka hidastaa vähän ✔️
  - tumma hiekka hidastaa enemmän ✔️

## Jatkokehitysideoita

Kun pelin perusversio yksinpelillä on saatu toimivaksi, voidaan peliä laajentaa lisäämällä siihen esimerkiksi

- moninpeli
- mahdollisuus omien tasojen luomiseen pelaajille
- mahdollisuus eri vaikeustason kenttäkokonaisuuksien pelaamiseen
- turnaukset
- 3D pinnanmuotojen jäljittely hitaiden ja nopeiden osuuksien avulla
