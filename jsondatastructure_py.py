import json

#convert json to python map/dictionary
companyJson = """ {
	"company": "metaii",
	"employees" : ["bob", "jon", "alice", "monica", "sadia", "sara", "rob", "igor"],
	"address" : {
		"canada": "56 Temperence",
		"bd": "Eskaton Garden"
	},
	"isStartup": true,
	"number of employees": 8,
	"averageEmployeeAge": 25.5
}"""
companyDictionary = json.loads(companyJson)
print(companyDictionary)
print(companyDictionary['company'])
print(companyDictionary['employees'])

#create a python dictionary and convert it to json
fruits = {"apple" : "red", "banana": "yellow", "grape": "green"}
fruitJsonString = json.dumps(fruits)
print(fruitJsonString)
