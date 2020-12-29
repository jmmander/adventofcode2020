import re
import traceback


class Passport(object):

    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self._cid = cid

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    @property
    def byr(self):
        return self._byr

    @byr.setter
    def byr(self, value):
        if len(value) == 4 and (1920 <= int(value) <= 2002):
            self._byr = value
        else:
            raise ValueError("invalid byr")

    @property
    def iyr(self):
        return self._iyr

    @iyr.setter
    def iyr(self, value):
        if len(value) == 4 and (2010 <= int(value) <= 2020):
            self._iyr = value
        else:
            raise ValueError("invalid iyr")

    @property
    def eyr(self):
        return self._eyr

    @eyr.setter
    def eyr(self, value):
        if len(value) == 4 and (2020 <= int(value) <= 2030):
            self._eyr = value
        else:
            raise ValueError("invalid eyr")

    @property
    def hgt(self):
        return self._hgt

    @hgt.setter
    def hgt(self, value):
        pattern = r'^\d+cm$|^\d+in$'
        valid = re.match(pattern, value)
        if valid:
            items = re.findall(r'[^\W\d_]+|\d+', value)
            num = int(items[0])
            unit = items[1]
            if unit == "cm":
                valid = 150 <= num <= 193
            else:
                valid = 59 <= num <= 76
        if valid:
            self._hgt = value
        else:
            raise ValueError("invalid hgt")

    @property
    def hcl(self):
        return self._hcl

    @hgt.setter
    def hcl(self, value):
        pattern = r'^#[a-f0-9]{6}$'
        valid = re.match(pattern, value)
        if valid:
            self._hcl = value
        else:
            raise ValueError("invalid hcl")

    @property
    def ecl(self):
        return self._ecl

    @ecl.setter
    def ecl(self, value):
        if value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            self._ecl = value
        else:
            raise ValueError("invalid ecl")

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        if len(value) == 9:
            self._ecl = value
        else:
            raise ValueError("invalid pid")

    @property
    def cid(self):
        return self._cid


f = open('day4input.txt', 'r')
content = f.read()
passports = content.split("\n\n")
cleaned_passports = []
index = 0
passports_numbered = {}


# part one
for passport in passports:
    passport = passport.replace("\n", " ").replace(" ", ",")
    entry = passport.split(",")
    passport_dict = {}
    for pair in entry:
        details = pair.split(":")
        passport_dict[details[0]] = details[1]
    cleaned_passports.append(passport_dict)

for passport in cleaned_passports:
    if len(passport) < 7:
        fail += 1
    if len(passport) == 7:
        if "cid" in passport:
            fail += 1

valid = len(cleaned_passports) - fail


#part 2
for passport in passports:
    passport = passport.replace("\n", " ").replace(" ", ",")
    entry = passport.split(",")
    passport_dict = {}
    for pair in entry:
        details = pair.split(":")
        passport_dict[details[0]] = details[1]
    try:
        passport_obj = Passport(**passport_dict)
    except ValueError as err:
        #print(traceback.format_exc())
        continue
    except TypeError as err:
        #print(traceback.format_exc())
        continue
    passports_numbered[index] = passport_obj
    index += 1

total_valid = len(passports_numbered)
