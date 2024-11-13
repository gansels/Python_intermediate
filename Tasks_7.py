# NA TENTO KOD NESAHAT
# Vytvoř novou instanci Budovy a přidej pár pater

from copy import deepcopy
class Budova:
    def __init__(self):
        self.patrol = []
    def add_patro(self,name_patro):
        self.patrol.append(name_patro)
    def get_copy(self):
        return deepcopy(self)

budova = Budova()
budova.pridej_patro("Kanceláře")
budova.pridej_patro("Laboratoř")

# Vytvoř kopii budovy pomocí metody get_copy
kopie_budovy = budova.get_copy()
kopie_budovy.pridej_patro("Střešní zahrada")

# Očekávaný výsledek: Budova má 2 patra, kopie budovy má 3 patra
print("Původní budova patra:", budova.patra)  # Očekává se: ["Kanceláře", "Laboratoř"]
print("Kopie budovy patra:", kopie_budovy.patra)  # Očekává se: ["Kanceláře", "Laboratoř", "Střešní zahrada"]

# Testuje, zda původní budova nebyla ovlivněna změnami v kopii
assert budova.patra == ["Kanceláře", "Laboratoř"], "Chyba: Původní budova byla změněna."
assert kopie_budovy.patra == ["Kanceláře", "Laboratoř",
                              "Střešní zahrada"], "Chyba: Kopie budovy nebyla správně vytvořena."

print("Gratuluji, test prošel: Třída Budova správně implementuje přidávání pater a metodu get_copy.")
