
import csv
from pathlib import Path

import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = Path("data") / "users.csv"


def extract_users():
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()
    return response.json()


def transform_users(users):
    cleaned_users = []

    for user in users:
        cleaned_users.append({
            "user_id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"],
            "username": user["username"],
            "company_name": user["company"]["name"]
        })

    return cleaned_users


def load_users(users):
    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_FILE.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["user_id", "name", "email", "city","username","company_name"],
        )
        writer.writeheader()
        writer.writerows(users)

def count_missing_emails(users):
    return sum(
        1 for user in users
        if not (user.get("email") or "").strip()
    )


def main():
    print("Extracting API data...")
    raw_users = extract_users()

    print("Transforming records...")
    cleaned_users = transform_users(raw_users)

    missing_email_count = count_missing_emails(cleaned_users)
    print(f"Records with missing or empty emails: {missing_email_count}")

    print("Saving CSV...")
    load_users(cleaned_users)

    print(f"Processed {len(cleaned_users)} users")


if __name__ == "__main__":
    main()
