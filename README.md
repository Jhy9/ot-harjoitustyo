# Readme
Sovellus on sudokupeli, jota käyttäjä voi pelata. Käyttäjä voi myös lisätä uusia sudokuja ratkottavaksi.

## Asennus
1. Avaa komentorivillä projektin päähakemisto
2. Suorita komento 
```
poetry install
```
## Komentorivin komennot
### Käynnistys
Sovelluksen voi käynnistää komennolla
```
poetry run invoke start
```
### Pylint
Pylint-tarkastukset voi suorittaa komennolla
```
poetry run invoke lint
```
### Testit
Ohjelman testit voi suorittaa komennolla
```
poetry run invoke test
```
Testikattavuusraportin voi generoida komennolla
```
poetry run invoke coverage-report
```

## Linkit

[Changelog](dokumentaatio/changelog.md)

[Käyttöohje](dokumentaatio/kayttoohje.md)

[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

[Testausdokumentti](dokumentaatio/testaus.md)

[Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)

[Viikon 5 release](https://github.com/Jhy9/ot-harjoitustyo/releases/tag/viikko5)
