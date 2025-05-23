# 🛍️ Minimalistic e-Commerce Store with Streamlit

## 🚀 Objective

Develop a minimalistic, data-driven e-commerce application using **Streamlit**. This project integrates three databases — **MongoDB**, **Redis**, and **Neo4j** — each responsible for a specific aspect of the app:

- **MongoDB**: Product and purchase data storage  
- **Redis**: Shopping cart functionality and caching  
- **Neo4j**: Graph-based product recommendations  

All components are connected using **Python**, with a Streamlit-based UI for visualization.

---

## 🧩 Components & Responsibilities

### 📦 MongoDB
- Stores product information.
- Loads product data into the app.
- Saves purchase data after checkout.

### 🧠 Neo4j
- Models product relationships as a graph.
- Generates product recommendations using Cypher queries.

### ⚡ Redis
- Stores shopping cart data temporarily.
- Caches recommendations to improve performance.

### 🐍 Python API
- Serves as the glue between all components.
- Interfaces with databases and provides recommendation endpoints.

---

## 📝 Introduction

This guide helps you set up and run a Streamlit-based e-commerce app with a multi-database backend. While a production-grade application would include a full API layer, this MVP focuses on visualizing the system via **Streamlit** for faster feedback and iteration.

---

## 🔧 Prerequisites

Make sure you have the following installed:
- Python 3.x
- Python packages: `streamlit`, `pymongo`, `redis`, `neo4j`, `pandas`
- Local installations of MongoDB, Redis, and Neo4j (or use cloud versions like MongoDB Atlas, Redis Cloud, and Neo4j AuraDB)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/e_commerce_app.git
cd e_commerce_app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```⌢渠彯煳彬慤慴慢敳彳捥浯獟潴敲•਍