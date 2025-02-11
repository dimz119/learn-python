# brew install llvm@18
# export PATH="/opt/homebrew/opt/llvm@18/bin:$PATH"
# export CC="/opt/homebrew/opt/llvm@18/bin/clang"
# export CXX="/opt/homebrew/opt/llvm@18/bin/clang++"
# export LDFLAGS="-L/opt/homebrew/opt/llvm@18/lib"
# export CPPFLAGS="-I/opt/homebrew/opt/llvm@18/include"
# export CMAKE_PREFIX_PATH="/opt/homebrew/opt/llvm@18"
# PYTHON_CONFIGURE_OPTS='--enable-experimental-jit' pyenv install 3.13.0t
# python -m sysconfig | grep jit
import sys
import time

print("Python Version:", sys.version)

def compute():
    return sum(i**2 for i in range(10**8))

start = time.time()
compute()
end = time.time()

print(f"Execution time: {end - start:.4f} seconds")

# Python Version: 3.13.0 (main, Feb 10 2025, 20:45:18) [Clang 16.0.0 (clang-1600.0.26.4)]
# Execution time: 5.9568 seconds
# Python Version: 3.13.0 experimental free-threading build (main, Feb 10 2025, 21:33:56) [Clang 18.1.8 ]
# Execution time: 5.8512 seconds
