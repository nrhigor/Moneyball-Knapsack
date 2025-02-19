# Moneyball Knapsack

## 📌 Project Overview

This project implements an optimization algorithm for selecting players for a football team within a given budget. The approach is based on the **0/1 Knapsack Problem**, a well-known combinatorial optimization problem. 
The goal is to maximize the choices from a given list by selecting the best players while staying within the financial constraints.
The idea was inspired by the **"Moneyball"** strategy, where data analysis is used to make cost-effective decisions in sports team formation.

## 🚀 How It Works

1. **Data Input**: A CSV file containing mockup data of football players with their attributes, including:
   - Market Value
   - Position
   - Injury tolerance
   - Extra-field factor
   - Overall

2. **Optimization Algorithm**:
   - The algorithm reads the player data and stores it in a custom `Player` class.
   - It calculates a **"player value"** based on multiple attributes.
   - Using **dynamic programming**, it determines the optimal set of players that maximize team value while staying within the budget.

3. **Mathematical Model**:
   - The solution is based on the following recurrence relation:

     $$f(i, p) = f(i - 1, p) \quad \text{if } p_i > p$$

     $$f(i, p) = \max(f(i - 1, p - p_i) + v_i , f(i - 1, p)) \quad \text{if } p_i \leq p$$

   - Where:
     - $$p$$ is the total budget.
     - $$i$$ represents the $$i$$-th player.
     - $$p_i$$ is the cost of player $$i$$.
     - $$v_i$$ is the calculated value of player $$i$$.

## 📂 Usage Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Moneyball-Knapsack.git
   cd Moneyball-Knapsack
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python main.py
   ```

## 🏆 Limitations
⚠️ The current implementation does not support **position-based filtering** (e.g., selecting only defenders and goalkeepers).  
⚠️ The script requires the user to manually update file paths in the code.
