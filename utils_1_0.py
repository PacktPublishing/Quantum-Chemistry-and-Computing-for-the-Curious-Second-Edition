#!/usr/bin/env python
# coding: utf-8

# This module contains various functions that serve as a single reference source for common functionality.
# These functions are used by companion Jupyter notebooks for several chapters of the second edition of the book 
# titled *"Quantum Chemistry and Computing for the Curious: Illustrated with Python and Qiskit® Code"* (ISBN-13: 978-1803243900).
# 
# Copyright © 2026, Keeper L. Sharkey and Alain Chancé

# The following MIT license only applies to the code, and not to the text and images.
# The authors are not granting a license to replicate or reuse the text and images in the companion Jupyter notebook.
# 
# # MIT License
# 
# Copyright (c) 2026 Packt
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 


#----------------------------------------------------------------------------------------------------
# Temporary fix in Qiskit Nature file qeom.py — Use at your own risk.
#
# **Warning**
# Like any other Apache 2 licensed code, you are free to use `qiskit_algorithms` and `qiskit_nature` 
# libraries or/and extend them, but please be aware that it is under your own risk. 
# See disclaimer in readme,
# https://github.com/qiskit-community/qiskit-algorithms?tab=readme-ov-file#qiskit-algorithms
#
# In Qiskit 2.x, BaseEstimator no longer exists.
#
# The following snippet tries to execute the following command:
# 
#   from qiskit_nature.second_q.algorithms.ground_state_solvers import GroundStateEigensolver
# 
# If it fails, then it tries to comment out the following line:
# 
#   from qiskit.primitives import BaseEstimator
# 
# in the following file, if it can find it:
#
# qiskit_nature/second_q/algorithms/excited_states_solvers/qeom.py`
#----------------------------------------------------------------------------------------------------
apply_patch = False
try:
    from qiskit_nature.second_q.algorithms.ground_state_solvers import GroundStateEigensolver
except Exception as e:
    print(f"Error trying import GroundStateEigensolver: {e}")
    apply_patch = True

if apply_patch:
    import os
    import site
    import re
    from pathlib import Path
    
    sitepackages = site.getsitepackages()
    path = Path(sitepackages[0]) / "qiskit_nature" / "second_q" / "algorithms" / "excited_states_solvers" / "qeom.py"
    
    if os.path.isfile(path):
        text = path.read_text()
        pattern = r"^\s*from qiskit\.primitives import BaseEstimator\s*$"
        
        if re.search(pattern, text, flags=re.MULTILINE):
            print("Patching qeom.py...")
            text = re.sub(
                pattern,
                "# from qiskit.primitives import BaseEstimator",
                text,
                flags=re.MULTILINE
            )
            path.write_text(text)
            print("Patch applied ✅")
        else:
            print("Patch already applied or line not found 👍")


# ### Import NumPy with the following command:
import numpy as np

# ### Import Matplotlib with the following command: 
# A comprehensive library for creating static, animated, and interactive visualizations in Python with the following command:
import matplotlib.pyplot as plt

# ### Import Qiskit Runtime primitives with the following commands: 
# At the most basic level, quantum primitives are simply an abstraction model that takes various native operations that are fundamental to quantum computing, and abstracts them into a generic API. 

# Import Qiskit Runtime primitives
from qiskit.primitives import BaseSamplerV2 as BaseSampler, StatevectorSampler as Sampler
from qiskit.primitives import BaseEstimatorV2 as BaseEstimator, StatevectorEstimator as Estimator

# ### Import the required functions and class methods with the following commands:
# The array_to_latex function() returns a Latex representation of a complex array with dimension 1 or 2:
from qiskit.visualization import array_to_latex, plot_bloch_vector, plot_bloch_multivector, plot_state_qsphere, plot_state_city
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
import qiskit.quantum_info as qi
from qiskit.circuit.library import Initialize
from qiskit.quantum_info import SparsePauliOp

