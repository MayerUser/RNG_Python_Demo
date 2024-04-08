import serial

# Replace 'COM2' with your serial port name
serial_port = 'COM2'
baud_rate = 9600
parity = serial.PARITY_NONE
stop_bits = serial.STOPBITS_ONE
bytesize = serial.EIGHTBITS

def main():
    try:
        # Initialize serial connection
        ser = serial.Serial(port=serial_port, 
                            baudrate=9600, 
                            parity=parity, 
                            stopbits=stop_bits, 
                            bytesize=bytesize,
                            timeout=None)
        # Receive 100 Byte
        for i in range(100):
            rx_data1 = int.from_bytes(ser.read()) #Receive High Bytes;
            rx_data2 = int.from_bytes(ser.read()) #Receive Low  Bytes;
            print("RX:",rx_data1 * 256 + rx_data2)
        
    except serial.SerialException as e:
        print(f"Error opening the serial port: {e}")

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

    finally:
        # Close the serial connection
        if 'ser' in locals() or 'ser' in globals():
            ser.close()
            print("Serial connection closed.")

if __name__ == "__main__":
    main()