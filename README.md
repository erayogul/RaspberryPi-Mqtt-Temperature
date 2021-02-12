# Raspberry Pi Temperature Station

Send temperature and humidity value to Mqtt broker on Raspberry Pi.
I used to DHT22 sensor for measuring temperature and humidity values.

## For Automatic Starting

You can use it with crontab.
```bash
@reboot /bin/sleep 30;  mosquitto_sub -d -t temp
@reboot /bin/sleep 30; mosquitto_sub -d -t hum
@reboot /bin/sleep 30; /usr/bin/python /home/pi/temp.py
```
