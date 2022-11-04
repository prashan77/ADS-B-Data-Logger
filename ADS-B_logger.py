#--------Logging ADS_B Data------------------------------------------------------------------
#------it converts aircraft.json file and save to data in csv format in real time------------
#-----By: Prashant Thapaliya email:- prashantthapaliya@outlook.com-------------------------------------

#the aircraft data is store in json format so we have to use json library
import json
import time
import datetime


#wait time to access the aircraf.json file NOTE: aircraf.json file is updated every second thats why we are using 1 as a wait time if you do not want to use bash script
#interval = 1 

#some decoded message might not have keys like 'flight' or 'squawk' that why we are creating default empty values if the json file does not have the keys
default = {
    'hex': " ",
    'flight': " ",
    'alt_baro': " ",
    'alt_geom': " ",
    'gs': " ",
    'track': " ",
    'baro_rate': " ",
    'category': " ",
    'nav_qnh': " ",
    'nav_altitude_mcp': "",
    'nav_heading': " ",
    'lat': " ",
    'lon': " ",
    'nic': " ",
    'rc': " ",
    'version': " ",
    'nic_baro': " ",
    'nac_p': " ",
    'nac_v': " ",
    'sil': " ",
    'sil_type': " ",
    'mlat': " ",
    'tisb': " ",
    'messages': " ",
    'seen': " ",
    'rssi': " ",
    'gva': " ",
    'sda': " ",
    'emergency': " ",
    'mlat': " ",
    'squawk': " ",
    'seen_pos': " ",
}

 #for time stamp
now = datetime.datetime.now()
    
#aircraft.json file where the 1090 MHz aircraft data is stored and updated every second
json_file1 = open(r'/run/dump1090-fa/aircraft.json')
aircraft1090_json = json.load(json_file1)
    
#file where we will log ADS-B data
csv_file= open('aircraft_data.csv', "a")


for data in aircraft1090_json['aircraft']:             #looping through data in aircraft section of json file
    for field in default.keys():                   #nested loop to check if the key are in the aircraft.json file
        if field not in data:                      #if loop to replace the values with empty if the keys are not present in the json file
            data[field] = default[field]
    if data['sil'] == " " and data['nac_p'] == " " or data['alt_geom'] == " ":                         # will not store data if sil value is empty
        continue
    else:
        csv_file.write(  # writing the data in cvs file
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (
                now.strftime('%Y-%m-%d %H:%M:%S'),
                data['hex'],
                data['flight'], data['alt_baro'], data['alt_geom'], data['gs'], data['track'], data['baro_rate'],
                data['emergency'],
                data['category'], data['nav_qnh'], data['nav_altitude_mcp'], data['nav_heading'], data['lat'],
                data['lon'],
                data['nic'], data['rc'],
                data['seen_pos'], data['version'], data['nic_baro'], data['nac_p'], data['nac_v'], data['sil'],
                data['sil_type'], data['gva'], data['sda'],
                data['mlat'], data['tisb'], data['messages'], data['seen'], data['rssi']))

#aircraft.json file where the 978 Mhz aircraft data is stored and updated every second
json_file2 = open(r'/run/skyaware978/aircraft.json')
aircraft978_json = json.load(json_file2)
    

for data in aircraft978_json['aircraft']:             #looping through data in aircraft section of json file
    for field in default.keys():                   #nested loop to check if the key are in the aircraft.json file
        if field not in data:                      #if loop to replace the values with empty if the keys are not present in the json file
            data[field] = default[field]
    if data['sil'] == " " and data['nac_p'] == " " and data['alt_geom'] == " ":                      # will not store data if sil value is empty
        continue
    else:
        csv_file.write(  # writing the data in cvs file
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (
                now.strftime('%Y-%m-%d %H:%M:%S'),
                data['hex'],
                data['flight'], data['alt_baro'], data['alt_geom'], data['gs'], data['track'], data['baro_rate'],
                data['squawk'], data['emergency'],
                data['category'], data['nav_qnh'], data['nav_altitude_mcp'], data['nav_heading'], data['lat'],
                data['lon'],
                data['nic'], data['rc'],
                data['seen_pos'], data['version'], data['nic_baro'], data['nac_p'], data['nac_v'], data['sil'],
                data['sil_type'], data['gva'], data['sda'],
                data['mlat'], data['tisb'], data['messages'], data['seen'], data['rssi']))

                                                                                          #wait time to access the aircraf.json file
    #closing file
    json_file1.close()
    json_file2.close()
    csv_file.close()

   
    

