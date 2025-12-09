"""Boliglånskalkulator - Forelesningsøkt 08122025
------------------------------------------------
Dette programmet gjør tre ting:
1. Spør brukeren om:
 - Kjøpesum
 - Egenkapital
 - Samlet årsinntekt
 - Samlet gjeld
 - Antall lånetakere
 - Sivilstatus (gift/ugift)
 - Om de har barn
 - Om de har bil
2. Regner ut:
 - Hvor mye lån du trenger (Lånebeløp = Kjøpesum - Egenkapital)
 - En veldig enkel maks lånegrense (5x samlet inntekt)
3. Beregner et estimat på månedlig terminbeløp basert på:
 - En fast årlig rente (f.eks. 4,5%)
 - En fast nedbetalingstid (f.eks. 25 år)
------------------------------------------------"""

print("=== VELDIG ENKEL BOLIGLÅNSKALKULATOR ===\n")
"""
1. HENTER INN DATA FRA BRUKEREN
-----------------------------------------------
input() LESER tekst fra brukeren
float() GJØR om tekst til desimaltall (f.eks. 3000000.0)
"""

kjopesum = float(input("Kjøpesum på boligen (kr): "))
egenkapital = float(input("Egenkapital (kr): "))
samlet_inntekt = float(input("Samlet årsinntekt (kr før skatt): "))
samlet_gjeld = float(input("Samlet gjeld fra før (kr): "))
antall_lanetakere = int(input("Antall lånetakere (f.eks 1 eller 2): "))
sivilstatus = input("Sivilstatus (gift/ugift): ").strip().lower()
har_barn = input("Har du/dere barn? (ja/nei): ").strip().lower()
har_bil = input("Har du/dere bil? (ja/nei): ").strip().lower()

"""
2. REGNER UT LÅNEBEHOV
-----------------------------------------------
Lånebeløp = Hvot mye lån man trenger
"""
lanebehov = kjopesum - egenkapital
print("\n--- STEG 2: LÅNEBEHOV ---")
print(f"Kjøpesum: {kjopesum:,.0f} kr")
print(f"Egenkapital: {egenkapital:,.0f} kr")

if lanebehov <= 0:
    #Hvis egenkapitalen er større enn eller lik kjøpesummen
    print("Du har nok egenkapital til å kjøpe boligen uten lån!")
else:
    print(f"Lånebehov (kjøpesum - egenkapital): {lanebehov:,.0f} kr")

print("\n--- ENKEL LÅNEVURDERING ---")
""" 3. ENKEL MAKS LÅNEGRENSE (VELDIG FORKORTET REGEL)
-----------------------------------------------
I Norge bruker banker ofte en "5-ganger-regel":
Totalt gjeld skal helst ikke være mer enn 5x inntekt.
Vi bruker dette bare som en PEDAGOGISK regel.
"""
maks_total_gjeld = samlet_inntekt * 5 #5-ganger-regel

#Total gjeld etter nytt lån
total_gjeld_etter_lan = samlet_gjeld + max(lanebehov, 0)

print(f"Samlet inntekt: {samlet_inntekt:,.0f} kr")
print(f"Samlet gjeld fra før: {samlet_gjeld:,.0f} kr")
print(f"Maks total gjeld basert på 5-ganger-regel: {maks_total_gjeld:,.0f} kr")
print(f"Total gjeld etter nytt lån: {total_gjeld_etter_lan:,.0f} kr")

if total_gjeld_etter_lan <= maks_total_gjeld:
    print("-> I denne ENKLE modellen er total gjeld innenfor 5x-regelen.")
else:
    print("-> I denne ENKLE modellen er total fjeld OVER 5x-regelen.")

#Vi skriver også litt om situasjonen, bare for å vise bruk av if-setninger

print("\n--- Kort om situasjonen din ---")

print(f"Antall lånetakere: {antall_lanetakere}")
print(f"Sivilstatus: {sivilstatus.capitalize()}")
print(f"Barn: {har_barn.capitalize()}")
print(f"Bil: {har_bil.capitalize()}")

"""4. BEREGNER MÅNEDLIG TERMINBELØP
-----------------------------------------------
Vi gjør dette KUN hvis det er behov for lån (lånebehov > 0)
"""
if lanebehov > 0:
    print("\n--- STEG 4: ESTIMERT TERMINBELØP ---")
    #Vi velger faste verdier for rente og nedbetalingstid
    #Disse kan dere få lov til å endre på og teste
    aarlig_rente_prosent = 4.5  #Årlig rente i prosent
    nedbetalingstid_aar = 25    #Nedbetalingstid i år

    #Gjør om årlig rente til månedsrente
    manedsrente = (aarlig_rente_prosent / 100) / 12

    #Antall måneder totalt
    antall_maneder = nedbetalingstid_aar * 12

    #Annuitetsformel
    #L= Lånebeløp (Lånebehov)
    #r= Månedsrente
    #n= Antall terminer (måneder)
    #Terminbeløp= L*r/(1-(1+r)^-n)

    if manedsrente > 0:
        terminbelop = lanebehov * manedsrente / (1 - (1 + manedsrente) ** -antall_maneder)
    else:
        #Hvis renta av en eller annen grunn er 0%
        terminbelop = lanebehov / antall_maneder
    print(f"Brukt rente: {aarlig_rente_prosent:.2f}% per år")
    print(f"Nedbetalingstid: {nedbetalingstid_aar} år ({antall_maneder} måneder)")
    print(f"Estimert terminbeløp per måned: {terminbelop:,.0f} kr")

    print("\nNB! Dette er et VELDIG forenklet estimat.")

else:
    print("\nIngen lån nødvendig, så ingen terminbeløp å beregne.")
