import json

class ExtractData():

    def extractInformation(self, data):
        theJSON = json.loads(data)

    # Returns Company information of the Company Number entered
        if 'name' in theJSON["results"]["company"]:
            companyName = theJSON["results"]["company"]["name"]
            companyNumber = theJSON["results"]["company"]["company_number"]
            incorporationDate = theJSON["results"]["company"]["incorporation_date"]
            companyType = theJSON["results"]["company"]["company_type"]
            companyStatus = theJSON["results"]["company"]["current_status"] 
        
        return companyName, companyNumber, incorporationDate, companyType, companyStatus

    #def printResults(self, data):
    #    print()