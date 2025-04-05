Blockchain-Based Supply Chain Tracker

Overview

This project implements a Blockchain-Based Supply Chain Tracking System using Python. It simulates the journey of products through different supply chain stages (e.g., farm, warehouse, customer), records each step on a blockchain, and allows exporting the full chain to an Excel file for transparency and analysis.

Features 🚀

✅ Custom-built Block and Blockchain classes

✅ Each block stores supply chain data (location, timestamp, product info)

✅ Chronological tracking of events: Farm → Warehouse → Customer

✅ Export the blockchain to Excel for easy sharing/reporting

Technologies Used 💻

Python 3.x

pandas for data export

datetime for timestamps

No external blockchain libraries used – built from scratch for educational clarity.

How It Works ⚖️

A new blockchain is created with a Genesis Block.

Each product movement is recorded as a block with details like:

Location (Farm, Warehouse, Customer)

Timestamp

Product Name / Description

The entire chain is saved to supply_chain_blockchain.xlsx.

Setup ⚙️

Clone this repo:

git clone https://github.com/Vipra001/SupplyChain_Blockchain.git
cd SupplyChain_Blockchain

Install dependencies:

pip install pandas

Run the Python script:

python supply_chain_tracker.py

Output 📄

A file named supply_chain_blockchain.xlsx containing:

Block Number

Timestamp

Previous Hash

Current Hash

Location (e.g., Farm, Warehouse)

Product Details

Use Case Examples 🌾🏢🏦

Tracking perishable goods like vegetables or meat

Monitoring electronics delivery across cities

Ensuring transparency for customers in e-commerce

Hashtags 🔖

#Blockchain #SupplyChain #Python #Logistics #Traceability #Transparency #ExcelExport #EducationalBlockchain #Web3 #Decentralization

🔥 Created with purpose by Vipra Sharma 🚀

