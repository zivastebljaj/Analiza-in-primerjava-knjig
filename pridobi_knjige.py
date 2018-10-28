import os
import requests
import re

def download_url_to_string(url):
    '''This function takes a URL as argument and tries to download it
    using requests. Upon success, it returns the page contents as string.'''
    try:
        # del kode, ki morda sproži napako
        r = requests.get(url)     
    except requests.exceptions.ConnectionError:
        # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        print('stran ne obstaja')
        return None
    # nadaljujemo s kodo če ni prišlo do napake
    else:
        return r.text

def save_string_to_file(text, directory, filename):
    '''Write "text" to the file "filename" located in directory "directory",
    creating "directory" if necessary. If "directory" is the empty string, use
    the current directory.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None

koncnice = []
datoteka = 'stran.html'
with open (datoteka, encoding='utf-8') as f:
    vsebina = f.read()
    vzorec = '<a class="bookTitle" href="/book/show/(.*?)">'
    koncnice += re.findall(vzorec, vsebina)

stevec = 1
for knjiga in koncnice:
    page_url = 'https://www.goodreads.com/book/show/{}'.format(knjiga)
    text = download_url_to_string(page_url)
    directory = 'knjige'
    filename = 'knjiga {}.html'.format(stevec)
    save_string_to_file(text, directory, filename)
    stevec +=1

