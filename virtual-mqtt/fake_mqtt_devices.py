import paho.mqtt.client as mqtt
import time
import json
import argparse

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def simulate_device(client, device_id, device_type, interval=5):
    while True:
        if device_type == "light":
            state = {"state": "ON" if int(time.time()) % 2 == 0 else "OFF"}
        elif device_type == "sensor":
            state = {"temperature": 20 + int(time.time()) % 10}
        else:
            state = {}

        client.publish(f"homeassistant/{device_type}/{device_id}/state", json.dumps(state))
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate MQTT Devices")
    parser.add_argument("--broker", required=True, help="MQTT Broker URL")
    args = parser.parse_args()

    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(args.broker)

    client.loop_start()

    simulate_device(client, "light1", "light")
    simulate_device(client, "sensor1", "sensor")
