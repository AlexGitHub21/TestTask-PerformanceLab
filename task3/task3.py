import sys
import json

values = sys.argv[1]
tests = sys.argv[2]
report = sys.argv[3]

with open(values) as f:
    values = json.load(f)

with open(tests) as f:
    tests = json.load(f)

values = {value["id"]: value["value"] for value in values["values"]}

def fill_values(tests):
    if type(tests) == dict:
        if "id" in tests and tests["id"] in values:
            tests["value"] = values[tests["id"]]
        for key in tests:
            fill_values(tests[key])
    if type(tests) == list:
        for test in tests:
            fill_values(test)

    return tests

tests = fill_values(tests["tests"])
with open(report, "w") as f:
    json.dump(tests, f, indent=2)
