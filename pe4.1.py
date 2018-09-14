cijferICOR = (7.0)
cijferPROG = (6.0)
cijferCSN = (9.0)

money_per_punt = 30



gemiddeldecijfers = (cijferCSN + cijferICOR + cijferPROG) / 3 # gemiddelde van alle vakken
gemiddeldecijfers = round(gemiddeldecijfers,2)
money_verdiend = gemiddeldecijfers * money_per_punt
print (f"Mijn cijfers (gemiddeld een {gemiddeldecijfers} leveren een beloning van € {money_verdiend} op!")