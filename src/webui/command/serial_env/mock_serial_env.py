import serial

def run_mock_serial():
    ser = serial.serial_for_url("loop://", baudrate=115200, timeout=1)
    print("Mock Serial Environment started...")

    while True:
        received = ser.readline()  # 讀取一行
        if received:
            print("Received:", received.decode().strip())
            response = f"Echo: {received.decode().strip()}\n"
            ser.write(response.encode())  # 回應相同的內容

if __name__ == "__main__":
    run_mock_serial()