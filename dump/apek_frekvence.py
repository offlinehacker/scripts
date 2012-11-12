#!/usr/bin/python
import urllib2
import json
import itertools
import csv

def get_page(page, url):
    response= urllib2.urlopen(url% page)
    data= json.load(response)

    return data

def get_data(url, count):
    merged=[]
    for x in range(1,count):
        data= get_page(x, url)
        if not data:
            break

        merged+= data

    return merged

def write_data(filename, data):
    with open(filename, 'wb') as csvfile:
        csvwriter = csv.DictWriter(csvfile, sorted(set([i for d in data for i in d.keys()]))
                                   , extrasaction='ignore')
        csvwriter.writeheader()

        enc= lambda v: unicode(v).encode('utf-8') if v else None

        for d in data:
            csvwriter.writerow({k:enc(v) for k,v in d.items()})

if __name__ == "__main__":
    # all radio and tv frequencies
    data= get_data("http://www.apek.si/ra-in-tv-frekvence?page=%d&jezik=sl&search=izvoz&vrsta_postaje=vsi&imetnik=-1&ime_programa_radio=-1&mrezni_program_radio=-1&oddajne_tocke_radio=-1&timesharing_radio=-1&ime_programa_sr_val=-1&timesharing_sr_val=-1&obmocje_pokrivanja_dvb_t=-1&type=json&modul=RAinTV&sort=st_odlocbe&direction=ASC", 2 )
    write_data("radio_tv_freqs.csv", data)
    # all non radio and tv frequencies
    data= get_data("http://www.apek.si/frekvence?page=%d&search=izvoz&jezik=sl&imetnik=-1&stevilka_odlocbe=&rk_storitev=vse&lokacija=&oddajna_frekvenca_od=&oddajna_frekvenca_do=&sprejemna_frekvenca_od=&sprejemna_frekvenca_do=&enota=enota&registracija_lt=-1&klicni_znak_ld=-1&registracija_ld=-1&mmsi_stevilka=&type=json&modul=Frekvence&sort=imetnik&direction=ASC", 20 )
    write_data("freqs.csv", data)
