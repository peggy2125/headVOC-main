import json
import os


def PPMtoConcMole(ppm, mw):
    # Convert concentration (ppm) to (mg/m^3) and to mol/L
    mgm3 = ppm / 1000000
    Conc = mgm3 / mw
    return Conc

def concToPP(Conc, R, K):
    # Convert concentration (moles) to partial pressure with ideal gas constant (L*atm/mol*K) and temperature (K)
    # 22.47L is already incorporated in the concentration definition
    VPP = Conc * R * K
    return VPP

def molFractionPP(VPP, VP, tATM):
    # Convert partial pressure to mole fraction with total pressure (atm)
    X = VPP / (VP/tATM)
    return X

def volToMass(vol, rho):
    # Convert volume (L) to mass with density (g/L) yielding mass (g)
    g = vol * rho
    return g

def massToMoles(mass, mw):
    # Convert mass (g) to moles with molecular weight (g/mol)
    n = mass / mw
    return n

def VPPtoMoleFraction(VPP, VP, tATM):
    # Convert partial pressure to mole fraction with total pressure (atm)
    X = VPP / (VP/tATM)
    return X

def molFractionToMole(X, n2):
    # Calculate moles of the volatile compound with mole fraction and total moles of the volatile compound
    n1 = (X * n2)/(1-X)
    return n1

def volToMole(vol, rho, mw):
    # Convert volume (L) to moles with density (g/L) and molecular weight (g/mol)
    # used to calculate water mole with a given volume
    mass = volToMass(vol, rho)
    moles = massToMoles(mass, mw)
    return moles
    
def moleToMass(n, mw):
    # Convert moles to mass with molecular weight (g/mol)
    mass = n * mw
    return mass

def massToVol(mass, rho):
    # Convert mass to volume with density (g/L)
    vol = mass / rho
    return vol

def load_voc_parameters(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def calc_v2c(voc_specie, dilute_med:str):
    directory = os.path.dirname(__file__)  # Get the directory where the script is located
    json_path = os.path.join(directory, 'voc_parameters.json')  # Construct the path to the JSON file
    voc_parameters = load_voc_parameters(json_path)
    voc = voc_parameters[voc_specie]
    std_conditions = voc_parameters['standard_conditions']
    dilute = voc_parameters[dilute_med]

    R = std_conditions['ideal_gas_constant']
    K = std_conditions['temperature']
    tATM = std_conditions['total_pressure']
    satp_V = std_conditions['satp_volume']

    # i.e., VOC diluted in water
    diluteRho = dilute['density'] # density of water (g/L)
    diluteMW = dilute['molecular_weight'] # molecular weight of water (g/mol)
    diluteVP = dilute['vapor_pressure'] # vapor pressure of water (atm) at 25 Degree C
    diluteVol = dilute['volume'] # volume of water (L)

    # Acetone
    vocRho = voc['density'] # density of acetone (g/L)
    vocMW = voc['molecular_weight'] # molecular weight of acetone (g/mol)
    vocVP = voc['vapor_pressure'] # vapor pressure of acetone (atm) at 25 Degree C
    vocPPM = voc['ppm'] # concentration of acetone in ppm

    # Calculate amount of acetone required to reach 1PPM with 50ml of water
    # Calculate moles of water in the system
    diluteMoles = volToMole(diluteVol, diluteRho, diluteMW)
    
    for PPM in vocPPM:
        # Calculate concentration of acetone in moles
        cM = PPMtoConcMole(PPM, vocMW)
        # Calculate partial pressure of acetone
        VPP = concToPP(cM, R, K)
        X = molFractionPP(VPP, vocVP, tATM)
        n1 = molFractionToMole(X, diluteMoles)
        mass = moleToMass(n1, vocMW)
        vol = massToVol(mass, vocRho)
        print(f"{vol*1000000} ul of {voc_specie} for {PPM}PPM with {diluteVol*1000}ml of {dilute_med}")

    # # Calculate concentration of acetone in moles
    # cM = PPMtoConcMole(1, vocMW)
    # # Calculate partial pressure of acetone
    # VPP = concToPP(cM, R, K)
    # X = molFractionPP(VPP, vocVP, tATM)
    # n1 = molFractionToMole(X, diluteMoles)
    # mass = moleToMass(n1, vocMW)
    # vol = massToVol(mass, vocRho)
    # print(f"{vol} L of acetone is required to reach 1PPM with 50ml of water")

if __name__ == "__main__":
    calc_v2c('2-propanol','water')