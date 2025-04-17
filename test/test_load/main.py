import keyboard
import threading
import time
import module

eventList = [0, 0, 0, 0, 0, 0]
eventLock = threading.Lock()


def on_key(event):
    if event.name.isdigit():
        num = int(event.name)
        if 0 <= num <= 5:
            with eventLock:
                eventList[num] = (eventList[num] + 1) % 2


def key_listener():
    keyboard.on_press(on_key)
    keyboard.wait("esc")


def main():
    listener_thread = threading.Thread(target=key_listener, daemon=True)
    listener_thread.start()

    try:
        while listener_thread.is_alive():
            with eventLock:
                module.printCliMessage(eventList.copy())
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()
