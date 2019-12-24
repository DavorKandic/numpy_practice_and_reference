import numpy as np

# np.int16 Integer (-32768 to 32767)
# np.int32 Integer (-2147483648 to 2147483647)
# np.int64 Integer (-9223372036854775808 to 9223372036854775807)

array_a = np.array([32766, 32767, 32768]) # last one is over the limit for Int16
print(array_a.dtype)  # so numpy converts them all to larger integers

# But we can force numpy to operate with int16
array_b = np.array([32766, 32767, 32768], dtype=np.int16)
print(array_b) # [ 32766  32767 -32768] Unexpected behaviour caused by overflow!

# Forced unsigned integer
array_c = np.array([-1,0,1], dtype=np.uint16)
print(array_c)    # More of unexpected behaviour!
