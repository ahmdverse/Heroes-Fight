# 🥊 Heroes Fight Game

A simple turn-based fighting game built with **Python**, demonstrating core **Object-Oriented Programming (OOP)** concepts.

## 🚀 Project Overview
In this game, a **Hero** battles against an **Enemy** in a loop until one of them runs out of health. The project simulates a battle system with different attack mechanisms for each character type.

## 🛠️ Concepts Applied
This project was built to practice and demonstrate the following OOP principles:
- **Classes & Objects**: Creating blueprints for `Hero` and `Enemy`.
- **Inheritance**: Both characters inherit from a base `Fighter` class.
- **Abstraction**: Using `ABC` (Abstract Base Classes) to enforce the implementation of the `attack` method.
- **Polymorphism**: The `attack` method behaves differently for a `Hero` (uses weapon) vs. an `Enemy` (uses raw damage).
- **Type Hinting**: Using Python's typing system for better code clarity and error checking.

## 📂 Class Structure
- `Fighter` (Abstract Base Class)
  - `Hero` (Child Class) -> Uses Weapons ⚔️
  - `Enemy` (Child Class) -> Uses Damage Power 👹

## 💻 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/ahmdverse/Heroes-Fight.git](https://github.com/ahmdverse/Heroes-Fight.git)
