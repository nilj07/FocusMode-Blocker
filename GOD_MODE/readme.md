# 🛑 God Mode: Website Blocker

A lightweight Python script designed to help you regain your focus and block out distractions. By modifying the Windows `hosts` file, this script prevents access to popular time-sinking websites (like Instagram, YouTube, Reddit, and Netflix) and easily toggles them back on when your work is done.

## ✨ Features
* **Interactive Menu:** Easily toggle "Focus Mode" on or off without manually editing system files.
* **Auto-DNS Flush:** Automatically clears your DNS cache so website blocks (and unblocks) take effect instantly in your browser.
* **Admin Verification:** Checks for Administrator privileges before running to prevent annoying crash errors.
* **Customizable:** Simple to add or remove websites from the blocklist directly in the code.

## ⚠️ Prerequisites
* **Windows OS:** This script is specifically configured for the Windows `hosts` file (`C:\Windows\System32\drivers\etc\hosts`).
* **Python 3.x:** Ensure Python is installed on your machine.

## 🚀 Usage

**CRITICAL:** Because this script modifies a system file, you **must** run it as an Administrator.

1. Clone or download this repository.
2. Open your Command Prompt, PowerShell, or Terminal **as Administrator** (Right-click -> "Run as Administrator").
3. Navigate to the directory where the script is located.
4. Run the script:
   ```bash
   python focus_mode.py
   ```
5. Follow the on-screen prompts to either block (1) or unblock (2) the configured websites.

## 🛠️ How to Add Your Own Websites
Open `focus_mode.py` in any text editor and find the `websites` list at the top of the file. Simply add the URLs you want to block. 
*Note: It is highly recommended to add both the `www.` and non-`www.` versions of the domain.*

```python
websites = [
    "www.example.com", "example.com",
    # Add yours here!
]
```

## 📜 Disclaimer
This script modifies the system `hosts` file. While it is designed to safely append and remove its own entries, it is always a good practice to create a manual backup of your `hosts` file (`C:\Windows\System32\drivers\etc\hosts`) before running scripts that modify it.