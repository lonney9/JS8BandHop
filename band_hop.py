#!/usr/bin/env python3
import time
from js8net import *

# Specify the wait time in seconds
# 600 is 10 minutes
wait_time = 600

# Define the list of dial values in Hz
dial_values = [3578000, 7078000, 10130000, 14078000, 28078000]

# Initialize the JS8Net connection
start_net("127.0.0.1", 2442)

# Call the get_freq() function and store the current Hz offset in a variable
# The offset is required by set_freq and this maintains the current offset when the band is changed
freq_info = get_freq()
offset = freq_info.get('offset')

while True:
    for dial_hz in dial_values:
        # Set the frequency with the current dial value
        set_freq(dial_hz, offset)

        # Convert the frequency from Hz to MHz for printing
        freq_mhz = dial_hz / 1e6  # 1 MHz = 1,000,000 Hz

        print(f"Set frequency to {freq_mhz:.4f} MHz")  # Display with 4 decimal places

        # Wait for the specified wait time in seconds
        time.sleep(wait_time)
