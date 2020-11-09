# cd EnOcean_Aruba_IoT_Demo_v0_6_zip\EnOceanArubaIoT_Demo_v0_6\
import json
import subprocess

# =========Change your program logic===============
def rockerB_on():
    print("ON!!")
    pass

def rockerB_off():
    print("OFFFFFFFFFFFFFFFFF!!")
    pass

def rockerB_notPressed():
    print("-!!")
    pass

# =========Program Start===========
proc = subprocess.Popen(".\EnOcean-Aruba-Demo.exe", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print("============")

for line in proc.stdout:
    #the real code does filtering here
    result = line.decode()
    # Connected
    if result[10] == "{":
        #Json detected
        result = result[10:-2]
        result = result.replace("\\", "").replace("\"{","{").replace("}\"", "}")
        result_json = json.loads(result)
        if result_json["EnOceanDevices"] != {}:
            if "data" in result_json["EnOceanDevices"]["switch"]:
                print("Device Connected, received data", result_json["EnOceanDevices"]["switch"]["data"])
                rockerB_data = result_json["EnOceanDevices"]["switch"]["data"]["rockerB"]
                # RockerB on, off, notPressed
                if rockerB_data == "on":
                    rockerB_on()
                    
                elif rockerB_data == "off":
                    rockerB_off()
                elif rockerB_data == "notPressed":
                    rockerB_notPressed()
                else:
                    pass
