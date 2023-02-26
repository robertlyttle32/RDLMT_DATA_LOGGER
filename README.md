# RDLMT_DATA_LOGGER
A data logger for general use for logging all data types once configured.  Includes a 2.0 inch LCD display and four push-buttons for stand alone operations. No need to ssh in order to start, stop, reset log file, or to power-down the logger.

Part List:
Pimononi Display Hat Mini: (https://shop.pimoroni.com/products/display-hat-mini)
Raspberry Pi Zero 2 W: (https://shop.pimoroni.com/products/raspberry-pi-zero-2-w)
Zero2Go Omni power supply: (https://shop.pimoroni.com/products/zero2go-omini-rev2-wide-input-range-multi-channel-power-supply-for-raspberry-pi)
PA1010D GPS Breakout: (https://shop.pimoroni.com/products/pa1010d-gps-breakout)
40-pin female header with long terminals: (https://shop.pimoroni.com/products/2x20-pin-gpio-header-for-raspberry-pi-2-b-a?variant=1132812269)
40-pin male header: (https://shop.pimoroni.com/products/male-40-pin-2x20-hat-header?variant=10476117383)
To Run at reboot:
Open terminal
Type <crontab -e> then press Enter (do NOT yes sudo)
Next type <@reboot pyhron3 script.py
Then save.
