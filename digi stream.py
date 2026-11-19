import random
import shutil
import sys
import time

# Minimum and maximum stream length
MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14

# Pause between each row
PAUSE = 0.1

# Characters used in the digital stream
STREAM_CHARS = ['0', '1']

# Density of digital streams
DENSITY = 0.02

# Get the terminal window width
WIDTH = shutil.get_terminal_size().columns

# Reduce width by one to avoid automatic line wrapping
WIDTH -= 1

print('Digital Stream, by Al Sweigart')
print('Press Ctrl-C to quit.')

time.sleep(2)

try:
    # Create a counter for each column
    columns = [0] * WIDTH

    while True:
        # Set up the counter for each column
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # Start a new stream
                    columns[i] = random.randint(
                        MIN_STREAM_LENGTH,
                        MAX_STREAM_LENGTH
                    )

            # Display a random 0 or 1
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')

        # Move to the next line
        print()

        # Display output immediately
        sys.stdout.flush()

        time.sleep(PAUSE)

except KeyboardInterrupt:
    print("\nDigital Stream stopped.")
    sys.exit()
