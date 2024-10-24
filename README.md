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




## c2v_headVOC 
def部分為變數轉換
function: calc_v2c(voc_specie, dilute_med:str)
voc_specie、dilute_med為一個變數，分別為要從json檔中抓取的voc名稱
因此當在function括弧中輸入不同的string(名稱voc)時，即可運算不同voc


## v2c_headVOC
def部分為變數轉換
main function中，針對voc以先前定義的函數取得之摩爾分率，最後根據拉伍爾定律計算出voc濃度

## mix.py


