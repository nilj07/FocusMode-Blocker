import ctypes
import os
import sys

# Windows hosts file path
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

# Expanded list of common distracting websites
websites = [
    "www.instagram.com", "instagram.com",
    "www.facebook.com", "facebook.com",
    "www.youtube.com", "youtube.com",
    "www.reddit.com", "reddit.com",
    "www.twitter.com", "twitter.com", "x.com",
    "www.tiktok.com", "tiktok.com",
    "www.netflix.com", "netflix.com",
    "www.primevideo.com", "primevideo.com",
    "web.whatsapp.com", "discord.com", "www.discord.com"
]

def is_admin():
    """Check if the script is running with Administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def block_sites():
    """Injects the redirect IPs into the hosts file."""
    with open(hosts_path, 'r+') as file:
        content = file.read()
        
        # Ensure we start writing on a new line if the file doesn't end with one
        if content and not content.endswith("\n"):
            file.write("\n")
            
        for site in websites:
            if site not in content:
                file.write(f"{redirect} {site}\n")
                
    print("🛑 God Mode Activated: Distractions blocked! Get back to work.")
    flush_dns()

def unblock_sites():
    """Removes the blocked websites from the hosts file."""
    with open(hosts_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        
        for line in lines:
            # Only keep lines that do NOT contain our blocked websites
            if not any(site in line for site in websites):
                file.write(line)
                
        # Remove any leftover old content
        file.truncate()
        
    print("🟢 Normal Mode: Websites unblocked. Break time!")
    flush_dns()

def flush_dns():
    """Flushes the DNS cache so changes take effect immediately."""
    os.system("ipconfig /flushdns >nul 2>&1")

if __name__ == "__main__":
    # The hosts file requires Admin rights to modify
    if not is_admin():
        print("⚠️  Error: You need Administrator privileges to modify the hosts file.")
        print("Right-click your Command Prompt, Terminal, or IDE and select 'Run as Administrator'.")
        sys.exit()

    print("=== Focus Mode Toggle ===")
    print("1. Block Distractions")
    print("2. Unblock Distractions")
    
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        block_sites()
    elif choice == '2':
        unblock_sites()
    else:
        print("Invalid choice. Exiting.")