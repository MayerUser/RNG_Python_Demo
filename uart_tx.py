import serial
import time
import random

serial_port = 'COM1'
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
                            timeout=1)
        for i in range(100):
            # Send data
            RNG_Num = int(random.random()*65536) #Generate a 16 bits Random Number;
            # Send High Byte
            ser.write(int.to_bytes(RNG_Num//256)) #Send High Byte;
            # Send Low Byte
            ser.write(int.to_bytes(RNG_Num%256))  #Send Low Byte;
            print("Tx:",RNG_Num)

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