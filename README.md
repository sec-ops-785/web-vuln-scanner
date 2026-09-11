# Web Vulnerability Scanner

A reusable Python CLI script designed to scan web servers for common OWASP Top 10 vulnerabilities and misconfigurations.

## Features & Mechanics
- **Exposed Sensitive Files:** Automatically checks for exposed configuration and backup paths (`.env`, `.git/HEAD`, `robots.txt`, `wp-admin/`, `config.php.bak`) via HTTP status code analysis.
- **Security Headers Analyzer:** Inspects the server's HTTP response headers for missing security mechanisms (`X-Frame-Options`, `X-Content-Type-Options`, `Content-Security-Policy`).
- **Interactive Multi-Target Mode:** Runs continuously using a repetitive loop to scan multiple targets in a single session until `exit` is triggered.

## Usage
```bash
pip install requests
python vuln_scanner.py
```

*Disclaimer: Authorized security testing only. Scanning without consent is illegal.*
