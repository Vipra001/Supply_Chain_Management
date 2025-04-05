import hashlib
import time
import json
import pandas as pd

class Block:
    def __init__(self, index, product_id, batch_info, location, sender, receiver, action, previous_hash):
        self.index = index
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.product_id = product_id
        self.batch_info = batch_info
        self.location = location
        self.sender = sender
        self.receiver = receiver
        self.action = action
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(
            index=0,
            product_id="0",
            batch_info={"name": "Genesis Block", "quantity": "0", "expiry": "N/A"},
            location="N/A",
            sender="N/A",
            receiver="N/A",
            action="Blockchain Initiated",
            previous_hash="0"
        )
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, product_id, batch_info, location, sender, receiver, action):
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            product_id=product_id,
            batch_info=batch_info,
            location=location,
            sender=sender,
            receiver=receiver,
            action=action,
            previous_hash=last_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.compute_hash():
                return False

            if current.previous_hash != previous.hash:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(f"\nIndex: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Product ID: {block.product_id}")
            print(f"Batch Info: {block.batch_info}")
            print(f"Location: {block.location}")
            print(f"Sender: {block.sender}")
            print(f"Receiver: {block.receiver}")
            print(f"Action: {block.action}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Current Hash: {block.hash}")

    def export_to_excel(self, filename="supply_chain_data.xlsx"):
        data = []
        for block in self.chain:
            data.append({
                "Index": block.index,
                "Timestamp": block.timestamp,
                "Product ID": block.product_id,
                "Batch Name": block.batch_info.get("name"),
                "Quantity": block.batch_info.get("quantity"),
                "Expiry": block.batch_info.get("expiry"),
                "Location": block.location,
                "Sender": block.sender,
                "Receiver": block.receiver,
                "Action": block.action,
                "Previous Hash": block.previous_hash,
                "Hash": block.hash
            })
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        print(f"\nData exported to {filename}")


# Example Usage
if __name__ == "__main__":
    sc_chain = Blockchain()

    # Simulate events in supply chain
    sc_chain.add_block(
        product_id="FOOD123456",
        batch_info={"name": "Organic Rice", "quantity": "500kg", "expiry": "2025-12-30"},
        location="Farm A, Haryana, India",
        sender="Farmer Co.",
        receiver="Distributor X",
        action="Dispatched from farm"
    )

    sc_chain.add_block(
        product_id="FOOD123456",
        batch_info={"name": "Organic Rice", "quantity": "500kg", "expiry": "2025-12-30"},
        location="Warehouse B, Delhi",
        sender="Distributor X",
        receiver="Retailer Y",
        action="Stored in warehouse"
    )

    sc_chain.add_block(
        product_id="FOOD123456",
        batch_info={"name": "Organic Rice", "quantity": "500kg", "expiry": "2025-12-30"},
        location="Retail Store Z, Delhi",
        sender="Warehouse B",
        receiver="Customer",
        action="Delivered to customer"
    )

    # Display blockchain and export to Excel
    sc_chain.display_chain()
    print("\nIs Blockchain valid?", sc_chain.is_chain_valid())
    sc_chain.export_to_excel()
