import urllib.request
import json
from searchcompanybynumber import SearchCompanyByNumber
from extractdata import ExtractData

def main():
    print("Please enter Company Number")
    companyNumberInput = input()
    searchCompanyByNumber = SearchCompanyByNumber()
    companyNumberSearchResult = searchCompanyByNumber.searchByCompanyNumber(companyNumberInput)
    dataExtractedFromCompanyNumberSearchResult = ExtractData()
    extractedData = dataExtractedFromCompanyNumberSearchResult.extractInformationFromCompanyNumberSearch(companyNumberSearchResult)
    print(extractedData)

if __name__ == "__main__":
    main()
