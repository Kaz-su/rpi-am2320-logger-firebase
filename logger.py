import smbus
import time
from datetime import datetime
from firebase import firebase
from pytz import timezone

i2c = smbus.SMBus(1)
address = 0x5c

firebase_url = 'https://YOUR_FIREBASE_URL.firebaseio.com/'
firebase = firebase.FirebaseApplication(firebase_url, None)

interval_sec = 600

def get_temp_hum():
    try:
        i2c.write_i2c_block_data(address,0x00,[])
    except:
        pass
    time.sleep(0.003)
    i2c.write_i2c_block_data(address,0x03,[0x00,0x04])

    time.sleep(0.015)
    block = i2c.read_i2c_block_data(address,0,6)
    humidity = ((block[2] << 8) + block[3]) / 10.0
    temperature = ((block[4] << 8) + block[5]) / 10.0

    return temperature, humidity

while True:
    temp, hum = get_temp_hum()
    data = {'temperature': temp, 'humidity':hum}
    timestamp = datetime.now().strftime('%s')
    try:
        firebase.put('/datas', timestamp, data)
    except:
        pass
    time.sleep(interval_sec)

