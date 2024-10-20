import serial
import time


# Setup serial connection
ser = serial.Serial(
    port='/dev/ttyUSB0',   # Adjust based on your device name
    baudrate=2400,         # Pelco D uses 2400 baud rate by default
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

# Pelco D command bytes for zoom in
address = 0x01      # Address of the camera (adjust if necessary)
command1 = 0x00     # No specific function in command1 for zoom
command2 = 0x00     # Command for zoom in (0x20 for zoom in, 0x40 for zoom out)
data1 = 0x00        # No need for speed here
data2 = 0x00        # No tilt or pan

# Calculate checksum
checksum = (address + command1 + command2 + data1 + data2) % 256
print(checksum)
# Create the 7-byte Pelco D packet
packet = bytearray([0xC5, address, command1, command2, data1, data2, checksum])
# Send the zoom in command
ser.write(packet)

command2 = 0x20     # Command for zoom in (0x20 for zoom in, 0x40 for zoom out)
checksum = (address + command1 + command2 + data1 + data2) % 256
packet = bytearray([0xC5, address, command1, command2, data1, data2, checksum])
ser.write(packet)
time.sleep(1)

command1 = 0x00     # No specific function in command1 for zoom
checksum = (address + command1 + command2 + data1 + data2) % 256
packet = bytearray([0xC5, address, command1, command2, data1, data2, checksum])
ser.write(packet)

# Close the serial connection
ser.close()
