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
