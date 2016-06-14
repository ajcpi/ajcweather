import nest
#from  ISStreamer.Streamer import Streamer
import flowthings
#from flowthings import API, Token, mem
import time
***REMOVED***
import configparser

config = configparser.ConfigParser()
config.read('iot.ini')

nestuser=config['NEST']['user']
nestpass=config['NEST']['password']

ACCOUNT=config["FLOWTHINGS.ajcweather"]['account']
TOKEN=config["FLOWTHINGS.ajcweather"]['token']

#BUCKETKEY='JCFANLUSNACG'
#ACCESSKEY='uawK8SHL7CMadFAqyKWToCUUe9mwOTim'

creds = flowthings.Token(ACCOUNT, TOKEN)
api = flowthings.API(creds)
flows = api.flow.find(flowthings.mem.path == '/ajcweather/raw', limit=10)
flow_id = flows[0]['id']

#streamer = Streamer(bucket_name="nest_data", bucket_key=BUCKETKEY, access_key=ACCESSKEY)
nlogged = 0
starttime = '%s' % (datetime.datetime.now(),)

def drop(readings):
    edict = {***REMOVED***
    for i in readings:
        edict[str(i[0])] = { "type": "float", "value" : i[1]***REMOVED***
    drop = {
            "elems": edict
            ***REMOVED***
            
    

    print (drop)
    return drop        

while True:
    readings = []
    with nest.Nest(nestuser, nestpass) as napi:
        for structure in napi.structures:
            readings.append((structure.name+"_ehum", structure.weather.current.humidity))
            readings.append((structure.name+"_etemp", '%d' %(structure.weather.current.temperature*9/5.0+32,)))
            for device in structure.devices:
                readings.append((device._repr_name+'_itemp', '%d' % (device.temperature*9/5.0+32,) ))
                readings.append((device._repr_name+'_ihum', device.humidity))
                #print ('reported %s in %s' % (device._repr_name, structure.name))
    nlogged = nlogged + 1
    print('Temp and Humidity logged at %s' % (datetime.datetime.now(),))
    print('%d logged since %s' % (nlogged, starttime))
    new_drop = api.drop(flow_id).create(drop(readings))
    time.sleep(900)
