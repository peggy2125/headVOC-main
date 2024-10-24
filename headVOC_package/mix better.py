import json
import os


def volToMass(Vol, vocrho):
    g = Vol * vocrho
    return g

def massToMoles(Mass, vocMW):
    n = Mass / vocMW
    return n


def vocPP(X, vocVP, tATM ):
    VPP = X * (vocVP/tATM)
    return VPP

def concMole(VPP, R, K):
    n = VPP / (R * K)
    cM = n / satp_V
    return cM

def volToMole(Vol, vocrho, vocMW):
    # Convert volume (L) to moles with density (g/L) and molecular weight (g/mol)
    mass = volToMass(Vol, vocrho)
    moles = massToMoles(mass, vocMW)
    return moles

def concMoleToPPM(cM, vocMW):
    # https://www.gastec.co.jp/en/technology/knowledge/concentration/
    # Assuming under standard conditions (1 atm, 25 Degree C)
    # Convert unit from mol/L to g/L
    cM = cM * mwvocMW
    # Convert unit from g/L to mg/L and to mg/m^3
    cM = cM * 1000 * 1000
    # Convert unit from mg/m^3 to ppm
    # mg/m^3*(22.4/MW) * (K/273.15) * 1atm
    PPM = cM * (22.4/mw) * (K/273.15) * 1
    return PPM



def load_voc_parameters(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def conc(voc_specie:str):
    directory = os.path.dirname(__file__)  # Get the directory where the script is located
    json_path = os.path.join(directory, 'voc_parameters.json')  # Construct the path to the JSON file
    voc_parameters = load_voc_parameters(json_path)
    voc = voc_parameters[voc_specie]
    std_conditions = voc_parameters['standard_conditions']


    R = std_conditions['ideal_gas_constant']
    K = std_conditions['temperature']
    tATM = std_conditions['total_pressure']

    #water
    #aRho = voc['density'] # density of acetone (g/L)
    #MW = voc['molecular_weight'] # molecular weight of acetone (g/mol)
    #aVP = voc['vapor_pressure'] # vapor pressure of acetone (atm) at 25 Degree C

    #ALL VOC # Acetone
    vocRho = voc['density'] # density of acetone (g/L)
    vocMW = voc['molecular_weight'] # molecular weight of acetone (g/mol)
    vocVP = voc['vapor_pressure'] # vapor pressure of acetone (atm) at 25 Degree C
    Vol = 0.00005 #assume all VOC has same volume

# Convert volume to mass
    Mass = volToMass(Vol, vocRho)
    # Convert mass to moles
    Moles = massToMoles(Mass, vocMW)
    # Vapor pressure of Ethanol
    VPP = vocPP(X, vocVP, tATM)
    # Concentration of Ethanol
    Conc = concMole(VPP, R, K)
     # Mole fraction of all
user_input = input("請輸入有多少種混和氣體: ")
number = int(user_input)
for i in range(0, number-1, 1):
    n =
    sum=
    
    X =  molFractionsec(Moles, Moles, Moles)

    # # Calculate concentration of acetone in moles
    # cM = PPMtoConcMole(1, vocMW)
    # # Calculate partial pressure of acetone
    # VPP = concToPP(cM, R, K)
    # X = molFractionPP(VPP, vocVP, tATM)
    # n1 = molFractionToMole(X, diluteMoles)
    # mass = moleToMass(n1, vocMW)
    # vol = massToVol(mass, vocRho)
    # print(f"{vol} L of acetone is required to reach 1PPM with 50ml of water")

