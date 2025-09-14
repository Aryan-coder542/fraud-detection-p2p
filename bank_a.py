import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib


class BankA:
    def __init__(self):
        self.data = None
        self.model = RandomForestClassifier(n_estimators=50, random_state=42)
        self.name = "Bank A"

    def load_data(self):
        self.data = pd.read_csv('data/bank_a_data.csv')
        print(f"{self.name}: Loaded {len(self.data)} transactions")

    def train_local_model(self):
        x = self.data[['amount', 'hour_of_day', 'day_of_week', 'account_age_days']]
        y = self.data['is_fraud']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

        self.model.fit(x_train, y_train)
        predictions = self.model.predict(x_test)

        print(f"{self.name} Model Performance:")
        print(classification_report(y_test, predictions))

        # Save model
        joblib.dump(self.model, 'bank_a_model.pkl')

        return sum(predictions)  # Return fraud signals count

    def get_fraud_patterns(self):
        # Share fraud detection patterns (not raw data)
        feature_importance = self.model.feature_importances_
        fraud_patterns = {
            'high_amount_threshold': 3000,
            'suspicious_hours': [22, 23, 0, 1, 2],
            'feature_weights': feature_importance.tolist()
        }
        return fraud_patterns


if __name__ == "__main__":
    bank = BankA()
    bank.load_data()
    fraud_count = bank.train_local_model()
    patterns = bank.get_fraud_patterns()
    print(f"Bank A detected {fraud_count} potential fraud cases")
