import urllib.request
import json
from searchcompanybynumber import SearchCompanyByNumber
from extractdata import ExtractData

def main():
    print("Please enter Company Number")
    companyNumberInput = input()
    p1 = SearchCompanyByNumber()
    companyNumberSearchResult = p1.searchByCompanyNumber(companyNumberInput)
    p2 = ExtractData()
    extractedData = p2.extractInformation(companyNumberSearchResult)
    print(extractedData)

if __name__ == "__main__":
    main()
