
from datetime import datetime, timezone

def run_pipeline():
    print("Starting data pipeline...")

    started_at = datetime.now(timezone.utc)
    print(f"Start time (UTC): {started_at.isoformat()}")

    records = [
        {"id": 101, "amount": 5000},
        {"id": 102, "amount": 7500},
        {"id": 103, "amount": 3200},
    ]

    total_amount = sum(record["amount"] for record in records)

    print(f"Records processed: {len(records)}")
    print(f"Total amount: {total_amount}")
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()
