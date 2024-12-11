information = eval(input())

incomeAnnual = float(input())

deduct = 0

baseTaxRate = information["INCOME"]
family = information["MARITAL_STATUS"]
child = information["CHILD"]
specialNeeds = information["SPECIAL_NEEDS"]
elderlyCare = information["ELDERLY_CARE"]
city = information["CITY_CATEGORY"]
education = information["EDUCATION"]
health = information["HEALTHCARE"]
green = information["GREEN_INITIATIVES"]
propertyStatus = information["PROPERTY_STATUS"]
taxDuration = information["TAXPAYER_DURATION"]

baseTaxDict = {"low": 0.1, "middle": 0.2, "high": 0.3}
familyDict = {"single": 0 , "married": 500,"single_parent":0}
familyDict2 = {"single": 0 , "married" : 300, "single_parent": 600}
specialNeedsDict = {True: 1000, False: 0}
elderlyCareDict = {True: 800, False: 0}
cityCategoryDict = {"urban": 0,"suburban": 200, "rural": 400}
educationDict = {True: 500, False: 0}
healthDict = {True: 750, False: 0}
greenDict = {True: 300, False: 0}
propertyDict = {"owns": 0 ,"rents": 300}
taxDurationDict = {"new": 1, "regular": 0.95, "long_term": 0.9}

smallThan18 = list(filter(lambda i: i < 18, child))

deduct = deduct + familyDict[family]
deduct = deduct + familyDict2[family] * len(child)
deduct = deduct + len(smallThan18)*200
deduct = deduct + specialNeedsDict[specialNeeds]
deduct = deduct + elderlyCareDict[elderlyCare]
deduct = deduct + cityCategoryDict[city]
deduct = deduct + educationDict[education]
deduct = deduct + healthDict[health]
deduct = deduct + greenDict[green]
deduct = deduct + propertyDict[propertyStatus]



final_tax_amount = ((incomeAnnual * baseTaxDict[baseTaxRate]) - deduct) * taxDurationDict[taxDuration]

if final_tax_amount < 0:
    final_tax_amount = 0

print("%.2f" % final_tax_amount)
