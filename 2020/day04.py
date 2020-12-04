import pandas as pd
import re

def is_valid1(pw):
    required_keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    fields = dict([x.strip() for x in f.split(":")] for f in pw.strip().replace("\n"," ").split(" "))
    
    return all([(k in fields.keys()) for k in required_keys])

def is_valid2(pw):
    fields = dict([x.strip() for x in f.split(":")] for f in pw.strip().replace("\n"," ").split(" "))
    present = check_fields_present(fields)
    valid = check_fields_valid(fields)
    print("present", present, "valid", valid)
    return present and valid

def check_fields_present(fields):
    required_keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    return all([(k in fields.keys()) for k in required_keys])

def check_fields_valid(fields):
    return all([print_check_field_valid(key,value) for key, value in fields.items()])

def print_check_field_valid(key, value):
    ret = check_field_valid(key, value)
    if not ret:
        print([ret, key, value]) 
    return ret
    
def check_field_valid(key, value):
    if key == "byr":
        return int(value) >= 1920 and int(value) <= 2002
    elif key == "iyr":
        return int(value) >= 2010 and int(value) <= 2020
    elif key == "eyr":
        return int(value) >= 2020 and int(value) <= 2030
    elif key == "hgt":
        mval = value[:-2]
        unit = value[-2:]
        if unit == "cm":
            return int(mval) >= 150 and int(mval) <= 193
        elif unit == "in":
            return int(mval) >= 59 and int(mval) <= 76
        else:
            return False
    elif key == "hcl":
        return bool(re.match("^#[0-9a-f]{6}$", value))
    elif key == "ecl":
        return value in ["amb","blu","brn","gry","grn","hzl","oth"]
    elif key == "pid":
        return bool(re.match("^[0-9]{9}$", value))
    elif key == "cid":
        return True
    else:
        raise ValueError("invalid key " + key)

def is_valid_all1(inp):
    
    pws = inp.split("\n\n")
    
    return sum([int(bool(is_valid1(i))) for i in pws])

def is_valid_all2(inp):
    
    pws = inp.split("\n\n")
    
    return sum([int(bool(is_valid2(i))) for i in pws])

def print_csv(inp):
    
    pws = inp.split("\n\n")
    a = []

    for pw in pws:
        fields = dict([x.strip() for x in f.split(":")] for f in pw.strip().replace("\n"," ").split(" "))
        
        d = fields.copy()
        
        for k, v in fields.items():
            valid = check_field_valid(k,v)
            d[f"{k}_valid"] = valid

        a.append(d)

        d['present'] = check_fields_present(fields)
        d['all_valid'] = check_fields_valid(fields)
        

    pd.DataFrame(data=a).to_csv("data.csv")
    
        
               
test = open('inputs/day04.test').read()

output = is_valid_all1(test)
print(output)

#assert(output == 2)

test_invalid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

#assert(is_valid_all2(test_invalid) == 0)

test_valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

assert(is_valid_all2(test_valid) == 4)

real = open('inputs/day04').read()

#print("Part 1", is_valid_all1(real))
print("----")
print_csv(real)
print("Part 2", is_valid_all2(real))
