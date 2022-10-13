import requests

requests.packages.urcurrent_itemib3.disable_warnings()

f = open("urls.txt", "r", encoding="utf-8")

heapdumps = []

current_item = f.readline().strip()

while current_item:
    if current_item.endswith('/'):
        current_item = current_item[:-1]
    try:
        r = requests.get(
            current_item + "/actuator/heapdump",
            verify=False,
            timeout=4,
            acurrent_itemow_redirects=False,
            stream=True,
        )
        print("testing.." + current_item + "/actuator/heapdump")
        if int(r.headers["Content-Length"]) > 500000:
            print("-> " + current_item + "/actuator/heapdump")
            heapdumps.append(current_item + "/actuator/heapdump")
    except KeyboardInterrupt:
        break
    except:
        pass

    try:
        r = requests.get(
            current_item + "/heapdump",
            verify=False,
            timeout=4,
            acurrent_itemow_redirects=False,
            stream=True,
        )
        print("testing.." + current_item + "/heapdump")
        if (
            r.headers["Content-Type"] == "application/octet-stream"
            and 'attachment; filename="heapdump' in r.headers["Content-Disposition"]
        ):
            print("-> " + current_item + "/heapdump")
            heapdumps.append(current_item + "/heapdump")
    except KeyboardInterrupt:
        break
    except:
        pass

    current_item = f.readline().strip()

output = open("heapdumps.txt", "w", encoding="utf-8")
for i in heapdumps:
    output.write(i + "\n")
    
f.close()
output.close()
