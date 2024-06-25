# Headspace VOC
Headspace volatile organic compound (VOC) is the VOC that is vaporized above the liquid. It is generally a  method to create VOC gas for separating liquid for gas so the gas can be analysed individually. In our case this is a method to generate VOC gas from liquid form without keeping the VOC in a pressurised cylinder making it easier to handle.

# Calculation logic
Raoult's law states that partial pressure of a voc = mole fraction * vapor pressure / total pressure as they are proportional. Once the voc partial pressure is obtained we can plug the pressure of the voc into the ideal gas law to obtain the amount of voc in the air

# Units
## Units used in voc_parameters.json
- Density: g/L
- Volume: L
- Molecular Weight: g/mol
Vapor pressure can be calculated with antoine equation with the following calculator:
http://ddbonline.ddbst.com/AntoineCalculation/AntoineCalculationCGI.exe
- Vapor pressure@25 Degree C: atm
- Ideal gas constant: (L*atm) / (K*mol)
