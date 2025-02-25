import sys
import json
valuesFile = sys.argv[1]
testsFile = sys.argv[2]
reportFile = sys.argv[3]
with open(valuesFile,'r') as valFile:
    values = json.load(valFile)
with open(testsFile, 'r') as tFile:
    tests = json.load(tFile)
report = []
    
def isValuePassed(id):
    for e in values['values']:
        if e['id'] == id:
            if (e['value'] == "passed"):
                return "passed"
            elif (e['value'] == "failed"):
                return "failed"
    return ""

def signValues(e : dict):
    e['value'] = isValuePassed(e['id'])
    if e['value'] == "":
        del e['value']
    if "values" in e:
        for elem in e['values']:
            signValues(elem)


for e in tests['tests']:
    signValues(e)
    report.append(e)

result = {"tests":report}
with open(reportFile, 'w+') as resultreport:
    json.dump(result,resultreport,indent=1)