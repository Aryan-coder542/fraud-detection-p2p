import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib


class BankB:
    def __init__(self):
        self.data = pd.read_csv('data/bank_b_data.csv')
        self.model = RandomForestClassifier(n_estimators=50, random_state=123)
        self.name = "Bank B"

    def load_data(self):
        print(f"{self.name}: Loaded {len(self.data)} transactions")

    def train_local_model(self):
        x = self.data[['amount', 'hour_of_day', 'day_of_week', 'account_age_days']]
        y = self.data['is_fraud']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

        self.model.fit(x_train, y_train)
        predictions = self.model.predict(x_test)

        print(f"{self.name} Model Performance:")
        print(classification_report(y_test, predictions))

        joblib.dump(self.model, 'bank_b_model.pkl')

        return sum(predictions)

    def get_fraud_patterns(self):
        feature_importance = self.model.feature_importances_
        fraud_patterns = {
            'high_amount_threshold': 2500,
            'suspicious_hours': [21, 22, 23, 0, 1],
            'feature_weights': feature_importance.tolist()
        }
        return fraud_patterns


if __name__ == "__main__":
    bank = BankB()
    bank.load_data()
    fraud_count = bank.train_local_model()
    patterns = bank.get_fraud_patterns()
    print(f"Bank B detected {fraud_count} potential fraud cases")
