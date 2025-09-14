from datetime import datetime


class BlockchainSimulator:
    def __init__(self):
        self.blocks = []
        self.pending_transactions = []

    def add_fraud_signal(self, bank_id, fraud_count, patterns):
        transaction = {
            'timestamp': datetime.now().isoformat(),
            'bank_id': bank_id,
            'fraud_signals_shared': fraud_count,
            'patterns_shared': patterns,
            'transaction_type': 'FRAUD_SIGNAL_SHARE'
        }
        self.pending_transactions.append(transaction)
        print(f"✓ {bank_id} shared {fraud_count} fraud signals to blockchain")

    def mine_block(self):
        if not self.pending_transactions:
            return

        block = {
            'block_number': len(self.blocks) + 1,
            'timestamp': datetime.now().isoformat(),
            'transactions': self.pending_transactions.copy(),
            'previous_hash': self.get_previous_hash()
        }

        self.blocks.append(block)
        self.pending_transactions = []
        print(f"✓ Block #{block['block_number']} mined with {len(block['transactions'])} transactions")

    def get_previous_hash(self):
        if len(self.blocks) == 0:
            return "0000000000000000"
        return f"hash_{len(self.blocks)}"

    def get_all_fraud_patterns(self):
        all_patterns = []
        for block in self.blocks:
            for tx in block['transactions']:
                if tx['transaction_type'] == 'FRAUD_SIGNAL_SHARE':
                    all_patterns.append(tx['patterns_shared'])
        return all_patterns

    def display_blockchain(self):
        print("\n=== BLOCKCHAIN LEDGER ===")
        for block in self.blocks:
            print(f"Block #{block['block_number']} - {block['timestamp']}")
            for tx in block['transactions']:
                print(f"  • {tx['bank_id']}: {tx['fraud_signals_shared']} fraud signals")
        print("========================\n")