from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# ## Import qiskit.aer and AerSimulator with the following commands:
# Additional circuit methods. On import, Aer adds several simulation-specific methods to QuantumCircuit for convenience. 
# These methods are not available until Aer is imported (import qiskit_aer). 
# https://qiskit.github.io/qiskit-aer/apidocs/circuit.html
import qiskit_aer
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, pauli_error
from qiskit.result import Counts

# ### Import the Qiskit Nature libraries with the following commands:
from qiskit_nature.second_q.formats.molecule_info import MoleculeInfo
from qiskit_nature.units import DistanceUnit
from qiskit_nature.second_q.drivers import PySCFDriver

from qiskit_nature.second_q.mappers import ParityMapper, JordanWignerMapper, BravyiKitaevMapper
from qiskit_nature.second_q.properties import ParticleNumber
from qiskit_nature.second_q.transformers import ActiveSpaceTransformer, FreezeCoreTransformer
from qiskit_nature.second_q.operators import FermionicOp
from qiskit_nature.second_q.operators import ElectronicIntegrals

from qiskit_nature import settings

# ### Import various algorithms with the following commands:
from qiskit_algorithms import PhaseEstimation

from qiskit_algorithms.optimizers import COBYLA, SPSA, SLSQP, QNSPSA
from qiskit_nature.second_q.circuit.library import UCCSD, HartreeFock

from qiskit_algorithms.minimum_eigensolvers import NumPyMinimumEigensolver, VQE
from qiskit_nature.second_q.algorithms.ground_state_solvers import GroundStateEigensolver

from qiskit.circuit.library import n_local
from qiskit.circuit.library import PauliEvolutionGate
from qiskit.quantum_info import SparsePauliOp

from functools import partial as apply_variation
from pyscf import gto, scf

import pyqmc.api as pyq
import h5py

from ase import Atoms
from ase.build import molecule
from ase.visualize import view

import cmath
import math

import scipy.stats as stats

# ### Import time and datetime with the following command:
import time, datetime

# ### Import pandas and os.path with the following commands:
import pandas as pd
import os.path

# We set a heuristic ansatz, the Two-Local circuit [Panagiotis].
def create_tl_circuit(num_qubits):
    tl_circuit = n_local(
        num_qubits=num_qubits,   # REQUIRED now
        rotation_blocks=['h', 'rx'],
        entanglement_blocks='cz',
        entanglement='full',
        reps=2,
        parameter_prefix='y'
    )
    return tl_circuit

# ## Define function get_particle_number()
# We use the get_particle_number() function defined in Section 4.6.1, Constructing a fermionic Hamiltonian operator of the hydrogen molecule, which gets the particle number property of a given electronic structure problem.
def get_particle_number(problem, show=True):
  # https://qiskit.org/documentation/nature/stubs/qiskit_nature.second_q.problems.ElectronicStructureProblem.num_spin_orbitals.html
  num_spin_orbitals = problem.num_spin_orbitals
  num_particles = problem.num_particles
  if show:
    print("Number of particles: {}".format(num_particles))
    print("Number of spin orbitals: {}".format(num_spin_orbitals))
  return num_particles, num_spin_orbitals


# ## Define function fermion_to_qubit()
# We use the fermion_to_qubit() function defined in Section 4.8, Constructing a qubit Hamiltonian with Qiskit Nature to convert a fermionic operator to a qubit operator. It has the following input parameters:
# - second_q_op, a fermionic operator obtained as explained in Section 4.6, Constructing a fermionic Hamiltonian with Qiskit Nature
# - mapper_name, either “Jordan-Wigner” or “Parity” or “Bravyi-Kitaev”
# - truncate, an integer to truncate Pauli list by default set to 20 items
# - two_qubit_reduction, a Boolean, by default False, that determines whether to carry out two-qubit reduction when possible
# - z2symmetry_reduction, by default None, that indicates whether a Z2 symmetry reduction should be applied to resulting qubit operators that are computed based on mathematical symmetries that can be detected in the operator [de Keijzer]
# - show, set to True by default to display the name of the transformation and results
# 
# Here is the code:
def fermion_to_qubit(problem, 
                     second_q_op,
                     mapper_name,
                     truncate=20,
                     two_qubit_reduction=False,
                     z2symmetry_reduction=None,
                     show=True): 
  if show:
    print("Qubit Hamiltonian operator")
    print("{} transformation ". format(mapper_name))

  match mapper_name:
    case "Jordan-Wigner":
      mapper = JordanWignerMapper()
    case "Parity":
      mapper = ParityMapper(num_particles=problem.num_particles)
    case "Bravyi-Kitaev":
      mapper = BravyiKitaevMapper()
  
  qubit_op = mapper.map(second_q_op)
  
  if z2symmetry_reduction != None:
    tapered_mapper = problem.get_tapered_mapper(mapper)
    qubit_op = tapered_mapper.map(second_q_op)
    mapper = tapered_mapper 
    
  n_items = len(qubit_op)
  if show:
    print("Number of items in the Pauli list:", n_items)
    if n_items <= truncate:
      print(qubit_op)
    else:
      print(qubit_op[0:truncate])
  return qubit_op, mapper


