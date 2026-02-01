<img width="1092" height="655" alt="image" src="https://github.com/user-attachments/assets/aa4135d5-6a2b-4453-b1a9-27f99fe740df" />

# 🏯 Dojo: Implementation Hub for Concept Learning

Welcome to **Dojo**, a curated repository of foundational scripts designed for rapid implementation, conceptual clarity, and academic study. This repository serves as a personal "training hall" where complex mathematical, computational, and quantum theories are distilled into clean, executable Python code.

---

## 💡 The Idea Behind the Code

Dojo was created with a clear philosophy: **theory becomes meaningful through implementation**. Each script in this repository transforms abstract concepts from textbooks and research papers into tangible, executable code that you can run, modify, and understand.

The core principles guiding this project are:

- **Learn by Doing**: Reading about algorithms is valuable, but implementing them solidifies understanding
- **Quick Experimentation**: All scripts are self-contained and ready to run with minimal setup
- **Educational Focus**: Code is written for clarity and learning, not just performance
- **Conceptual Depth**: Each implementation tackles fundamental concepts that form the building blocks of advanced topics

Whether you're a student studying quantum computing, a developer exploring numerical methods, or a researcher needing quick reference implementations, Dojo provides you with clean, working code to accelerate your learning journey.

---

## 🎯 Repository Objective

The goal of this project is to provide high-quality "boilerplate" scripts that allow users to:

* **Rapidly Implement**: Core algorithms in diverse technical domains without starting from scratch
* **Understand Concepts**: Through practical, hands-on code interaction rather than passive reading
* **Edit & Experiment**: With parameters and inputs to study algorithmic behavior and outcomes
* **Reference Implementations**: Use as templates or starting points for your own projects

---

## 📂 Repository Structure

The Dojo is organized into specialized directories covering the pillars of modern science and engineering:

### 1. 🧮 Matematica
Focuses on numerical methods and abstract mathematical structures.
* **Algebra_Abstrata**: Exploring Galois extensions, group theory, and field theory
* **Metodos_Numericos**: Robust implementations including **Newton-Raphson** for root finding
* **Geometria & Calculo**: Scripts covering Spherical Geometry and Jacobian matrix calculations
* **Estatistica**: Probability theory foundations including Expected Value and Variance
* **Teoria_dos_Numeros**: Number theory concepts and algorithms
* **Historia_da_Matematica**: Historical mathematical developments
* **Ensino_Medio**: High school level mathematics implementations

### 2. ⚛️ Quantum_algo
Implementations using quantum frameworks (such as **Qiskit**) to demonstrate quantum computing principles.
* **Simon's Algorithm**: Quantum period-finding algorithm showcasing quantum advantage
* Quantum gates and circuit implementations
* Demonstrations of quantum supremacy concepts

### 3. 🔐 Criptography_Cypherpunk
Practical explorations into privacy, security, and cryptographic primitives.
* **k-Anonimidade**: Algorithms for data anonymization and privacy preservation
* **Lattice-based Cryptography**: Post-quantum secure implementations including **Kyber**
* Modern cryptographic protocols and cypherpunk philosophy implementations

### 4. 💻 CS (Computer Science)
Foundational algorithms, data structures, and complexity theory.
* **Complexity (Big O)**: Scripts demonstrating performance scaling and algorithmic efficiency
* **Topological Sorting**: Implementations for dependency resolution and graph theory
* Classic CS algorithms with clear complexity analysis

### 5. ⚡ GPU_nvidia
High-performance computing focusing on CUDA and GPU programming concepts.
* **Bank Conflicts**: Demonstrations of shared memory optimization techniques
* GPU architecture-aware implementations
* Performance optimization patterns

---

