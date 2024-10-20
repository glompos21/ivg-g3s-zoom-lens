import serial

# Initialize serial connection
ser = serial.Serial(
    port='/dev/ttyUSB0',   # Replace with your actual device port
    baudrate=2400,         # Default baud rate (check your device's settings)
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

# Example BiCom command to control pan/tilt
# Replace the values with the actual Bosch BiCom protocol command bytes
pan_tilt_command = bytearray([0x01, 0x12, 0x05, 0x05, 0x02, 0xFF])

# Send the command
ser.write(pan_tilt_command)

# Close the serial connection
ser.close()
