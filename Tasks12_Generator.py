#Tasks_12_Generator


# vytvorite generator, ktery bude postupne vracet
# Albert - mame koncovku "bert"
# pred tu koncovku budou davany predpany "Al", "Ro",
# "Hu", "Nor", "Gil"

def Generator_jmeno(pred, konc):
    for p in pred:
        yield p + konc


predpony = ["Ga", "Di", "Ja", "Ho", "Vigh"]
koncovka = "nesh"
for jmeno in Generator_jmeno(predpony, koncovka):
    print(f" Tve jmeno je {jmeno}")