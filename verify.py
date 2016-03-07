import base64, hashlib, json


with open('motions.json') as file:
    json_data = json.load(file)


for motion in json_data:

    data = json_data[motion]

    expected_hash = data.get("hash")

    calculated_hash = hashlib.new('ripemd160', base64.b64decode(data.get("b64encoded"))).hexdigest()

    if expected_hash != calculated_hash:
        print motion + " FAILED"
        print "expected hash: " + expected_hash
        print "calculated hash: " + calculated_hash
        print "\n"