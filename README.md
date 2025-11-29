## Clipboard Monitor
This Python script monitors your system clipboard in real time and prints any detected changes. It is useful for debugging, research, productivity workflows, or tracking copy events during text extraction tasks.

### Features:
-   **Real-time monitoring** of clipboard changes
-   **Prints clipboard contents** whenever they change
-   **Counts total clipboard events**
-   Stops cleanly using **Ctrl+C**
-   Adjustable scan interval (default: 0.1 seconds)

### Requirements:
Make sure you have the following Python packages installed:
``` bash
pip install pyperclip
```
`pyperclip` supports clipboard access across Windows, macOS, and Linux (requires `xclip` or `xsel` on some Linux distributions).

### Usage:
Run the script using Python:
``` bash
python monitor_clipboard.py
```
Once running, the terminal will display messages similar to:

    --- Clipboard Change #1 ---
    Hello world
    ----------------------------------------
To stop monitoring, press:
    Ctrl + C

### How It Works:
The script repeatedly checks the current clipboard contents using `pyperclip.paste()` and compares it against the last observed value. If a change is detected:
- It increments an internal counter
- Prints the new clipboard contents
- Logs a separator line for readability.  

The monitor pauses for **0.1 seconds** per loop to reduce CPU usage.

### Script:
``` python
import pyperclip
import time

def monitor_clipboard():
    print('Recording clipboard... (Ctrl-C to stop)')
    previous_content = ''
    change_count = 0

    try:
        while True:
            content = pyperclip.paste()
            if content != previous_content:
                change_count += 1
                print(f"
--- Clipboard Change #{change_count} ---")
                print(content)
                print("-" * 40)
                previous_content = content
            time.sleep(0.1)  # Reduced frequency to 0.1s to be less resource-intensive

    except KeyboardInterrupt:
        print(f"
Stopped. Total clipboard changes recorded: {change_count}")

if __name__ == "__main__":
    monitor_clipboard()
```
