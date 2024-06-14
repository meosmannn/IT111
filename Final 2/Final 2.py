
import json


f = open('final2.json', 'r')


data = json.load(f)

f.close()


print(data)


data.pop("HTTPS", None)


print(data)


data["Rating"] = "Excellent"


print(data)


print(data["Link"])


f = open('final2_results.json', 'w')


JSONdata = json.dumps(data)
f.write(JSONdata)


f.close()