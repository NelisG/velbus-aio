# Installing on RPi

* Install uv
* git clone https://github.com/NelisG/velbus-aio.git
* cd velbus-aio
* uv sync
## Run locally
* git pull && uv run examples/read_bus_2.py --connect /dev/ttyACM0

## Making service
Doc: https://www.raspberrypi.org/documentation/linux/usage/systemd.md

* Make service file:         
`sudo nano /etc/systemd/system/velbus-monitor.service`

* Add service code:
```[Unit]
[Unit]
Description=Velbus AIO Monitor
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/velbus-aio
ExecStart=/home/pi/.local/bin/uv run examples/read_bus_2.py --connect /dev/ttyACM0
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

* Enable service to start on boot  
```
# Reload systemd to recognize the new service
sudo systemctl daemon-reload

# Enable the service to start on boot
sudo systemctl enable velbus-monitor.service

# Start the service now
sudo systemctl start velbus-monitor.service
```

## Check the status and logs
```
# Check if it's running
sudo systemctl status velbus-monitor.service

# View the logs
journalctl -u velbus-monitor.service -f
```
