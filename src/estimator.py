def askForRegionName() :
    RegionName = str( input( "Please enter your region name: "))
    return RegionName

def askForavgAge() :
    avgAge = int( input( "Please enter average age: "))
    return avgAge

def askForavgDailyIncomeInUSD() :
    avgDailyIncomeInUSD = int( input( "Please enter your average daily income in USD: "))
    return avgDailyIncomeInUSD

def askForavgDailyIncomePopulation() :
    avgDailyIncomePopulation = int( input( "Please enter your average daily income population: "))
    return avgDailyIncomePopulation

def askForperiodType() :
    periodType = str( input( "Please enter period type: "))
    return periodType

def askFortimeToElapse() :
    timeToElapse = int( input( "Please enter time to elapse: "))
    return timeToElapse

def reportedCases() :
    reportedCases = int( input( "Please enter reported cases: "))
    return reportedCases

def askForpopulation() :
    population = int( input( "Please enter population: "))
    return population

def askFortotalHospitalBeds() :
    totalHospitalBeds = int( input( "Please enter number of hospital beds: "))
    return totalHospitalBeds

def calculatecurrentlyinfected( reportedCases ):
    currentlyinfected = ( reportedCases * 10)
    return currentlyinfected

def calculatesevereimpact( reportedCases ):
    severeimpactcurrentlyInfected = ( reportedCases * 50)
    return severeimpactcurrentlyInfected

def calculateNumberofInfectionsAfter28days( currentlyinfected):
    NumberofInfectionsAfter28days = ( currentlyinfected * 512)
    return NumberofInfectionsAfter28days

#def calculateinfectionsByRequestedTime(  )

def calcutalesevereCasesByRequestedTime (infectionsByRequestedTime):
    severeCasesByRequestedTime =( infectionsByRequestedTime * 0.15)
    return severeCasesByRequestedTime

def calculatehospitalBedsByRequestedTime ( totalHospitalBeds, severeCasesByRequestedTime ):
    hospitalBedsByRequestedTime = (totalHospitalBeds - severeCasesByRequestedTime)
    return hospitalBedsByRequestedTime


def main():

    RegionName = askForRegionName()
    avgAge = askForavgAge()
    DailyIncomeInUSD = askForavgDailyIncomeInUSD()
    DailyIncomePopulation = askForavgDailyIncomePopulation()
    PeriodType = askForperiodType()
    timeToElapse = askFortimeToElapse()
    population = askForpopulation()
    totalHospitalBeds = askFortotalHospitalBeds()
    CurrentlyInfected = calculatecurrentlyinfected( reportedCases)
    SevereImpact = calculatesevereimpact(reportedCases)
    NumberofInfectionsAfter28days = calculateNumberofInfectionsAfter28days(reportedCases)
    severeCasesByRequestedTime = calcutalesevereCasesByRequestedTime(infectionsByRequestedTime)
    hospitalBedsByRequestedTime = calculatehospitalBedsByRequestedTime(totalHospitalBeds, severeCasesByRequestedTime )

main()

