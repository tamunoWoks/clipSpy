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
