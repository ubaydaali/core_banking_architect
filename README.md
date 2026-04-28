# HYDRA Core-Banking Settlement & SWIFT Gateway 🏦🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![COBOL](https://img.shields.io/badge/Language-COBOL-blue.svg)](#)
[![Python](https://img.shields.io/badge/Language-Python-green.svg)](#)
[![Security](https://img.shields.io/badge/Architecture-Zero--Trust-red.svg)](#)

## 🏗️ Executive Overview

**HYDRA** is a high-performance, hybrid architectural framework designed to bridge the gap between mission-critical legacy COBOL environments and modern cloud-native ecosystems. 

In the financial sector, billions of lines of COBOL code still process the world's most sensitive data. **HYDRA** demonstrates a "Modernize-in-Place" strategy, wrapping a high-integrity COBOL settlement engine within a secured Python orchestration layer. This approach unlocks cloud agility, real-time analytics, and modern interoperability without compromising the unmatched precision of mainframe-grade processing.

---

## 🏛️ System Architecture

The project implements a **Sequential Master File Update (Balance Line Algorithm)**—the gold standard for batch financial processing—orchestrated through a modern Python/Streamlit interface.

### 1. The Core Engine (Legacy Layer)
* **Language:** GnuCOBOL (Standard-compliant).
* **Logic:** Implements multi-file synchronization (Master, Transactions, Exchange Rates).
* **Performance:** Optimized for sub-millisecond sequential processing, achieving execution speeds unreachable by standard interpreted languages.

### 2. The Orchestration Layer (Modern Bridge)
* **Language:** Python 3.x.
* **Function:** Acts as a **Zero-Trust Gateway**. It handles file I/O, process monitoring, and real-time data extraction from COBOL output buffers.
* **Visualization:** Streamlit-powered dashboard providing executive-level metrics and compliance audit logs.

### 3. Security & Compliance (Zero-Trust Design)
* **PII Masking:** Automated PII (Personally Identifiable Information) anonymization occurs at the source level. Names and IDs are masked during processing (e.g., `OBEIDA` ➡️ `O****A`) to ensure data privacy before it reaches any cloud-facing interface.
* **Encryption:** Integration-ready for AES-256 data-at-rest encryption protocols.

---

## 🛠️ Key Enterprise Features

* **High-Integrity Settlement:** Reliable balance updates using historical banking algorithms.
* **SWIFT Gateway:** Automated generation of standard **SWIFT MT103** messages for international credit transfers.
* **Cloud-Native Deployment:** Engineered for seamless execution on Linux-based cloud containers (Streamlit Cloud, Docker) using native GnuCOBOL compilers.
* **Real-time Audit Trails:** Comprehensive reporting with automated discrepancy detection (negative balances, invalid IDs).

---

## 🚀 Getting Started

### Prerequisites
* **GnuCOBOL** (via MSYS2 for Windows or `apt-get install gnucobol` for Linux).
* **Python 3.x** with `streamlit`.

### Local Execution
1. Clone the repository.
2. Compile the engine: 
   ```bash
   cobc -x -free -o cobol_engine/hydra_core src/hydra_core.cbl


## 🌐 Live Demo & Source Code

Experience the speed and security of the HYDRA Engine in real-time. The cloud-native dashboard demonstrates the sub-millisecond execution of the COBOL backend alongside automated PII masking.

* **Live Interactive Dashboard:** [HYDRA Cloud Demo](https://corebankingarchitect.streamlit.app/)
* **Source Code & Architecture:** [GitHub Repository](https://github.com/ubaydaali/core_banking_architect/tree/main)

---
