import requests
import sys
from urllib.parse import urlparse

def print_banner():
    print("-" * 60)
    print("      ★ Simple Vulnerability & Misconfiguration Scanner ★      ")
    print("             For Educational & Authorized Testing Only         ")
    print("-" * 60)

def check_vulnerabilities(target_url):
    if not target_url.startswith('http://') and not target_url.startswith('https://'):
        target_url = 'http://' + target_url
    
    print(f"\n[+] Starting scan on: {target_url}\n")
    
    sensitive_paths = [
        '.env',          
        'robots.txt',     
        '.git/HEAD',     
        'wp-admin/',     
        'config.php.bak' 
    ]
    
    print("[*] Checking for exposed sensitive files and directories...")
    for path in sensitive_paths:
        scan_url = f"{target_url.rstrip('/')}/{path}"
        try:
            response = requests.get(scan_url, timeout=3, allow_redirects=False)
            if response.status_code == 200:
                print(f" [!] WARNING: Sensitive path exposed: {scan_url} (Status: 200 OK)")
            elif response.status_code == 403:
                print(f" [i] Found protected path: {scan_url} (Status: 403 Forbidden)")
        except requests.exceptions.RequestException:
            continue

    print("\n[*] Analyzing Security Headers...")
    try:
        response = requests.get(target_url, timeout=3)
        headers = response.headers
        
        important_headers = [
            'X-Frame-Options',          
            'X-Content-Type-Options',   
            'Content-Security-Policy'   
        ]
        
        for header in important_headers:
            if header not in headers:
                print(f" [!] MISSING HEADER: {header} is not set! (High Risk for Web Attacks)")
            else:
                print(f" [✓] SECURE: {header} is active.")
                
    except requests.exceptions.RequestException as e:
        print(f" [X] Error connecting for Header Analysis: {e}")

def main():
    print_banner()
    
    while True:
        try:
            user_input = input("\nEnter target URL/IP (or type 'exit' to quit): ").strip()
            
            if user_input.lower() == 'exit':
                print("\nExiting Scanner. Stay safe!")
                break
                
            if not user_input:
                print("[X] Please enter a valid target.")
                continue
                
            check_vulnerabilities(user_input)
            print("\n" + "="*60)
            
        except KeyboardInterrupt:
            print("\n\nExiting Scanner. Stay safe!")
            sys.exit()

if __name__ == "__main__":
    main()
