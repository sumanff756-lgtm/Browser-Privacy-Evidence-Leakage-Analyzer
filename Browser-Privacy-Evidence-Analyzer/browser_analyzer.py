import os
import sqlite3
import shutil

def get_chrome_history():
    user_path = os.getenv("LOCALAPPDATA")
    history_path = os.path.join(
        user_path,
        r"Google\Chrome\User Data\Default\History"
    )

    if not os.path.exists(history_path):
        print("Chrome history not found.")
        return

    temp_history = "History_copy"
    shutil.copy2(history_path, temp_history)

    conn = sqlite3.connect(temp_history)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT url, title, last_visit_time
        FROM urls
        ORDER BY last_visit_time DESC
        LIMIT 10
    """)

    print("\nRecent Browser Evidence:\n")
    for row in cursor.fetchall():
        print("URL:", row[0])
        print("Title:", row[1])
        print("-" * 50)

    conn.close()
    os.remove(temp_history)

def privacy_leak_analysis():
    suspicious_sites = ["facebook", "google", "bank", "login"]
    print("\nPrivacy Leakage Indicators:")
    for site in suspicious_sites:
        print(f"- Potential sensitive interaction detected: {site}")

if __name__ == "__main__":
    print("Browser Privacy & Evidence Leakage Analyzer")
    print("-----------------------------------------")
    get_chrome_history()
    privacy_leak_analysis()
