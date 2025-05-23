# 🥗 Personalized Nutrition and Fitness Recommendation Engine

Welcome to the **Personalized Nutrition and Fitness Recommendation Engine**, a Java-based academic project emphasizing clean software architecture, key design patterns, and intelligent search algorithms for user-centric health recommendations.

> 📚 Developed as part of our **second-semester Java and Data Structures course**.

---

## 🚀 Project Goals

This project is not a complete frontend/backend system but showcases how to design scalable and maintainable software using:

- ✅ **Clean Architecture**
- ✅ **MVC (Model-View-Controller) Pattern**
- ✅ **Singleton Design Pattern**
- ✅ **Jaro-Winkler String Similarity Algorithm**

---

## 🏗️ Architecture Overview

### Clean Architecture
The project is structured into different layers to promote separation of concerns:

- **Entities (Core Models)**
- **Use Cases / Services**
- **Interfaces (CLI Input, Search, etc.)**
- **Frameworks & Drivers (Main class)**
- ---
![WhatsApp Image 2025-04-06 at 13 13 26](https://github.com/user-attachments/assets/151e4a84-5d4d-42d2-aaf3-2205e551df0e)

### MVC Pattern
We applied the MVC pattern to separate:
- `Model`: Nutrition and fitness data classes
- `View`: Routes handling 
- `Controller`: Handles the logic (ex:user already exist or not)
![DSA_Project drawio](https://github.com/user-attachments/assets/705897a5-6493-44b6-89be-1e112f727a87)





## 🔍 Key Features

> 🧪 **Note:** The user interface (UI) is currently under development. A Command Line Interface (CLI) is used for demonstration purposes.

### 🔸 Jaro-Winkler Algorithm
Utilized to provide intelligent approximate search for food items or fitness terms.  
> Example: Typing "appl" will match "apple" using similarity scoring.

### 🔸 Singleton Pattern
Applied in configuration/service classes to ensure a single instance throughout the application (e.g., Recommendation Engine).

### 🔸 User Input System
A simple CLI that:
- Accepts user input like food preferences or fitness goals
- Suggests recommendations based on input and search matching

---

## 🧠 Algorithms & Patterns Used

| Pattern/Algorithm       | Purpose                                      |
|-------------------------|----------------------------------------------|
| Singleton               | Ensure a single instance of key components   |
| MVC                     | Clear separation of logic, data, and UI      |
| Clean Architecture      | Organized, scalable, maintainable structure  |
| Jaro-Winkler Algorithm  | Fuzzy matching for more user-friendly search |

---


