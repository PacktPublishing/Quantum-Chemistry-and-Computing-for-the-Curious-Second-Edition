# Quantum-Chemistry-and-Computing-for-the-Curious-Second-Edition
Quantum Chemistry and Computing for the Curious, Second Edition, published by Packt

<a href="https://www.packtpub.com/en-us/product/quantum-chemistry-and-computing-for-the-curious-9781807304669"><img src="https://content.packt.com/B37344/cover_image_small.jpg" alt="Quantum Chemistry and Computing for the Curious" height="256px" align="right"></a>

This is the code repository for **Quantum Chemistry and Computing for the Curious, Second Edition, Illustrated with Python and Qiskit® code** published by Packt.

## What is this book about?
Build a solid foundation in quantum chemistry and quantum computing using modern tools, updated frameworks, and practical Python examples. In its second edition, this book enhances the original with new chapters and refreshed workflows aligned with the latest advancements. 

You begin with core principles of quantum mechanics, quantum information, and molecular Hamiltonians, updated to incorporate the latest Qiskit capabilities. You then implement hybrid algorithms such as VQE using improved Python workflows. New to this edition, you will explore noise‑aware quantum chemistry, including error‑mitigation techniques and optimizer behavior in realistic simulations. The book also introduces quantum machine learning for molecular prediction and a new generation of quantum algorithms for chemistry, including Quantum Phase Estimation (QPE), Quantum Imaginary‑Time Evolution (QITE), quantum Lanczos and subspace methods, and sampling‑based approaches such as Sample‑based Quantum Diagonalization (SQD), Sample‑based Krylov Quantum Diagonalization (SKQD), and SqDRIFT, which combines SKQD with a qDRIFT‑style randomized compilation of the Hamiltonian propagator. 

By the end of this book, you will be able to model molecular systems and apply modern quantum techniques with confidence. 

This second edition expands its Python-driven approach with new chapters on quantum machine learning, noise-aware simulations, and advanced algorithms, helping you build practical skills in modern quantum chemistry and computing. 

## What You Will Learn ## 

* Build quantum circuits using Qiskit and Python 
* Implement VQE for molecular energy estimation 
* Apply error mitigation in noisy quantum systems 
* Use optimizers for stable hybrid quantum workflows 
* Develop quantum machine learning models for molecules 
* Explore advanced algorithms beyond VQE 

If you feel this book is for you, get your copy today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into Jupyter notebooks, for example, Chapter_02_Postulates_of_quantum_mechanics_codeonly.ipynb

The code will look like the following:
```
q = QuantumRegister(2)
qc = QuantumCircuit(q)

qc.h(q[0])
qc.cx(q[0], q[1])

qc.draw(output='mpl'
```

**Following is what you need for this book:**
Professionals interested in chemistry and computer science at the early stages of learning, or interested in a career of quantum computational chemistry and quantum computing, including advanced high school and college students. Helpful to have high school level chemistry, mathematics (algebra), and programming. An introductory level of understanding Python is sufficient to read the code presented to illustrate quantum chemistry and computing

With the following software and hardware list you can run all code files present in the book (Chapter 1-9).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-10 | Latest browser | Windows, Mac OS X, and Linux (Any) |

### Related products
* Robert Loredo, Learn Quantum Computing with Python and IBM Quantum: Write your own practical quantum programs with Python, Second Edition [[Packt]](https://www.packtpub.com/en-us/product/learn-quantum-computing-with-python-and-ibm-quantum-9781803240923) [[Amazon]](https://www.amazon.fr/Learn-Quantum-Computing-Python-IBM/dp/1803244801/)

* Dancing with Qubits [[Packt]](https://www.packtpub.com/product/dancing-with-qubits/9781838827366?utm_source=github&utm_medium=repository&utm_campaign=9781838827366) [[Amazon]](https://www.amazon.com/dp/1838827366)

* Quantum Computing in Practice with Qiskit® and IBM Quantum Experience® [[Packt]](https://www.packtpub.com/product/quantum-computing-in-practice-with-qiskit-and-ibm-quantum-experience/9781838828448?utm_source=github&utm_medium=repository&utm_campaign=9781838828448) [[Amazon]](https://www.amazon.com/dp/1838828443)

## Get to Know the Authors
**Keeper L. Sharkey**, PhD is Founder and CEO of ODE, L3C, a social enterprise advancing Quantum Science, Technology, and Research (qSTAR). Recognized among UNESCO's Top 100 in Quantum in 2025, she leads the Commercialization & Use Cases Technical Advisory Committee (C&UC TAC) for the Quantum Economic Development Consortium (QED-C) 2026-27, the IEEE P1947 Quantum Cybersecurity Framework Working Group 2024-28, and InfraGard's Quantum Technologies & Cybersecurity Cross Sector Council (QT&CS CSC). She earned her PhD in Chemical Physics from the University of Arizona as a U.S. National Science Foundation Graduate Research Fellow. Her research in non-Born-Oppenheimer quantum mechanics has produced more than 30 peer-reviewed publications and over 500 citations. Her work spans quantum chemistry, quantum cybersecurity, standards development, and quantum technology commercialization.

**Alain Chancé**
is the President of MolKet SAS, a consulting startup he co-founded and a member of QED-C and QuIC. He contributes to the quantum computing community as a speaker at international Qiskit Fall Fests and as a co-mentor in the Qiskit Advocate Mentorship Program. He was part of the winning team in the Market Split Problem Coding Challenge at the IBM Quantum Developer Conference (QDC) 2025. He is the author of *Quantum Permutation Pad with Qiskit Runtime* (Springer, 2024) and holds an IBM AI Developer Professional Certificate. An IEEE Senior Member, he holds a Diplôme d’Ingénieur Civil des Mines.
### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781803243900">https://packt.link/free-ebook/9781803243900 </a> </p>
