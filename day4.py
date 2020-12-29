
class passport_data(object):

    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid





f = open('day4input.txt', 'r')
content = f.read()
passports = content.split("\n\n")
cleaned_passports = []
for passport in passports:
    passport = passport.replace("\n", " ").replace(" ", ",")
    entry = passport.split(",")
    passport_dict = {}
    for pair in entry:
        details = pair.split(":")
        passport_dict[details[0]] = details[1]
    cleaned_passports.append(passport_dict)



fail = 0
for passport in cleaned_passports:
    if len(passport) < 7:
        fail += 1
    if len(passport) == 7:
        if "cid" in passport:
            fail += 1

valid = len(cleaned_passports) - fail
print(valid)

print(len(cleaned_passports))