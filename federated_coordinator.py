from bank_a import BankA
from bank_b import BankB
from blockchain_simulator import BlockchainSimulator


class FederatedCoordinator:
    def __init__(self):
        self.blockchain = BlockchainSimulator()
        self.banks = []

    def register_bank(self, bank):
        self.banks.append(bank)
        print(f"✓ {bank.name} registered in the network")

    def coordinate_training(self):
        print("\n=== PHASE 1: LOCAL TRAINING ===")
        fraud_signals = {}

        for bank in self.banks:
            bank.load_data()
            fraud_count = bank.train_local_model()
            patterns = bank.get_fraud_patterns()

            # Share to blockchain
            self.blockchain.add_fraud_signal(bank.name, fraud_count, patterns)
            fraud_signals[bank.name] = fraud_count

        # Mine the block
        self.blockchain.mine_block()
        return fraud_signals

    def aggregate_insights(self):
        print("\n=== PHASE 2: AGGREGATING INSIGHTS ===")
        all_patterns = self.blockchain.get_all_fraud_patterns()

        if not all_patterns:
            return {}

        # Simple aggregation: average thresholds
        avg_threshold = sum(p['high_amount_threshold'] for p in all_patterns) / len(all_patterns)

        # Combine suspicious hours
        all_suspicious_hours = set()
        for p in all_patterns:
            all_suspicious_hours.update(p['suspicious_hours'])

        aggregated_knowledge = {
            'consensus_amount_threshold': avg_threshold,
            'consensus_suspicious_hours': list(all_suspicious_hours),
            'participating_banks': len(all_patterns)
        }

        print(f"✓ Aggregated knowledge from {len(all_patterns)} banks")
        print(f"  • Consensus fraud threshold: ${avg_threshold:,.2f}")
        print(f"  • Suspicious hours: {sorted(list(all_suspicious_hours))}")

        return aggregated_knowledge

    def display_results(self):
        self.blockchain.display_blockchain()


# Main execution
if __name__ == "__main__":
    coordinator = FederatedCoordinator()

    # Register banks
    coordinator.register_bank(BankA())
    coordinator.register_bank(BankB())

    # Run federated learning process
    fraud_signals = coordinator.coordinate_training()
    insights = coordinator.aggregate_insights()
    coordinator.display_results()

    print("\n=== SUMMARY ===")
    print("✓ Banks trained models locally (data never shared)")
    print("✓ Fraud patterns shared via blockchain")
    print("✓ Consensus knowledge generated")
    print("✓ All transactions logged and auditable")
