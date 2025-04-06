import argparse
import requests

def scan_subdomains(domain, wordlist_path):
    with open(wordlist_path, 'r') as file:
        subdomains = file.read().splitlines()

    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code < 400:
                print(f"[+] Found: {url}")
        except requests.RequestException:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Subdomain Scanner")
    parser.add_argument("domain", help="Target domain (e.g., example.com)")
    parser.add_argument("wordlist", help="Path to wordlist file")
    args = parser.parse_args()

    scan_subdomains(args.domain, args.wordlist)