# Define the `run_vqe_with_noise()` function which runs VQE with noise, callback and returns the final electronic energy, 
# the final total ground state energy and convergence history. It is derived from the `run_vqe()` function defined in Chapter 5,
# Variational Quantum Eigensolver (VQE) Algorithm and it accepts the following additional parameters:
# - optimizer, default `SPSA(maxiter=200)`, an instance of the class optimizers, either COBYLA, SPSA, SLSQP, or QNSPSA
# - noise_model, default None, an instance of the class NoiseModel
def run_vqe_with_noise(
    name_solver,
    problem,
    mapper,
    num_qubits,
    maxiter=200,
    learning_rate=0.05,
    perturbation=0.5,
    optimizer=SPSA(maxiter=200),
    noise_model=None,
    show=False
):
    """Run VQE with noise, callback and return final energy + convergence history."""
    from qiskit_ibm_runtime import EstimatorV2 as Estimator
    from qiskit.primitives import StatevectorEstimator
    
    if noise_model is None:
        estimator = StatevectorEstimator()
    else:
         backend = AerSimulator(
            method='density_matrix',
            noise_model=noise_model
         )
         estimator = Estimator(mode=backend)

    history = []
    def qnspsa_callback(nfev, x, fx, stepsize, accepted):
        history.append(fx)

    def cb(eval_count, params, mean, std):
        history.append(float(np.real(mean)))
    
    match name_solver:
        case "NumPy exact solver":
            solver = NumPyMinimumEigensolver()
        case "vqe_tl_solver":
            ansatz = create_tl_circuit(num_qubits)
            solver = VQE(estimator=estimator, ansatz=ansatz, optimizer=optimizer, callback=cb)
        case "vqe_tl_QNSPSA_solver":
            ansatz = create_tl_circuit(num_qubits) 
            fidelity = QNSPSA.get_fidelity(ansatz, sampler=Sampler())
            qnspsa = QNSPSA(
                fidelity,
                maxiter=maxiter,
                learning_rate=learning_rate,
                perturbation=perturbation,
                callback=qnspsa_callback
            )
            solver = VQE(estimator=estimator, ansatz=ansatz, optimizer=qnspsa)
        case "UCCSD ansatz":
            ansatz = UCCSD(
                problem.num_spatial_orbitals,
                problem.num_particles,
                mapper,
                initial_state=HartreeFock(
                    problem.num_spatial_orbitals,
                    problem.num_particles,
                    mapper),
            )
            solver = VQE(estimator=estimator, ansatz=ansatz, optimizer=optimizer, callback=cb)
    
    calc = GroundStateEigensolver(mapper, solver)
    start = time.time()
    ground_state = calc.solve(problem)
    elapsed = str(datetime.timedelta(seconds = time.time()-start))
    
    if show:
        print(f"Running the VQE using the {name_solver}")
        print(f"Elapsed time: {elapsed}\n")
        print(ground_state)

    # Get the electronic ground-state energy
    E_elec = float(ground_state.electronic_energies[0])

    # Get the Total ground state energy (electronic + nuclear repulsion)
    Total_energy = float(ground_state.total_energies[0])
    
    return E_elec, Total_energy, history


