import argparse
from scanner.sql_injection import check_sql_injection
from scanner.xss_scanner import check_xss
from scanner.csrf_checker import check_csrf

def main():
    parser = argparse.ArgumentParser(description="Web Application Security Testing Toolkit")
    parser.add_argument("--url", required=True, help="Target website URL to scan")
    args = parser.parse_args()

    target_url = args.url
    print(f"🔍 Scanning {target_url} for vulnerabilities...\n")

    check_sql_injection(target_url)
    check_xss(target_url)
    check_csrf(target_url)

    print("\n✅ Scan complete. Report saved in /reports folder.")

if _name_ == "_main_":
    main()
