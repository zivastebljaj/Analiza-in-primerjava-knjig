import re
import csv

vzorec_knjige = re.compile(
    r'setTargeting\("author",\s*\[(?P<avtor_id>.*?)\]\).*?'
    r'setTargeting\("shelf",\s*\[(?P<zanri>.*?)\]\).*?'
    r'rel="canonical" href="https://www.goodreads.com/book/show/(?P<id>\d+)\W.*?'
    r'Start by marking “(?P<naslov>.*?)” as.*?'
    r'<span itemprop="name">(?P<avtor>.*?)<.*?'
    r'itemprop="ratingValue">(?P<ocena>\d\.\d+)<.*?'
    r'<span class="votes value-title" title="(?P<st_ocen>\d+)">.*?' 
    r'<span class="count value-title" title="(?P<st_kritik>\d+)">.*?'
    r'<div class="row">\s*?Published\s*?.*?(?P<leto1>\d{4}).*?'
    r'\(f(irst published.*?(?P<leto2>\d{4})\))?',
    flags=re.DOTALL
)

vzorec_avtorja = re.compile(
    r'setTargeting\("author",\s*\[(?P<avtor_id>.*?)\]\).*?'
    r'<span itemprop="name">(?P<avtor>.*?)<.*?',
    flags=re.DOTALL
)

knjige = []
avtorji = []
for i in range(1, 3501):
    datoteka = (
        "C:\\Users\\Živa\\Desktop\\nalozene_knjige\\knjiga {}.html"
        ).format(i)
    with open(datoteka, encoding='utf8') as f:
        vsebina = f.read()
        for knjiga in re.finditer(vzorec_knjige, vsebina):
                knjiga = knjiga.groupdict()
                knjiga['zanri'] = knjiga['zanri'].replace('"', '').split(',')
                knjiga['ocena'] = float(knjiga['ocena'])
                knjiga['st_ocen'] = int(knjiga['st_ocen'])
                knjiga['st_kritik'] = int(knjiga['st_kritik'])
                if knjiga['leto2']:
                    knjiga['leto'] = int(knjiga['leto2'])
                else:
                    knjiga['leto'] = int(knjiga['leto1'])
                del knjiga['leto2']
                del knjiga['leto1']
                knjiga['avtor_id'] = int(knjiga['avtor_id'])
                knjiga['id'] = int(knjiga['id'])
                knjige.append(knjiga)
                print(i)
        for avtor in re.finditer(vzorec_avtorja, vsebina):
                avtor = avtor.groupdict()
                oznaka_avtorja = {
                    'id': int(avtor['avtor_id']),
                    'ime': avtor['avtor']
                    }
                if oznaka_avtorja not in avtorji:
                    avtorji.append(oznaka_avtorja)
print(len(knjige))



def izloci_zanre(seznam_knjig):
    zanri = []
    for knjiga in seznam_knjig:
        for zanr in knjiga.pop('zanri'):
            zanri.append({'knjiga': knjiga['id'], 'zanr': zanr})
    return zanri

with open('avtorji.csv', 'w', encoding='utf8') as csv_datoteka:
    writer = csv.DictWriter(csv_datoteka, ['id', 'ime'])
    writer.writeheader()
    for avtor in avtorji:
        writer.writerow(avtor)

with open('zanri.csv', 'w', encoding='utf8') as csv_datoteka:
    writer = csv.DictWriter(csv_datoteka, ['knjiga', 'zanr'])
    writer.writeheader()
    for knjiga in izloci_zanre(knjige):
        writer.writerow(knjiga)

with open('knjige.csv', 'w', encoding='utf8') as csv_datoteka:
    writer = csv.DictWriter(csv_datoteka, 
    ['id', 
    'naslov', 
    'avtor_id', 
    'avtor', 
    'leto', 
    'ocena', 
    'st_ocen', 
    'st_kritik']
    )
    writer.writeheader()
    for knjiga in knjige:
        writer.writerow(knjiga)
