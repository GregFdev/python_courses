import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
#print(mo.group())

phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex2.search('My number is (415) 555-4242.')
#print(mo2.group(1))
#print(mo2.group(2))
#print(mo2.groups())

heroRegex = re.compile(r'(Batman)|(Tina Fey)')
# mo1 = heroRegex.search('Batman and Tina Fey')
# print(mo1.group())

mo2 = heroRegex.search('Batman and Tina Fey')
print(mo2.group(2))

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group())
