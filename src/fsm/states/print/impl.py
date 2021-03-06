'''
 * @file        impl.py
 * @ingroup     print
 * @brief       Files containing internal/private APIs
 *
 * Contains definitions of APIs specific to the print state
 *
'''

from fsm.states.cal.impl import sharedMemory_Cal
from fsm.states.input.impl import sharedMemory_Input

class printData():
    '''################## class API ##################'''
    # def __init__(self):
        # print("Empty Constructor for printData class")

    def printAllData(self):
        errorStatus = False

        ipObj = sharedMemory_Input()
        i = ipObj.getInputObj()

        calObj = sharedMemory_Cal()
        c = calObj.getCalObj()

        print("|-------------------------------------------------------------------------------------------------|")
        print("\t\t\t   Home Details")
        print("|-------------------------------------------------------------------------------------------------|")
        print("\t Address: \t\t\t{}".format(i.streetAddr))
        print("\t City: \t\t\t\t{}".format(i.city))
        print("\t State: \t\t\t{}".format(i.state))
        print("\t Beds: \t\t\t\t{}".format(i.beds))
        print("\t Baths: \t\t\t{}".format(i.baths))
        print("\t Sq.ft: \t\t\t{}".format(i.sqft))
        print("\t Year Built: \t\t\t{}".format(i.yearBuilt))
        print("\n\n")
        print("\t\t\t   Closing Details")
        print("\t Price:              \t\t\t\t{}".format(i.price))
        print("\t Downpayment Percent:\t\t\t\t{}".format(i.dpPercent))
        print("\t Downpayment Amount: \t\t\t\t{}".format(i.dpValue))
        print("\t Closing Amount:     \t\t\t{}".format(i.closingCost))
        print("\t Rehab Amount:       \t\t\t{}".format(i.rehabCost))
        print("\t Gap Amount:         \t\t\t{}".format(i.gapPayment))
        print("\t Initial Amount:     \t\t\t\t{}".format(c.totalInitialInvestment - i.dpValue))
        print("\t Total Closing Costs:\t\t\t\t\t\t{}".format(c.totalInitialInvestment))
        print("\n\n")

        print("|-------------------------------------------------------------------------------------------------|")
        print("\t\t\t\t CASH FLOW")
        print("|-------------------------------------------------------------------------------------------------|")
        print("Monthly Expenses")
        print("A. Principal & Interest: \t\t\t\t${:.2f}".format(c.monthlyPAndI))

        print(" B. Additional Expenses")
        print("    i. Monthly Fixed Expenses: \t\t${:.2f}".format(c.addlFixedExpenses))
        print("     - Property Tax: \t\t${:.2f}".format(c.propertyTaxPerMonth))
        print("     - Insurance: \t\t${:.2f}".format(i.monthlyInsurance))
        print("     - HOA: \t\t\t${:.2f}".format(i.hoa))
        print("     - PMI: \t\t\t${:.2f}".format(i.pmiPerMonth))

        print("   ii. Monthly Variable Expenses: \t${:.2f}".format(c.addlVarExpenses))
        print("     - Electricity: \t\t${:.2f}".format(i.electricity))
        print("     - Gas: \t\t\t${:.2f}".format(i.gas))
        print("     - Water/Sewer: \t\t${:.2f}".format(i.waterSewer))
        print("     - Garbage: \t\t${:.2f}".format(i.garbage))
        print("     - Other (monthly): \t${:.2f}".format(i.other))

        print("  iii. Futureproofing Expenses: \t\t${:.2f}".format(c.futureProofingExpenses))
        print("     - Repairs & Maintenance: \t${:.2f}".format(c.rnmValueMonthly))
        print("     - Vacancy: \t\t${:.2f}".format(c.vacancyValueMonthly))
        print("     - Capital Expenditure: \t${:.2f}".format(c.capExValueMonthly))
        print("     - Property Management: \t${:.2f}".format(c.pmValueMonthly))
        print("   Total Additional Expenses\t\t\t\t${:.2f}".format(c.addlMonthlyExpenses))

        print(" Total Monthly Expenses: \t\t\t\t\t${:.2f}".format(c.totalMonthlyExpenses))

        print(" Monthly Earnings")
        print("   Rent Earnings (monthly): \t\t\t\t${:.2f}".format(i.monthlyRent))
        print("   Other Earnings (monthly): \t\t\t\t${:.2f}".format(i.otherEarnings))
        print(" Total Monthly Earnings: \t\t\t\t\t${:.2f}".format(c.totalMonthlyEarnings))

        print("Total Cash Flow: \t\t\t\t\t\t${:.2f}".format(c.cashFlow))
        print("\n")

        print("|-------------------------------------------------------------------------------------------------|")
        print("\t\t\t\t CASH-ON-CASH RETURNS")
        print("|-------------------------------------------------------------------------------------------------|")
        print("Total Cash-on-Cash Returns (CoC): \t\t\t\t\t{:.2f}%".format(c.cocReturns))
        print("\n\n")

        print("|-------------------------------------------------------------------------------------------------|")
        print("\t\t\t\t OPERATING INCOME")
        print("|-------------------------------------------------------------------------------------------------|")
        print(" a. Gross Operating Income (GOI)")
        print("    - Monthly Gross Operating Income: \t\t\t\t${:.2f}".format(c.grossOperatingIncomeMon))
        print("    - Total Gross Operating Income (GOI): \t\t\t${:.2f}".format(c.grossOperatingIncome))
        print(" b. Net Operating Income (NOI)")
        print("    - Monthly Net Operating Income (NOI) Without CapEx: \t${:.2f}".format(c.noiMonthlyNoCapEx))
        print("    - Net Operating Income (NOI) Without CapEx: \t\t${:.2f}".format(c.totalNOINoCapEx))
        print("    - Monthly Net Operating Income (NOI): \t\t\t${:.2f}".format(c.noiMonthly))
        print("    - Total Net Operating Income (NOI): \t\t\t${:.2f}\n".format(c.totalNOI))
        print("\n\n")

        print("|-------------------------------------------------------------------------------------------------|")
        print("\t\t\t\t   CAP RATES")
        print("|-------------------------------------------------------------------------------------------------|")
        print(" a. Purchase Cap Rate: \t\t\t\t\t\t{:.2f}%".format(c.purchaseCapRate))
        print(" b. Pro-forma Cap Rate: \t\t\t\t\t{:.2f}%".format(c.proFormaCapRate))
        print("\n\n")

        print("|-------------------------------------------------------------------------------------------------|")
        print("\t\t\t    GROSS RENT MULTIPLIER (GRM)")
        print("|-------------------------------------------------------------------------------------------------|")
        print("Gross Rent Multiplier (GRM): \t\t\t\t\t{:.2f}".format(c.grm))
        print("\n\n")

        print("|-------------------------------------------------------------------------------------------------|")
        print("|\t\t\t\t\t END")
        print("|-------------------------------------------------------------------------------------------------|")

        return errorStatus


class SharedMemory_Print():
    '''############### Class Variables ###############'''
    printObj = printData()

    ''' ###### class API ###### '''
    # def __init__(self):
        # print("Empty constructor for sharedMemory_Print")

    def getPrintObj(self):
        return(self.printObj)

    def display(self):
        print(printObj)
