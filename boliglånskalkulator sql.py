"""
Boliglånskalkulator - Forelesningsøkt 8.12.2025

-----------------------------------------------

Dette programmet gjør tre ting:

1. Spør bruker om:
    - Kjøpesum (Pris på bolig)
    - Egenkapital
    -Samlet årsintekt
    - Samlet gjeld
    - Antall lånetakere
    - Sivilstatus (gift / ugift)
    - Om de har barn
    - Om de har bil

2. Regne ut:
    - Hvor mye lån man trenger (lånebeløp = kjøpesum - egenkapital)
    - En veldig enkel maks lånegrense ( 5x samlet inntekt)

3. Beregner et estimat på mnd. terminbeløp, basert på:
    - En fast årlig rente (f.eks. 4,5 %)
    - En fast nedbetalingstid (f.eks. 25 år)

"""

print("Veldig enkel boliglånskalkulator\n")

# 1. Henter inn data fra bruker

# input () Henter inn / leser tekst fra bruker.
# Vi bruker float() for å gjøre tekst om til et desimaltall (f.eks. 3000000.0)

kjopesum = float(input("Kjøpesum på boligen (kr): "))
egenkapital = float(input("Egenkapital (kr): "))
samlet_inntekt = float(input("Samlet årsinntekt (kr før skatt): "))
samlet_gjeld = float(input("Samlet gjeld fra før (kr): "))

antall_lanetakere = int(input("Antall lånetaker (f.eks 1 eller 2): "))

sivilstatus = input("Sivilstatus (Skriv 'gift' eller 'ugift'): ").strip().lower()

har_barn = input("Har du / dere barn? (ja/nei): ").strip().lower()
har_bil = input("Har du/dere bil? (ja/nei): ").strip().lower()


print("\nSteg 2: Regner ut lånebehov")
# Regner ut lånebehov
# Lånebehov = hvor mye vi må låne i banken

lanebehov = kjopesum - egenkapital

print(f"Kjøpesum: {kjopesum:,.0f} kr")
print(f"Egenkapital {egenkapital:,.0f} kr")

if lanebehov <= 0:
    # Hvis egenkapital er større eller lik kjøpesum
    print("Du har nok egenkapital til å kjøpe bolig uten lån!")
else:
    print(f"Lånebehov (kjøpesum - egenkapital): {lanebehov:,.0f} kr")

print("\nSteg 3: Enkel lånevurdering")

# 3. Enkel maks lånegrenser (Veldig forkortet regel)
# I Norge bruker banken ofte en "5 ganger regel"
# Vi bruker dette bare som en pedagogisk regel.

maks_total_gjeld = 5 * samlet_inntekt  # 5 ganger inntekt regel

# Total gjeld etter et evt boliglå:
total_gjeld_etter_lan = samlet_gjeld + max(lanebehov, 0)
print(f"Samlet inntekt: {samlet_inntekt:,.0f} kr")
print(f"Samlet gjeld fra før: {samlet_gjeld:,.0f}")
print(f"Maks total gjeld (5x inntekt): {maks_total_gjeld:,.0f} kr")
print(f"Total gjeld etter boliglån: {total_gjeld_etter_lan:,.0f}")

if total_gjeld_etter_lan <= maks_total_gjeld:
    print("I denne enkle modellen er total gjeld innenfor 5x regelen")
else:
    print("I denne enkle modelen er total gjeld over 5x regelen")

# Vi skriver også litt om situasjonen, bare for å vise bruk av if-setninger
print("\nKort om situasjonen din")

print(f"Antall lånetakere: {antall_lanetakere}")
print(f"Sivilstatus: {sivilstatus}")
print(f"Barn: {har_barn}")
print(f"Bil: {har_bil}")

# 4. Bergengne mnd terminbeløp
# Vi gjør dette kun hvis det er behov for lån (lånebehov > 0)

if lanebehov > 0:
    print("\nSteg 4: Estimer terminbeløp")

    # Vi velger faste verdier for rente og nedbetalinstid.
    # Disse kan dere få lov til å endre og teste

    arlig_rente_prosent = 4.5  # 4,5% årlig rente
    nedbetalingstid_ar = 25  # 25 års nedbetalingstid

    # Gjør om årlig rente til månedesrente
    mnd_rente = arlig_rente_prosent / 100 / 12

    # Antall måneder totalt
    antall_mnd = nedbetalingstid_ar * 12

    # Annuitetsformel
    # L = Lånebeløp (Lånebehov)
    # r = månedsrente
    # n = antall rerminer (måneder)
    # Terminbeløp: L * r / (1 - (1+r)^(-n))

    if mnd_rente > 0:
        terminbelop = lanebehov * mnd_rente / (1 - (1 + mnd_rente) ** (antall_mnd))
    else:
        # Hvis renten av en eller annen grunn er 0
        terminbelop = lanebehov / antall_mnd
    print(f"Brukt rente: {arlig_rente_prosent:.2f} % per år")
    print(f"Nedbetalingstid: {nedbetalingstid_ar} år {antall_mnd} måneder")
    print(f"Estimert terminbeløp per måned: {terminbelop:,.0f} kr")

    print("\nNB! Dette er en veldig forenklet modell, bare for undervisning")
else:
    print("Du trenger ikke lån. Vi beregner ikke terminbeløp")
