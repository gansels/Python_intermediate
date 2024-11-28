#Tasks_12_Generator


# vytvorite generator, ktery bude postupne vracet
# Albert - mame koncovku "bert"
# pred tu koncovku budou davany predpany "Al", "Ro",
# "Hu", "Nor", "Gil"

def Generator_jmeno(pred, konc):
    for i in pred:
        yield i + konc


predpony = ["Ga", "Di", "Ja", "Ho", "Vigh"] #predpony-prefix
koncovka = "nesh" # koncovka- suffix
for jmeno in Generator_jmeno(predpony, koncovka):
    print(f" Tve jmeno je {jmeno}")