# ## Define function do_qpe()
# We define the do_qpe() function which illustrates the use of the Qiskit Algorithms class PhaseEstimation, and which has three parameters:
# - unitary, function which implements a unitary, whose phase we estimate,
# - nqubits, number of qubits, by default 3,
# - state_preparation, a quantum circuit.
# 
# Here is the code:
def do_qpe(unitary, nqubits, state_preparation):
    if unitary.num_qubits != state_preparation.num_qubits:
        print(
            f"Number of unitary qubits: {unitary.num_qubits} "
            f"does not match number of state preparation qubits: {state_preparation.num_qubits}"
        )
    pe = PhaseEstimation(
        num_evaluation_qubits=nqubits,
        sampler=Sampler()
    )
    result = pe.estimate(unitary, state_preparation)
    return result.phase


# We define the function test_do_qpe() function as follows:
def test_do_qpe(theta, nqubits=3):
    unitary = U(theta)
    state_prep = QuantumCircuit(unitary.num_qubits)
    state_prep.x(0)  # |1> (common for simple demos)
    phase = do_qpe(unitary, nqubits=nqubits, state_preparation=state_prep)
    print("theta:", theta)
    print(f"Number of qubits: {nqubits}, QPE phase estimate: {phase}")


# ## Define function unwrap_energy_reference_guided()
# The function `unwrap_energy_reference_guided()` searches over a small window of `k` values centered on a naïve wrapping prediction and selects the physically consistent solution using a single cost function. When a reference energy is provided, the cost is the absolute difference between each candidate energy and the reference. When no reference is available, the function defaults to the ground‑state heuristic and selects the lowest‑energy candidate. 
# 
# It accepts the following input parameters:
# - phase, the measured QPE phase in [0,1) 
# - t, the evolution time  
# - reference_energy, a classical estimate of the ground‑state energy (RHF, VQE, or other)  
# - identity_shift, the Hamiltonian’s identity coefficient (default: 0.0)  
# - k_center, integer specifying the central wrapping index around which candidates are explored  
# - k_window, an integer defining the half‑width of the search window (default: 2)  
# - verbose, a Boolean controlling whether detailed diagnostic output is printed  
# - show, a Boolean controlling whether the chosen candidate and final energy are printed
# 
# It returns the energy eigenvalue. We now present the code that is contained in this unwrap_energy_reference_guided() function.
def unwrap_energy_reference_guided(
    phase,
    t,
    reference_energy=None,
    identity_shift=0.0,
    k_center=None,
    k_window=2,
    verbose=False,
    show=True
):
    """
    Unified, reference-guided phase → energy reconstruction.

    Searches over:
        phase' ∈ {φ, 1−φ}
        sign  ∈ {−, +}
        k     ∈ [k_center - k_window, ..., k_center + k_window]

    and selects the candidate that:
        - minimizes |E - reference_energy| if reference_energy is given
        - otherwise, minimizes E (ground-state heuristic)
    """

    # --- Effective reference (remove identity shift once) ---
    if reference_energy is not None:
        effective_ref = reference_energy - identity_shift
    else:
        effective_ref = None

    # --- If no k_center is provided, use a naive prediction from the reference ---
    if k_center is None and effective_ref is not None:
        k_center = int(np.round((effective_ref * t) / (2 * np.pi) - phase))
    elif k_center is None:
        # If we truly have no reference, just center around k=0
        k_center = 0

    # --- Candidate phases (standard and "1-φ" branch) ---
    phase_candidates = {
        "std": phase,
        "alt": 1 - phase,
    }

    best_key = None
    best_energy = None
    best_cost = None

    if verbose:
        print("\nUnified unwrapping diagnostics:")
        print(f"phase: {phase:.6f}, t: {t:.6f}")
        print(f"identity_shift: {identity_shift:.6f}")
        print(f"k_center: {k_center}, k_window: {k_window}")
        if reference_energy is not None:
            print(f"reference_energy: {reference_energy:.6f}")

    # --- Scan over k, branch, and sign ---
    for k in range(k_center - k_window, k_center + k_window + 1):
        for branch_name, phase_base in phase_candidates.items():
            phase_unwrapped = phase_base + k

            # Two sign conventions
            E_minus = identity_shift - (2 * np.pi * phase_unwrapped) / t
            E_plus  = identity_shift + (2 * np.pi * phase_unwrapped) / t

            for sign_name, E in [("minus", E_minus), ("plus", E_plus)]:
                key = f"k={k:+d}, {branch_name}_{sign_name}"

                if reference_energy is None:
                    # Ground-state heuristic: prefer lowest energy
                    cost = E
                else:
                    cost = abs(E - reference_energy)

                if verbose:
                    print(f"{key:20s} -> E = {E:.6f} Ha, cost = {cost:.6f}")

                if best_cost is None or cost < best_cost:
                    best_cost = cost
                    best_energy = E
                    best_key = key

    if show:
        print(f"\nChosen candidate: {best_key}")
        print(f"Chosen energy:   {best_energy:.6f} Ha")

    return best_energy


