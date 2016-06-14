import nest
from  ISStreamer.Streamer import Streamer
import flowthings
import time
***REMOVED***

nestuser='herbndove@comcast.net'
nestpass='H&MR4Fun'

BUCKETKEY='JCFANLUSNACG'
ACCESSKEY='uawK8SHL7CMadFAqyKWToCUUe9mwOTim'



streamer = Streamer(bucket_name="nest_data", bucket_key=BUCKETKEY, access_key=ACCESSKEY)
nlogged = 0
starttime = '%s' % (datetime.datetime.now(),)

while True:
    with nest.Nest(nestuser, nestpass) as napi:
        for structure in napi.structures:
            streamer.log(structure.name+": external Temperature", '%d' % (structure.weather.current.temperature*9/5.0+32,))
            streamer.log(structure.name+": external Humidity", structure.weather.current.humidity)
            for device in structure.devices:
                streamer.log(device._repr_name+': temperature', '%d' % (device.temperature*9/5.0+32,) )
                streamer.log(device._repr_name+': humidity', device.humidity)
                #print ('reported %s in %s' % (device._repr_name, structure.name))
    nlogged = nlogged + 1
    print('Temp and Humidity logged at %s' % (datetime.datetime.now(),))
    print('%d logged since %s' % (nlogged, starttime))
    time.sleep(60)
