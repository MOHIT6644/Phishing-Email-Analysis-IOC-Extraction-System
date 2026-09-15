from pathlib import Path
import re

def main():

    base_dir = Path(__file__).resolve().parents[2]

    email_file = base_dir / "Emails" / "phishing_email.txt"

    with open(email_file, "r", encoding="utf-8") as f:
        email_content = f.read()

    print("===== EMAIL ANALYSIS =====")

    urls = re.findall(r'https?://\S+', email_content)

    suspicious_domains = []

    for url in urls:
        suspicious_domains.append(url)

    print("\nDetected URLs:")
    for url in suspicious_domains:
        print(url)

    print("\n===== IOC EXTRACTION =====")

    for url in suspicious_domains:
        print(f"IOC: {url}")

    report_path = base_dir / "IOC_Report" / "ioc_report.txt"

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("IOC REPORT\n")
        report.write("====================\n")

        for url in suspicious_domains:
            report.write(f"URL: {url}\n")

if __name__ == "__main__":
    main()
