import csv
import re

with open("stran_2_direkt.html", encoding='utf8') as datoteka:
    vsebina = datoteka.read()

vzorec_bloka = re.compile(
    r'<a title="'
    r'<div class=\'wtrButtonContainer',
    flags=re.DOTALL
)

vzorec_knjige = re.compile(
    r'<a title="(?P<naslov>.*?)"'
    r'itemprop="name">(?P<avtor>.*?)<'
    r'published\s*(?P<leto>\d+)\s*'
    r'\s*(?P<st_ocen>\d+,\d+,?\d+?)\s*ratings'
    r'avg rating\s*(?P<ocena>\d\.\d+)\s*',
    flags=re.DOTALL
)

def izloci_podatke_knjige(blok):
    knjiga = vzorec_knjige.search(blok).groupdict()
    return knjiga

vzorec_avtor_id = r'/author/show/(\d+)\.\w*"><span itemprop="name">(.*?)<'
vzorec = r'avg rating\s*(?P<ocena>\d\.\d+)\s*'


with open('poskusni_obdelani.csv', 'w') as datoteka:
    writer = csv.writer(datoteka)
    writer.writerow(('id', 'avtor'))
    for ujemanje in re.finditer(vzorec, vsebina, re.DOTALL):
        print(ujemanje.group(1))
        #print((ujemanje.group(1), ujemanje.group(2)))
        #writer.writerow((ujemanje.group(1), ujemanje.group(2)))