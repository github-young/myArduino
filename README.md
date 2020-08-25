# Memo and backup for arduino
`` myDHT `` contains bash and python scripts for logging temparature and humidity of our lab.

## Get started
See official repo: [arduino-cli](https://github.com/arduino/arduino-cli).

```sh
# Check arduino-cli commands first!
arduino-cli core install arduino:avr
arduino-cli compile --fqbn arduino:avr:uno xxx/xxx
arduino-cli upload -p /dev/ttyUSB0 --fqbn arduino:avr:uno xxx/xxx
```

## Basic usage
```sh
arduino-cli --help
arduino-cli board list
arduino-cli board listall mkr
arduino-cli compile --fqbn arduino:avr:uno SOS
arduino-cli compile --fqbn arduino:avr:uno myDHT
arduino-cli compile --fqbn arduino:samd:mkr1000 test.ino
arduino-cli compile test.ino
arduino-cli config init
arduino-cli core install arduino:avr
arduino-cli core list
arduino-cli core update-index
arduino-cli lib install "DHT sensor library"
arduino-cli lib search DHT
arduino-cli lib search DHT | less
arduino-cli sketch new ~/Documents/Arduino/newOne
arduino-cli upload -p /dev/ttyUSB0 --fqbn arduino:avr:uno SOS
arduino-cli upload -p /dev/ttyUSB0 --fqbn arduino:avr:uno myDHT
```
