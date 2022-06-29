'''Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo imena + prezime. X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo iprezime@sum.ba). Od korisnika zatražiti unos maila i eduid te ispisati uspješnost. Istražiti greedy i non-greedy quantifiers.'''

import re

regex = "^k.*[0-5].*\s.*v$"
regex2 = "\s"

while 1:
    unos = input("Unesit ime: ")
    rezultat = re.search(regex and regex2, unos)
    print(rezultat)
    if rezultat:
        break
    else:
        print("Greška!") 

print("Točan unos!") 

