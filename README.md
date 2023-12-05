
### Installation

Use this [tutorial](https://micropython.org/download/ESP32_GENERIC/) for installation the uPython on the MADE4HOME

 1. On windows

 - Erase the chip
```sh
call C:\Users\<user_name>\Documents\Python\esptool\.venv\Scripts\python -m esptool --chip esp32 --port COM11 erase_flash
```

 - Flash the chip
```sh
call C:\Users\<user_name>\Documents\Python\esptool\.venv\Scripts\python -m esptool --chip esp32 --port COM11 --baud 460800 write_flash -z 0x1000 C:\Users\User\Documents\Python\esptool\uPython\ESP32_GENERIC-20231005-v1.21.0.bin
```

2. On linux
 - Erase the chip
```sh
python -m esptool --chip esp32 --port /dev/ttyUSB0 erase_flash
```

 - Flash the chip
```sh
python -m esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin
```

### Use development environment

 - [Download](https://thonny.org/) Thony IDE
