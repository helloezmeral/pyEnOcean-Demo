# pyEnOcean-Demo
This is the Addon of the EnOcean demo where forward the demo program terminal to python and do other things.

![](https://www.enocean.com/fileadmin/user_upload/aruba-header.jpg)
# EnOcean and Aruba
Check this link: https://www.enocean.com/en/applications/iot-solutions/

To download the demo program: https://www.enocean.com/fileadmin/redaktion/visuals/aruba/EnOcean_Aruba_IoT_Demo_v0_6.zip
- Newer version is available, but it do not work

# Usage
1. Download the IoT Demo program, double click the exe file to make sure everything is connected
2. Kill the program
3. Run the pyEnOcean.py within the same directory of "EnOcean-Aruba-Demo.exe"
4. Change the py file to do what you want

# Tips and Tricks
result.replace("\\", "").replace("\"{","{").replace("}\"", "}") is needed because the original Json message is not correct.

## Using the USB directly
1. Install the driver
2. Check the manual of the ascii code https://www.enocean.com/fileadmin/redaktion/support/dolphin-api/esp3_page.html

![image](https://user-images.githubusercontent.com/72959956/131094703-4c270a5e-93e6-48b5-a35a-698f82390f6d.png)

