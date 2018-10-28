import requests
import os



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


for i in range(1, 26):
    page_url = 'https://www.goodreads.com/shelf/show/fiction?page={}'.format(i)
    text = download_url_to_string(page_url)
    directory = 'nalozene_strani'
    filename = 'stran{}.html'.format(i)
    save_string_to_file(text, directory, filename)
