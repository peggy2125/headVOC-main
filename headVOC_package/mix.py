# Headspace volatile organic compound concentration calculator 

"""
Raoults Law (P = X * P0)
P = partial pressure of the volatile compound
X = mole fraction of the volatile compound
P0 = vapor pressure of the volatile compound

Ideal gas law (PV = nRT)
P = pressure of the volatile compound
V = volume of the headspace
n = moles of the volatile compound
R = ideal gas constant
T = temperature

Mole fraction (X = n1/nT)
n1 = moles of the volatile compound
nT = total moles of the volatile compound

n/V = P/RT
mole/volume is an expression of concentration
"""

# Ideal Gas (L*atm/mol*K)
R = 0.0821

# Temperature (K)
K = 298.15

# Volume of gas under SATP
satp_V = 22.4

# Total pressure (atm)
tATM = 1

# i.e., VOC diluted in water
h_2oRho = 1000 # density of water (g/L)
h_2oMW = 18.01528 # molecular weight of water (g/mol)
h_2oVP = 0.0313 # vapor pressure of water (atm) at 25 Degree C
h_20Vol = 0.05 # volume of water (L)

def volToMass(vol, rho):
    g = vol * rho
    return g

def massToMoles(mass, mw):
    n = mass / mw
    return n

def molFraction(n1, n2):
    # calculate total moles in the system
    nT = n1 + n2
    X = n1 / nT
    # return mole fraction of the first component
    return X
    
    

def molFractionsec(n1, n2, n3):
    # calculate total moles in the system
    nT = n1 + n2+ n3
    Y = n3 / nT
    # return mole fraction of the second component
    return Y

def vocPP(X, VP, tATM ):
    VPP = X * (VP/tATM)
    return VPP


def concMole(VPP, R, K):
    n = VPP / (R * K)
    cM = n / satp_V
    return cM

def volToMole(vol, rho, mw):
    # Convert volume (L) to moles with density (g/L) and molecular weight (g/mol)
    mass = volToMass(vol, rho)
    moles = massToMoles(mass, mw)
    return moles

def concMoleToPPM(cM, mw):
    # https://www.gastec.co.jp/en/technology/knowledge/concentration/
    # Assuming under standard conditions (1 atm, 25 Degree C)
    # Convert unit from mol/L to g/L
    cM = cM * mw
    # Convert unit from g/L to mg/L and to mg/m^3
    cM = cM * 1000 * 1000
    # Convert unit from mg/m^3 to ppm
    # mg/m^3*(22.4/MW) * (K/273.15) * 1atm
    PPM = cM * (22.4/mw) * (K/273.15) * 1
    return PPM
    
def main():
    # Water
    wRho = 1000 # density of water (g/L)
    wMW = 18.01528 # molecular weight of water (g/mol)
    wVP = 0.0313 # vapor pressure of water (atm) at 25 Degree C

    # Volume of water (L)
    wVol = 0.05

    # Convert volume to mass
    wMass = volToMass(wVol, wRho)

    # Convert mass to moles
    wMoles = massToMoles(wMass, wMW)
    
    # Acetone
    aRho = 791 # density of acetone (g/L)
    aMW = 58.08 # molecular weight of acetone (g/mol)
    aVP = 0.304 # vapor pressure of acetone (atm) at 25 Degree C

    # Volume of acetone (L)
    aVol = 0.00005

    # Convert volume to mass
    aMass = volToMass(aVol, aRho)

    # Convert mass to moles
    aMoles = massToMoles(aMass, aMW)

    # Mole fraction of acetone
    aX = molFraction(aMoles, wMoles)

    # Vapor pressure of acetone
    aVPP = vocPP(aX, aVP, tATM)

    # Concentration of acetone
    aConc = concMole(aVPP, R, K)

    # Ethanol
    eRho = 791 # density of Ethanol (g/L)
    eMW = 46.068 # molecular weight of Ethanol (g/mol)
    eVP = 0.0773074 # vapor pressure of Ethanol (atm) at 25 Degree C

    # Volume of Ethanol (L)
    eVol = 0.00005

    # Convert volume to mass
    eMass = volToMass(eVol, eRho)

    # Convert mass to moles
    eMoles = massToMoles(eMass, eMW)

    # Mole fraction of Ethanol
    eX =  molFractionsec(aMoles, wMoles, eMoles)

    # Vapor pressure of Ethanol
    eVPP = vocPP(eX, eVP, tATM)

    # Concentration of Ethanol
    eConc = concMole(eVPP, R, K)


    print(f"Water mass: {wMass} g")
    print(f"Water moles: {wMoles} mol")
    print(f"Acetone mass: {aMass} g")
    print(f"Acetone moles: {aMoles} mol")
    print(f"Acetone mole fraction: {aX}")
    print(f"Acetone concentration: {aConc} mol/L")
    PPM = concMoleToPPM(aConc, aMW)
    print(f"Acetone concentration: {PPM} ppm")

    print(f"Ethanol mass: {eMass} g")
    print(f"Ethanol moles: {eMoles} mol")
    print(f"Ethanol mole fraction: {eX}")
    print(f"Ethanol concentration: {eConc} mol/L")
    PPM2 = concMoleToPPM(eConc, eMW)
    print(f"Ethanol concentration: {PPM2} ppm")

if __name__ == "__main__":
    main()

    