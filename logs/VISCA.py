import serial

# Initialize serial connection
ser = serial.Serial(
    port='/dev/ttyUSB0',   # Your device's serial port
    baudrate=115200,         # Default VISCA baud rate
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

# VISCA command to zoom in
zoom_in_command = bytearray([0x81, 0x01, 0x04, 0x07, 0x02, 0xFF])

# Send the command
ser.write(zoom_in_command)

# Close the serial connection
ser.close()
