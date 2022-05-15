import threading
import time


def e():
    print("start e")
    # time.sleep(5)
    print("end e")


th = threading.Thread(target=e, daemon=True)
th.start()
# th.join()