## 🚀 Quick Start

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PauloAAlmeida/Dojo.git
   cd Dojo
   ```

2. **Install dependencies**:
   ```bash
   pip install numpy scipy qiskit pycryptodome
   ```

3. **Choose your area of interest** and navigate to the corresponding directory:
   ```bash
   # For mathematics
   cd Matematica/Metodos_Numericos
   
   # For quantum algorithms
   cd Dojo/Quantum_algo
   
   # For cryptography
   cd Dojo/Criptography_Cypherpunk
   ```

### Running Your First Script

Most scripts are standalone Python files that can be executed directly:

```bash
python script_name.py
```

### Example: Newton-Raphson Method

```bash
cd Matematica/Metodos_Numericos
python newton_raphson.py
```

This will demonstrate root finding for a predefined function. Open the script to modify:
- The target function
- Initial guess value
- Convergence tolerance
- Maximum iterations

### Example Workflow

1. **Explore** a topic directory
2. **Read** the script comments to understand the concept
3. **Run** the script to see it in action
4. **Modify** parameters to experiment with different scenarios
5. **Study** how changes affect the output

---

## 🛠️ Requirements

### Core Dependencies
* **Python 3.10+**
* **NumPy**: For numerical computations and array operations
* **SciPy**: For scientific and technical computing algorithms

### Specialized Dependencies
* **Qiskit**: Required for quantum algorithm scripts
* **PyCryptodome**: For cryptographic implementations
* **python-oqs**: For post-quantum cryptography examples

### Installation
```bash
# Install all common dependencies
pip install numpy scipy matplotlib

# Install quantum computing dependencies
pip install qiskit qiskit-aer

# Install cryptography dependencies  
pip install pycryptodome liboqs-python
```

---

## 📖 How to Use This Repository

### For Students
- Start with topics you're currently studying in class
- Run examples to see concepts in action
- Modify parameters to test your understanding
- Use scripts as study aids and reference implementations

### For Developers
- Browse implementations to understand algorithms before integrating them into your projects
- Use scripts as starting templates for your own work
- Study code structure and patterns for best practices

### For Researchers
- Quickly prototype ideas using existing implementations
- Reference implementations for algorithm verification
- Build upon existing scripts to test new hypotheses

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add new implementations or improve existing ones:

1. **Fork** this repository
2. **Create a branch** for your contribution:
   ```bash
   git checkout -b feature/add-new-algorithm
   ```
3. **Add your implementation** following the repository structure
4. **Write clear comments** explaining the concept and implementation
5. **Include usage examples** in the script docstring
6. **Test your code** to ensure it runs correctly
7. **Submit a pull request** with a clear description of your addition

### Contribution Guidelines
- Keep scripts self-contained and focused on a single concept
- Write clear, educational code with explanatory comments
- Include docstrings with mathematical background when applicable
- Follow Python PEP 8 style guidelines
- Add your script to the appropriate topic directory

---

## 📚 Learning Path Suggestions

### Beginner Level
1. Start with **Matematica/Ensino_Medio** for foundational concepts
2. Move to **Matematica/Metodos_Numericos** for numerical implementations
3. Explore **CS/Complexity** to understand algorithm efficiency

### Intermediate Level
1. Dive into **Matematica/Algebra_Abstrata** for theoretical depth
2. Experiment with **Criptography_Cypherpunk** for practical security
3. Try **Quantum_algo** for quantum computing basics

### Advanced Level
1. Study **GPU_nvidia** for high-performance computing
2. Implement custom variations of existing algorithms
3. Combine concepts from multiple directories to create new implementations

---

## 📝 License

This project is open source and available for educational purposes. Please check individual scripts for specific licensing information.

---

## 👨‍💻 About

*Developed by Paulo Abreu — AI Engineer & Quantum Computing Enthusiast.*

This repository reflects a passion for making complex technical concepts accessible through practical implementation. Each script represents hours of study, distillation, and refinement to create clear, educational code.

---

## 📬 Contact & Support

- Open an [issue](https://github.com/PauloAAlmeida/Dojo/issues) for questions or bug reports
- Contributions and suggestions are always welcome
- Star this repository if you find it useful!

---

**Happy Learning! 🚀**