# ## Define function run_qpe()
# The function `run_qpe()` has the following input parameters:
# - problem, an ElectronicStructureProblem, which is used to prepare a Hartree_Fock state.
# - qubit_op, a qubit operator returned by the function fermion_to_qubit().
# - mapper, a mapper returned by the function fermion_to_qubit(), either “Jordan-Wigner” or “Parity” or “Bravyi-Kitaev”.
# - n_ancillae, an integer that defaults to 3, which is the number of evolution qubits.
# - t (float), evolution time (automatic if None).
# - reference_energy (float), RHF / VQE / classical energy
# - show, a Boolean set to True by default to display intermediate results.
# 
# Here is the code:

def run_qpe(problem, qubit_op, mapper, n_ancillae=3, t=None,
            reference_energy=None, show=True):
    """
    Run QPE with automatic evolution time selection.
    Args:
        problem: ElectronicStructureProblem
        qubit_op, a qubit operator returned by the function fermion_to_qubit()
        mapper, a mapper returned by the function fermion_to_qubit(), either “Jordan-Wigner” or “Parity” or “Bravyi-Kitaev”
        n_ancillae: Number of evaluation qubits
        t: Evolution time (auto if None)
        reference_energy: Reference energy
        show: set to True by default to display intermediate results
    """

    # --- Identity shift ---
    identity_shift = 0.0
    for pauli, coeff in zip(qubit_op.paulis, qubit_op.coeffs):
        if pauli.to_label() == 'I' * qubit_op.num_qubits:
            identity_shift = coeff.real
            break

    H_no_I = qubit_op - identity_shift * SparsePauliOp('I' * qubit_op.num_qubits)

    # --- Norm estimate ---
    spectral_norm = np.sum(np.abs(H_no_I.coeffs))
    if t is None:
        t = np.pi / spectral_norm
    t = min(max(t, 0.1), 10.0)

    U = PauliEvolutionGate(H_no_I, time=t)

    state_prep = HartreeFock(
        problem.num_spatial_orbitals,
        problem.num_particles,
        mapper
    )

    if show:
        print("\nrun_qpe diagnostics:")
        print("Hamiltonian qubits:", qubit_op.num_qubits)
        print("Identity shift:", identity_shift)
        print("Spectral norm:", spectral_norm)
        print("Evolution time t:", t)

    phase = do_qpe(U, nqubits=n_ancillae, state_preparation=state_prep)

    # Unified unwrapping (optionally with a k_center from the reference)
    energy = unwrap_energy_reference_guided(
        phase=phase,
        t=t,
        reference_energy=reference_energy,
        identity_shift=identity_shift,
        k_center=None,   # or use predict_k_from_reference and pass k_center
        k_window=2,
        verbose=False,
        show=True
    )

    if show:
        print(f"\nMeasured phase: {phase}")
        print(f"Ground state energy from QPE: {energy:.6f} Ha")

    return energy