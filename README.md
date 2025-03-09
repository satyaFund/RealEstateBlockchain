# Blockchain Real Estate Investment Token (REIT)

**Author:** Nicholas Coram  
**Date:** February 5, 2025  
**IDE Share Link:** [Programiz Online Compiler](https://www.programiz.com/online-compiler/6EGajS7cRk9rp)

---

## Project Overview

Traditional real estate transactions often suffer from inefficiencies, high costs, and security vulnerabilities due to manual processes and multiple intermediaries. This blockchain-powered platform addresses these issues by using a cryptocurrency-based model called Real Estate Investment Tokens (REIT).

### Problem Definition
- High entry costs and lengthy processes in real estate investment.
- Risks of human error, fraud, and disputes in traditional title transactions.

### Solution
This project implements an automated market maker (AMM) platform, inspired by Uniswap, allowing users to trade fractional ownership of properties securely and transparently using blockchain technology. Transactions are recorded securely through Python-based hashing functions, enhancing integrity and trust.

---

## Features & Functionalities

### Key Features
- **Blockchain Ledger**: Securely records transactions using cryptographic hashes.
- **Fractional Ownership:** Enables the trading of property shares using the fictional cryptocurrency REIT.
- **Dynamic Pricing Model:** Share prices automatically adjust according to supply and demand.

### Pricing Model
- **Starting Price:** `P₀ = (Property Price ÷ 100,000) × 0.98`
- **Final Price:** `P_f = (Property Price ÷ 100,000) × 1.02`
- **Current Share Price:** `y = P₀ + ((P_f - P₀) × (100,000 - x) ÷ 100,000)`  
  *(where x = shares remaining, y = current share price)*

---

## Features Demonstrated

### User Creation
- Users create an account and receive an initial amount of REIT.
- Account creation and funding are recorded on the blockchain.

### Property Listing
- Properties listed with a defined number of shares and initial pricing.
- Shares and pricing dynamically update as trading occurs.

### Buying and Selling Shares
- Users purchase and sell shares with automatic account balance adjustments.
- Transactions and price adjustments securely recorded and updated in the blockchain.

---

## Implementation Details

### Blockchain Technology
- Cryptographic hashing links each block to the previous, ensuring security and transparency.

### User Interface
- Real-time balance and transaction history updates.
- Intuitive, user-friendly interaction for trading and portfolio management.

---

## Testing and Validation
- Verified blockchain integrity and linkage.
- Confirmed correct account creation, property listings, transactions, and pricing adjustments.
- Tested edge cases including insufficient balances and share availability limits.

---

## Future Enhancements
- Enhanced UI/UX improvements.
- Further security optimizations.
- Expanded data integration and external data sourcing.

---

**Developed by Nicholas Coram, February 2025**

