import pandas as pd
import numpy as np
import os


def create_bank_data(bank_name, num_transactions=1000):
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    np.random.seed(42 if bank_name == "A" else 123)

    data = {
        'transaction_id': range(1, num_transactions + 1),
        'amount': np.random.uniform(10, 5000, num_transactions),
        'hour_of_day': np.random.randint(0, 24, num_transactions),
        'day_of_week': np.random.randint(0, 7, num_transactions),
        'account_age_days': np.random.randint(1, 365, num_transactions),
        'is_fraud': np.random.choice([0, 1], size=num_transactions, p=[0.95, 0.05])
    }

    # Make fraud more detectable: high amounts at odd hours
    for i in range(num_transactions):
        if data['amount'][i] > 3000 and data['hour_of_day'][i] > 22:
            data['is_fraud'][i] = 1

    df = pd.DataFrame(data)
    df.to_csv(f'data/bank_{bank_name.lower()}_data.csv', index=False)
    return df


if __name__ == "__main__":
    # Generate data for both banks
    bank_a_data = create_bank_data("A")
    bank_b_data = create_bank_data("B")
    print("Data generated for both banks!")
