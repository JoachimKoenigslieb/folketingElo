#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 22:35:26 2021

@author: joachim
"""


html = """<ul class="chosen-results" style="max-height: 180px;"><li class="active-result" data-option-array-index="1" style="">Adsbøl,
                        Karina (DF)
                      </li><li class="active-result" data-option-array-index="2" style="">Ahlers,
                        Tommy (V)
                      </li><li class="active-result" data-option-array-index="3" style="">Ahrendtsen,
                        Alex (DF)
                      </li><li class="active-result" data-option-array-index="4" style="">Ambo-Rasmussen,
                        Marlene (V)
                      </li><li class="active-result" data-option-array-index="5" style="">Ammitzbøll,
                        Katarina (KF)
                      </li><li class="active-result" data-option-array-index="6" style="">Ammitzbøll-Bille,
                        Simon Emil (UFG)
                      </li><li class="active-result" data-option-array-index="7" style="">Andersen,
                        Hans (V)
                      </li><li class="active-result" data-option-array-index="8" style="">Andersen,
                        Kirsten Normann (SF)
                      </li><li class="active-result" data-option-array-index="9" style="">Andersen,
                        Theresa Berg (SF)
                      </li><li class="active-result" data-option-array-index="10" style="">Bager,
                        Britt (V)
                      </li><li class="active-result" data-option-array-index="11" style="">Bank,
                        Heidi (V)
                      </li><li class="active-result" data-option-array-index="12" style="">Bech,
                        Lise (DF)
                      </li><li class="active-result" data-option-array-index="13" style="">Bek,
                        Kaare Dybvad (S)
                      </li><li class="active-result" data-option-array-index="14" style="">Bergman,
                        Birgitte (KF)
                      </li><li class="active-result" data-option-array-index="15" style="">Berthelsen,
                        Anne Valentina (SF)
                      </li><li class="active-result" data-option-array-index="16" style="">Bjerre,
                        Marie (V)
                      </li><li class="active-result" data-option-array-index="17" style="">Blixt,
                        Liselott (DF)
                      </li><li class="active-result" data-option-array-index="18" style="">Bonnesen,
                        Erling (V)
                      </li><li class="active-result" data-option-array-index="19" style="">Bramsen,
                        Trine (S)
                      </li><li class="active-result" data-option-array-index="20" style="">Brandenborg,
                        Bjørn (S)
                      </li><li class="active-result" data-option-array-index="21" style="">Bruus,
                        Jeppe (S)
                      </li><li class="active-result" data-option-array-index="22" style="">Bødskov,
                        Morten (S)
                      </li><li class="active-result" data-option-array-index="23" style="">Bøgsted,
                        Bent (DF)
                      </li><li class="active-result" data-option-array-index="24" style="">Carøe,
                        Astrid (SF)
                      </li><li class="active-result" data-option-array-index="25" style="">Christensen,
                        Peter Seier (NB)
                      </li><li class="active-result" data-option-array-index="26" style="">Christensen,
                        René (DF)
                      </li><li class="active-result" data-option-array-index="27" style="">Dahl,
                        Henrik (LA)
                      </li><li class="active-result" data-option-array-index="28" style="">Dahl,
                        Jens Henrik Thulesen (DF)
                      </li><li class="active-result" data-option-array-index="29" style="">Dahl,
                        Kristian Thulesen (DF)
                      </li><li class="active-result" data-option-array-index="30" style="">Dahlin,
                        Morten (V)
                      </li><li class="active-result" data-option-array-index="31" style="">Damsbo-Andersen,
                        Lennart (S)
                      </li><li class="active-result" data-option-array-index="32" style="">Danielsen,
                        Thomas (V)
                      </li><li class="active-result" data-option-array-index="33" style="">Dehnhardt,
                        Karina Lorentzen (SF)
                      </li><li class="active-result" data-option-array-index="34" style="">Dencker,
                        Mette Hjermind (DF)
                      </li><li class="active-result" data-option-array-index="35" style="">Dyhr,
                        Pia Olsen (SF)
                      </li><li class="active-result" data-option-array-index="36" style="">Elbæk,
                        Uffe (UFG)
                      </li><li class="active-result" data-option-array-index="37" style="">Elholm,
                        Louise Schack (V)
                      </li><li class="active-result" data-option-array-index="38" style="">Ellemann,
                        Karen (V)
                      </li><li class="active-result" data-option-array-index="39" style="">Ellemann-Jensen,
                        Jakob (V)
                      </li><li class="active-result" data-option-array-index="40" style="">Engelbrecht,
                        Benny (S)
                      </li><li class="active-result" data-option-array-index="41" style="">Espersen,
                        Søren (DF)
                      </li><li class="active-result" data-option-array-index="42" style="">Fabricius,
                        Camilla (S)
                      </li><li class="active-result" data-option-array-index="43" style="">Flydtkjær,
                        Dennis (DF)
                      </li><li class="active-result" data-option-array-index="44" style="">Frederiksen,
                        Claus Hjort (V)
                      </li><li class="active-result" data-option-array-index="45" style="">Frederiksen,
                        Mette (S)
                      </li><li class="active-result" data-option-array-index="46" style="">Fuglede,
                        Mads (V)
                      </li><li class="active-result" data-option-array-index="47" style="">Geertsen,
                        Martin (V)
                      </li><li class="active-result" data-option-array-index="48" style="">Gejl,
                        Torsten (ALT)
                      </li><li class="active-result" data-option-array-index="49" style="">Gjerskov,
                        Mette (S)
                      </li><li class="active-result" data-option-array-index="50" style="">Gottlieb,
                        Jette (EL)
                      </li><li class="active-result" data-option-array-index="51" style="">Halsboe-Jørgensen,
                        Ane (S)
                      </li><li class="active-result" data-option-array-index="52" style="">Hansen,
                        Eva Kjer (V)
                      </li><li class="active-result" data-option-array-index="53" style="">Hansen,
                        Niels Flemming (KF)
                      </li><li class="active-result" data-option-array-index="54" style="">Hav,
                        Orla (S)
                      </li><li class="active-result" data-option-array-index="55" style="">Hegaard,
                        Kristian (RV)
                      </li><li class="active-result" data-option-array-index="56" style="">Heitmann,
                        Jane (V)
                      </li><li class="active-result" data-option-array-index="57" style="">Henriksen,
                        Preben Bang (V)
                      </li><li class="active-result" data-option-array-index="58" style="">Heunicke,
                        Magnus (S)
                      </li><li class="active-result" data-option-array-index="59" style="">Hulgaard,
                        Egil (KF)
                      </li><li class="active-result" data-option-array-index="60" style="">Hummelgaard,
                        Peter (S)
                      </li><li class="active-result" data-option-array-index="61" style="">Hvelplund,
                        Peder (EL)
                      </li><li class="active-result" data-option-array-index="62" style="">Hækkerup,
                        Nick (S)
                      </li><li class="active-result" data-option-array-index="63" style="">Høegh-Dam,
                        Aki-Matilda (SIU)
                      </li><li class="active-result" data-option-array-index="64" style="">Hønge,
                        Karsten (SF)
                      </li><li class="active-result" data-option-array-index="65" style="">Haarder,
                        Bertel (V)
                      </li><li class="active-result" data-option-array-index="66" style="">Jakobsen,
                        Daniel Toft (S)
                      </li><li class="active-result" data-option-array-index="67" style="">Jarlov,
                        Rasmus (KF)
                      </li><li class="active-result" data-option-array-index="68" style="">Jelved,
                        Marianne (RV)
                      </li><li class="active-result" data-option-array-index="69" style="">Jensen,
                        Jacob (V)
                      </li><li class="active-result" data-option-array-index="70" style="">Jensen,
                        Kristian (V)
                      </li><li class="active-result" data-option-array-index="71" style="">Jensen,
                        Leif Lahn (S)
                      </li><li class="active-result" data-option-array-index="72" style="">Jensen,
                        Michael Aastrup (V)
                      </li><li class="active-result" data-option-array-index="73" style="">Jensen,
                        Mogens (S)
                      </li><li class="active-result" data-option-array-index="74" style="">Jensen,
                        Thomas (S)
                      </li><li class="active-result" data-option-array-index="75" style="">Jerkel,
                        Brigitte Klintskov (KF)
                      </li><li class="active-result" data-option-array-index="76" style="">Jerup,
                        Bruno (EL)
                      </li><li class="active-result" data-option-array-index="77" style="">Joel,
                        Jens (S)
                      </li><li class="active-result" data-option-array-index="78" style="">Joensen,
                        Edmund (SP)
                      </li><li class="active-result" data-option-array-index="79" style="">Johansen,
                        Jan (S)
                      </li><li class="active-result" data-option-array-index="80" style="">Juel-Jensen,
                        Peter (V)
                      </li><li class="active-result" data-option-array-index="81" style="">Juhl,
                        Christian (EL)
                      </li><li class="active-result" data-option-array-index="82" style="">Juul,
                        Mona (KF)
                      </li><li class="active-result" data-option-array-index="83" style="">Jørgensen,
                        Dan (S)
                      </li><li class="active-result" data-option-array-index="84" style="">Jørgensen,
                        Jan E. (V)
                      </li><li class="active-result" data-option-array-index="85" style="">Khader,
                        Naser (KF)
                      </li><li class="active-result" data-option-array-index="86" style="">Kidde,
                        Ruben (RV)
                      </li><li class="active-result" data-option-array-index="87" style="">Kissmeyer,
                        Carsten (V)
                      </li><li class="active-result" data-option-array-index="88" style="">Kjær,
                        Kasper Sand (S)
                      </li><li class="active-result" data-option-array-index="89" style="">Kjærsgaard,
                        Pia (DF)
                      </li><li class="active-result" data-option-array-index="90" style="">Knuth,
                        Marcus (KF)
                      </li><li class="active-result" data-option-array-index="91" style="">Knuth,
                        Stén (V)
                      </li><li class="active-result" data-option-array-index="92" style="">Kollerup,
                        Simon (S)
                      </li><li class="active-result" data-option-array-index="93" style="">Krag,
                        Astrid (S)
                      </li><li class="active-result" data-option-array-index="94" style="">Krarup,
                        Marie (DF)
                      </li><li class="active-result" data-option-array-index="95" style="">Kristensen,
                        Henrik Dam (S)
                      </li><li class="active-result" data-option-array-index="96" style="">Kronborg,
                        Anders (S)
                      </li><li class="active-result" data-option-array-index="97" style="">Kronborg,
                        Susan (RV)
                      </li><li class="active-result" data-option-array-index="98" style="">Langhoff,
                        Rasmus Horn (S)
                      </li><li class="active-result" data-option-array-index="99" style="">Larsen,
                        Malte (S)
                      </li><li class="active-result" data-option-array-index="100" style="">Larsen,
                        Per (KF)
                      </li><li class="active-result" data-option-array-index="101" style="">Larsen,
                        Aaja Chemnitz (IA)
                      </li><li class="active-result" data-option-array-index="102" style="">Larsson,
                        Tanja (S)
                      </li><li class="active-result" data-option-array-index="103" style="">Lauritzen,
                        Karsten (V)
                      </li><li class="active-result" data-option-array-index="104" style="">Laustsen,
                        Bjarne (S)
                      </li><li class="active-result" data-option-array-index="105" style="">Lidegaard,
                        Martin (RV)
                      </li><li class="active-result" data-option-array-index="106" style="">Lilleholt,
                        Lars Christian (V)
                      </li><li class="active-result" data-option-array-index="107" style="">Lind,
                        Annette (S)
                      </li><li class="active-result" data-option-array-index="108" style="">Lindgreen,
                        Stinus (RV)
                      </li><li class="active-result" data-option-array-index="109" style="">Lorentzen,
                        Kristian Pihl (V)
                      </li><li class="active-result" data-option-array-index="110" style="">Lund,
                        Rosa (EL)
                      </li><li class="active-result" data-option-array-index="111" style="">Lund,
                        Rune (EL)
                      </li><li class="active-result" data-option-array-index="112" style="">Løhde,
                        Sophie (V)
                      </li><li class="active-result" data-option-array-index="113" style="">Madsen,
                        Christian Rabjerg (S)
                      </li><li class="active-result" data-option-array-index="114" style="">Madsen,
                        Rasmus Vestergaard (EL)
                      </li><li class="active-result" data-option-array-index="115" style="">Mark,
                        Jacob (SF)
                      </li><li class="active-result" data-option-array-index="116" style="">Mathiesen,
                        Lars Boje (NB)
                      </li><li class="active-result" data-option-array-index="117" style="">Matthiesen,
                        Anni (V)
                      </li><li class="active-result" data-option-array-index="118" style="">Melson,
                        Christoffer Aagaard (V)
                      </li><li class="active-result" data-option-array-index="119" style="">Mercado,
                        Mai (KF)
                      </li><li class="active-result" data-option-array-index="120" style="">Messerschmidt,
                        Morten (DF)
                      </li><li class="active-result" data-option-array-index="121" style="">Mortensen,
                        Flemming Møller (S)
                      </li><li class="active-result" data-option-array-index="122" style="">Munk,
                        Signe (SF)
                      </li><li class="active-result" data-option-array-index="123" style="">Mølbæk,
                        Charlotte Broman (SF)
                      </li><li class="active-result" data-option-array-index="124" style="">Møller,
                        Henrik (S)
                      </li><li class="active-result" data-option-array-index="125" style="">Nawa,
                        Samira (RV)
                      </li><li class="active-result" data-option-array-index="126" style="">Nielsen,
                        Sofie Carsten (RV)
                      </li><li class="active-result" data-option-array-index="127" style="">Nordqvist,
                        Rasmus (SF)
                      </li><li class="active-result" data-option-array-index="128" style="">Nørby,
                        Ellen Trane (V)
                      </li><li class="active-result" data-option-array-index="129" style="">Oguz,
                        Halime (SF)
                      </li><li class="active-result" data-option-array-index="130" style="">Olesen,
                        Ole Birk (LA)
                      </li><li class="active-result" data-option-array-index="131" style="">Olldag,
                        Kathrine (RV)
                      </li><li class="active-result" data-option-array-index="132" style="">Paulin,
                        Anne (S)
                      </li><li class="active-result" data-option-array-index="133" style="">Pedersen,
                        Torsten Schack (V)
                      </li><li class="active-result" data-option-array-index="134" style="">Petersen,
                        Jesper (S)
                      </li><li class="active-result" data-option-array-index="135" style="">Petersen,
                        Rasmus Helveg (RV)
                      </li><li class="active-result" data-option-array-index="136" style="">Poulsen,
                        Søren Pape (KF)
                      </li><li class="active-result" data-option-array-index="137" style="">Poulsen,
                        Troels Lund (V)
                      </li><li class="active-result" data-option-array-index="138" style="">Prehn,
                        Rasmus (S)
                      </li><li class="active-result" data-option-array-index="139" style="">Rasmussen,
                        Lars Aslan (S)
                      </li><li class="active-result" data-option-array-index="140" style="">Rasmussen,
                        Lars Løkke (V)
                      </li><li class="active-result" data-option-array-index="141" style="">Rasmussen,
                        Søren Egge (EL)
                      </li><li class="active-result" data-option-array-index="142" style="">Ravn,
                        Troels (S)
                      </li><li class="active-result" data-option-array-index="143" style="">Robsøe,
                        Katrine (RV)
                      </li><li class="active-result" data-option-array-index="144" style="">Rod,
                        Lotte (RV)
                      </li><li class="active-result" data-option-array-index="145" style="">Rohde,
                        Jens (RV)
                      </li><li class="active-result" data-option-array-index="146" style="">Rosenkrantz-Theil,
                        Pernille (S)
                      </li><li class="active-result" data-option-array-index="147" style="">Roug,
                        Kasper (S)
                      </li><li class="active-result" data-option-array-index="148" style="">Schmidt,
                        Hans Christian (V)
                      </li><li class="active-result" data-option-array-index="149" style="">Siddique,
                        Sikandar (UFG)
                      </li><li class="active-result" data-option-array-index="150" style="">Skibby,
                        Hans Kristian (DF)
                      </li><li class="active-result" data-option-array-index="151" style="">Skipper,
                        Pernille (EL)
                      </li><li class="active-result" data-option-array-index="152" style="">Skovsby,
                        Julie (S)
                      </li><li class="active-result" data-option-array-index="153" style="">Skaale,
                        Sjúrður (JF)
                      </li><li class="active-result" data-option-array-index="154" style="">Skaarup,
                        Peter (DF)
                      </li><li class="active-result" data-option-array-index="155" style="">Stampe,
                        Zenia (RV)
                      </li><li class="active-result" data-option-array-index="156" style="">Steenberg,
                        Andreas (RV)
                      </li><li class="active-result" data-option-array-index="157" style="">Stoklund,
                        Rasmus (S)
                      </li><li class="active-result" data-option-array-index="158" style="">Strøjer-Schmidt,
                        Ina (SF)
                      </li><li class="active-result" data-option-array-index="159" style="">Støjberg,
                        Inger (V)
                      </li><li class="active-result" data-option-array-index="160" style="">Sølvhøj,
                        Jakob (EL)
                      </li><li class="active-result" data-option-array-index="161" style="">Søndergaard,
                        Søren (EL)
                      </li><li class="active-result" data-option-array-index="162" style="">Tesfaye,
                        Mattias (S)
                      </li><li class="active-result" data-option-array-index="163" style="">Thiesen,
                        Mette (NB)
                      </li><li class="active-result" data-option-array-index="164" style="">Torp,
                        Trine (SF)
                      </li><li class="active-result" data-option-array-index="165" style="">Tørnæs,
                        Ulla (V)
                      </li><li class="active-result" data-option-array-index="166" style="">Valentin,
                        Carl (SF)
                      </li><li class="active-result" data-option-array-index="167" style="">Valentin,
                        Kim (V)
                      </li><li class="active-result" data-option-array-index="168" style="">Vanopslagh,
                        Alex (LA)
                      </li><li class="active-result" data-option-array-index="169" style="">Velasquez,
                        Victoria (EL)
                      </li><li class="active-result" data-option-array-index="170" style="">Vermund,
                        Pernille (NB)
                      </li><li class="active-result" data-option-array-index="171" style="">Villadsen,
                        Mai (EL)
                      </li><li class="active-result" data-option-array-index="172" style="">Vind,
                        Birgitte (S)
                      </li><li class="active-result" data-option-array-index="173" style="">Vinther,
                        Henrik (RV)
                      </li><li class="active-result" data-option-array-index="174" style="">Wammen,
                        Nicolai (S)
                      </li><li class="active-result" data-option-array-index="175" style="">Wermelin,
                        Lea (S)
                      </li><li class="result-selected" data-option-array-index="176" style="">Zimmer,
                        Susanne (UFG)
                      </li><li class="active-result" data-option-array-index="177" style="">Øktem,
                        Fatma (V)
                      </li><li class="active-result" data-option-array-index="178" style="">Østerby,
                        Orla (UFG)
                      </li><li class="active-result" data-option-array-index="179" style="">Østergaard,
                        Anne Honoré (V)
                      </li></ul>"""
                      
import bs4 as bs
import string
import requests

soup = bs.BeautifulSoup(html)
names = [tag.text.strip() for tag in soup.find_all('li')]

whitespace = [' ', '\n']
f = lambda x: ''.join([c for c in x if c not in whitespace])
names = [f(tag) for tag in names]

def get_url(name):
    name = name[:name.find('(')]
    
    name = name.replace('æ', 'ae')
    name = name.replace('ø', 'oe')
    name = name.replace('å', 'aa')
    
    last, first = name.split(',')
    uppers = string.ascii_uppercase
    upper_splits = []
    if first[1:].lower() != first[1:]:
        for i, c in enumerate(first):
            if c in uppers:
                upper_splits.append(i)
                
    first_fixed = [first[i:j].lower() for i,j in zip(upper_splits[:-1], upper_splits[1:])]
    if upper_splits: 
        first_fixed.append(first[upper_splits[-1]:].lower())
    else:
        first_fixed = [first.lower()]
        
    url_name = '-'.join(first_fixed + [last.lower()])
    
    url = f'https://www.ft.dk/medlemmer/mf/{url_name[0]}/{url_name}'
    return url
    
urls = [get_url(name) for name in names]

def get_img(url):
    r = requests.get(f'{url}')
    soup = bs.BeautifulSoup(r.text)
    image_link = soup.find('img', class_='bio-image').attrs['src']
    r = requests.get(image_link)
    return f'{"/".join(image_link.split("/")[:-1])}/{r.headers["Content-Disposition"].split(";")[-1][11:-1]}'

def download_image(url):
    download_link = get_img(url)
    img = requests.get(download_link)
    name = url.split('/')[-1]
    
    file = open(f"{name}.jpg", "wb")
    file.write(img.content)
    file.close()

for url in urls:
    try:
        download_image(url)
    except:
        print(url)