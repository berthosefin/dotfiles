

'''
IRSA : Import sur les Revenus Salariaux et Assimilés
SME : Salaire Minimum d'Embauche
SI : Salaire Impôsable
Tranche IRSA: 
    a - SI < 350_000 = 0%
    b - 350_001 < SI < 400_000 = 5%
    d - 400_001 < SI < 500_000 = 10%
    e - 500_001 < SI < 600_000 = 15%
    f - 600_001 < SI = 20%
'''


# CNAPS
def cnaps(salaire):
    return int((salaire * 1)/100)   # Retenu par l'employeur


# CDS
def cds(salaire):
    return int((salaire * 2)/100)   # Retenu par l'employeur


# SI
def si(salaire):
    return salaire - cnaps(salaire) - cds(salaire)


# IRSA
def irsa(si):
    SME = 250_000
    MIN_IRSA = 3_000
    MAX_A = 350_000
    MAX_B = 400_000
    MAX_D = 500_000
    MAX_E = 600_000

    # Tranche
    a = 0
    b = 2_500
    d = 10_000
    e = 15_000

    if si <= MAX_A:
        a = MIN_IRSA
        irsa = a
    elif MAX_A+1 < si <= MAX_B:
        b = int(((si - MAX_A+1) * 5)/100)
        irsa = a + b
    elif MAX_B+1 < si <= MAX_D:
        d = int(((si - MAX_B+1) * 10)/100)
        irsa = a + b + d
    elif MAX_D+1 < si <= MAX_E:
        e = int(((si - MAX_D+1) * 15)/100)
        irsa = a + b + d + e
    elif MAX_E+1 < si:
        f = int(((si - MAX_E+1) * 20)/100)
        irsa = a + b + d + e + f

    return irsa if irsa > MIN_IRSA else MIN_IRSA


if __name__=='__main__':
    salaire = 618_556
    si = si(salaire)
    print(f"Salaire: {salaire}")
    print(f"CNAPS: {cnaps(salaire)}")
    print(f"CDS: {cds(salaire)}")
    print(f"SI: {si}")
    print(f"IRSA: {irsa(si)}")