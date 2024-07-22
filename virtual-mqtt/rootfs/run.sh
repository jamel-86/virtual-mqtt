#!/usr/bin/with-contenv bashio

# Get the MQTT broker URL from the add-on configuration
BROKER=$(bashio::config 'broker')

# Run your Python script to simulate devices
python3 /fake_mqtt_devices.py --broker $BROKER