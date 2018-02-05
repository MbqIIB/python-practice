#!/usr/bin/python
# import string
# frm = ''
# to = ''
# trans = string.maketrans(frm,to)
# print trans


# from string import maketrans
#
# intab = 'aeiou'
# outtab = '12345'
# trantab = maketrans(intab,outtab)
# print trantab


import string
def translator(frm = '',to = '',delete = '',keep = None):
    if len(to) == 1:
        to = to * len(frm)
    trans = string.maketrans(frm,to)
    if keep is not None:
        allchars = string.maketrans('','')
        delete = allchars.translate(allchars,keep.translate(allchars,delete))
    def test(s):
        return s.translate(trans,delete)
#    def translate(s):
#       return s.translate(trans,delete)
    return test

digites_only = translator(keep = string.digits)
q = digites_only("chris perkins:233-2346")


digites_twice = translator(keep = string.digits)

print  digites_only == digites_twice



