import re
import requests

link = "https://auto.bazos.cz"
response = requests.get(link)
bazos = response.text

print(bazos)
# Pattern = r"[A-Z]\.[A-Z]\.[A-Z]"

# patt2 = r"D"

# result = re.search(patt2, s)
# print(result)


#tasks -13 -#Task 13 - write the code. Ask if anything is unclear
#try - find all three-character abbreviations
#try - find all four-character abbreviations
#try - find all words that start with a capital letter
#extra - modify so that on https://auto.bazos.cz/ 
# we go through all the links and find how many km the cars 
# have driven there

pattern1 = r"[A-Z][A-Z][A-Z]"
pattern2 = r"[A-Z]{4}"
pattern3 = r"\b[A-Z].*?\b"

car_link_patt =  r"/inzerat[A-Za-z0-9/-]*"

km_patt = r"(Tachometr)+.*(\d[\d\s]*km)"

result1 = re.findall(pattern1, bazos)
print("result1=", result1)

result2 = re.findall(pattern2, bazos)
print("result2=",result2)

result3 = re.findall(pattern3, bazos)
print("result3=",result3)


#print(re.findall(car_link_patt, bazos))
for one_car_link in re.findall(car_link_patt, bazos):
    full_link = link + one_car_link + ".php"
    print(full_link)
    car_response = requests.get(full_link)
    car_text = car_response.text
    km_result = re.search(km_patt, car_text)
    if km_result:
        print(km_result)
    else:
        print(f" Error {full_link}")

   