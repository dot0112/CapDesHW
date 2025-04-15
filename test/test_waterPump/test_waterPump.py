import RPi.GPIO as g

A_1A = 23
A_1B = 24
g.setmode(g.BCM)
g.setup(A_1A, g.OUT)
g.setup(A_1B, g.OUT)

try:
    while True:
        key = input("0 to forward, 1 to backward, s to stop, x to close: ")
        if key == "0":
            print("Forward")
            g.output(A_1A, g.HIGH)
            g.output(A_1B, g.LOW)
        elif key == "1":
            print("backward")
            g.output(A_1A, g.LOW)
            g.output(A_1B, g.HIGH)
        elif key == "s":
            print("stop")
            g.output(A_1A, g.LOW)
            g.output(A_1B, g.LOW)
        elif key == "x":
            break
except KeyboardInterrupt:
    print("\n프로그램이 강제 종료되었습니다.")
finally:
    g.output(A_1A, g.LOW)
    g.output(A_1B, g.LOW)
    g.cleanup()
    print("GPIO 리소스를 정리했습니다.")
