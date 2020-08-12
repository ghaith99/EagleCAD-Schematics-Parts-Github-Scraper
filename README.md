# EagleCAD Schematics Parts Github Scraper

- Frequency analysis of parts used in EagleCAD schematics. 
- 1300+ schematics sheets from Sparkfun + Adafruit collected. 
- Will ignore KiCAD sch files
- XML Parts tags are parsed and stored in csv file in the same folder
- Following part's values are colleted:
    - library
    - deviceset
    - device
    - value

**Usage**

```main.py -c <count_per_page> -p <page> -o <organization>```

***Example***

```main.py -c 10 -p 20 -o sparkfun```




