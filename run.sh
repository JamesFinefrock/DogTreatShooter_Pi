#!/bin/bash

sudo systemctl restart bluetooth.service
./gatt_server &
sudo hciconfig hci0 reset
sudo hciconfig hci0 leadv 0
sudo hciconfig hci0 leadv 0
