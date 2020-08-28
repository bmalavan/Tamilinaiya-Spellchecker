#!/usr/bin/env python3

import tamil


# reference - https://thanithamizhakarathikalanjiyam.github.io/windows_283
start_letters = [
 'அ','ஆ','இ','ஈ','உ','ஊ','எ','ஏ','ஐ','ஒ','ஓ','ஔ',
 'க','கா','கி','கீ','கு','கூ','கெ','கே','கை','கொ','கோ','கௌ','ங',
 'ச','சா','சி','சீ','சு','சூ','செ','சே','சை','சொ','சோ','சௌ','ஞ',
 'ஞா','ஞெ','ஞொ','த','தா','தி','தீ','து','தூ','தெ','தே','தை','தொ',
 'தோ','தௌ','ந','நா','நி','நீ','நு','நூ','நெ','நே','நை','நொ','நோ',
 'நௌ','ப','பா','பி','பீ','பு','பூ','பெ','பே','பை','பொ','போ','பௌ',
 'ம','மா','மி','மீ','மு','மூ','மெ','மே','மை','மொ','மோ','மௌ','ய',
 'யா','யு','யூ','யோ','யௌ','வ','வா','வி','வீ','வெ','வே','வை','வௌ'
]

end_letters = [
'ஆ','ஈ','ஊ','ஏ','ஐ','ஓ','ஔ','இ','உ','எ','ஒ',
'க','கா','கி','கீ','கு','கூ','கே','கை','கோ','கௌ',
'ங','ஙா','ஙி','ஙீ','ஙு','ஙூ','ஙே','ஙை','ஙோ','ச',
'சா','சி','சீ','சு','சூ','சே','சை','சோ','ஞ்','ஞ','ஞா',
'ஞி','ஞீ','ஞு','ஞூ','ஞே','ஞை','ஞோ','ட','டா','டி',
'டீ','டு','டூ','டே','டை','டோ','ண்','ண','ணா','ணி',
'ணீ','ணு','ணூ','ணே','ணை','ணோ','த','தா','தி',
'தீ','து','தூ','தே','தை','தோ','ந்','ந','நா','நி','நீ',
'நு','நூ','நே','நை','நொ','நோ','ப','பா','பி','பீ','பு',
'பூ','பே','பை','போ','ம்','ம','மா','மி','மீ','மு','மூ',
'மே','மை','மோ','ய்','ய','யா','யி','யீ','யு','யூ','யே',
'யை','யோ','ர்','ர','ரா','ரி','ரீ','ரு','ரூ','ரே','ரை',
'ரோ','ல்','ல','லா','லி','லீ','லு','லூ','லே','லை','லோ',
'வ்','வ','வா','வி','வீ','வு','வூ','வே','வை','வோ','வௌ',
'ழ்','ழ','ழா','ழி','ழீ','ழு','ழூ','ழே','ழை','ழோ','ள்','ள',
'ளா','ளி','ளீ','ளு','ளூ','ளே','ளை','ளோ','ற','றா','றி',
'றீ','று','றூ','றே','றை','றோ','ன்','ன','னா','னி','னீ',
'னு','னூ','னே','னை','னோ'
]


def check_first_letter(word):

    letters = tamil.utf8.get_letters(word)

    if letters[0] in start_letters:
        return True
    else:
        return False
    


def check_last_letter(word):

    letters = tamil.utf8.get_letters(word)

    if letters[-1] in end_letters:
        return True
    else:
        return False

print(check_first_letter("நன்றி"))
print(check_last_letter("நன்றி"))