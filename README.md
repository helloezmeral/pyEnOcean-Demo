# pyEnOcean-Demo
This is the Addon of the EnOcean demo where forward the demo program terminal to python and do other things.

![](https://www.enocean.com/fileadmin/user_upload/aruba-header.jpg)
# EnOcean and Aruba
Check this link: https://www.enocean.com/en/applications/iot-solutions/

To download the demo program: https://www.enocean.com/fileadmin/redaktion/visuals/aruba/EnOcean_Aruba_IoT_Demo_v0_6.zip

# Usage
1. Download the IoT Demo program, double click the exe file to make sure everything is connected
2. Kill the program
3. Run the pyEnOcean.py within the same directory of "EnOcean-Aruba-Demo.exe"
4. Change the py file to do what you want

# Tips and Tricks
result.replace("\\", "").replace("\"{","{").replace("}\"", "}") is needed because the original Json message is not correct.


