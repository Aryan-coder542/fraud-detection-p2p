from generate_data import create_bank_data
from federated_coordinator import FederatedCoordinator
from bank_a import BankA
from bank_b import BankB
import os


def main():
    print("🏦 P2P FRAUD DETECTION: DECENTRALIZED AI DEMO 🏦\n")

    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)

    # Step 1: Generate sample data
    print("Step 1: Generating sample transaction data...")
    create_bank_data("A")
    create_bank_data("B")

    # Step 2: Run federated learning
    print("\nStep 2: Starting decentralized AI coordination...")
    coordinator = FederatedCoordinator()
    coordinator.register_bank(BankA())
    coordinator.register_bank(BankB())

    # Step 3: Execute the process
    fraud_signals = coordinator.coordinate_training()
    insights = coordinator.aggregate_insights()
    coordinator.display_results()

    print("\n🎉 DEMO COMPLETE! 🎉")
    print("Key achievements:")
    print("• Privacy preserved (no raw data shared)")
    print("• Collaborative fraud detection improved")
    print("• Blockchain provides transparency and trust")
    print("• Scalable to many banks")


if __name__ == "__main__":
    main()
