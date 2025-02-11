import sys
import threading

print("Python Version:", sys.version)

import threading
import time

def compute():
    sum(i**2 for i in range(10**7))

start = time.time()

thread1 = threading.Thread(target=compute)
thread2 = threading.Thread(target=compute)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

end = time.time()
print(f"Execution time: {end - start:.4f} seconds")

# Python Version: 3.13.0 experimental free-threading build (main, Feb 10 2025, 20:46:56) [Clang 16.0.0 (clang-1600.0.26.4)]
# Execution time: 0.5695 seconds
# Python Version: 3.13.0 (main, Feb 10 2025, 20:45:18) [Clang 16.0.0 (clang-1600.0.26.4)]
# Execution time: 1.1237 seconds