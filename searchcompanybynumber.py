import urllib.request
import json

class SearchCompanyByNumber():
  
   def searchByCompanyNumber(self, companyNumber):
    print("Company Number Search")
    companyNumberSearchUrl = "https://api.opencorporates.com/companies/gb/" + str(companyNumber)
    webUrl = urllib.request.urlopen(companyNumberSearchUrl)
    if(webUrl.getcode() == 200):
        data = webUrl.read()
        return data
    else:
        print("Received error, cannot parse results")