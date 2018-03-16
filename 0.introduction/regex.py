'''
extract morphemes and labels from morphological analysis
'''

import re

words = [
    'ettirilmesinden  (ed)et  +Verb(+dHr)^DB+Verb+Caus(+Hl)^DB+Verb+Pass+Pos(+mA)^DB+Noun+Inf2+A3sg(+sH)+P3sg(+ndAn)+Abl',
    'geliştirici    (gel)gel    +Verb(+HS)^DB+Verb+Recip(+dHr)^DB+Verb+Caus+Pos(+yHcH)^DB+Adj+Agt',
    'geliştirici (gel)gel    +Verb(+HS)^DB+Verb+Recip(+dHr)^DB+Verb+Caus+Pos(+yHcH)^DB+Noun+Agt+A3sg+Pnon+Nom',
    'geliştirici (geliS)geliş+Verb(+dHr)^DB+Verb+Caus+Pos(+yHcH)^DB+Adj+Agt',
    'geliştirici (geliS)geliş+Verb(+dHr)^DB+Verb+Caus+Pos(+yHcH)^DB+Noun+Agt+A3sg+Pnon+Nom',
]


for w in words:

    tmp = w.split()
    word, analysis = tmp[0], ''.join(tmp[1:])
    print(word)
    print(analysis)

    morphemes = ''.join([m.strip('(').strip(')')
                         for m in
                         re.findall('\([^)]*\)', analysis)])
    print(morphemes)

    tags = re.sub('\([^)]*\)', '', analysis)
    print(tags)
    print()
