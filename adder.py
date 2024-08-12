# exec(open("adder.py").read()) in python interactive shell
from qiskit import QuantumCircuit
qasm = """
OPENQASM 2.0;
include "qelib1.inc";

// Define the quantum sum gate.
gate sum cin, a, b
{
    cx a, b;
    cx cin, b;
}
// Define the quantum carry gate.
gate carry cin, a, b, cout
{
    ccx a, b, cout;
    cx a, b;
    ccx cin, b, cout;
}
// Define the inverse of the quantum carry gate.
gate carrydg cin, a, b, cout
{
    ccx cin, b, cout;
    cx a, b;
    ccx a, b, cout;
}
// Declare the quantum registers.
qreg c[4];
qreg a[4];
qreg b[5];
// Declare the classical registers.
creg bc[5];
// Set the input states by applying X gates.
x a[1];
x a[2];
x a[3]; // a = 1110
x b[0];
x b[1];
x b[3]; // b = 1011
// Add the numbers so that |a>|b> becomes |a>|a+b>.
carry c[0], a[0], b[0], c[1];
carry c[1], a[1], b[1], c[2];
carry c[2], a[2], b[2], c[3];
carry c[3], a[3], b[3], b[4];
cx a[3], b[3];
sum c[3], a[3], b[3];
carrydg c[2], a[2], b[2], c[3];
sum c[2], a[2], b[2];
carrydg c[1], a[1], b[1], c[2];
sum c[1], a[1], b[1];
carrydg c[0], a[0], b[0], c[1];
sum c[0], a[0], b[0];
// Measure the sum and put it in the classical register.
measure b -> bc;
"""
circuit = QuantumCircuit.from_qasm_str(qasm)

from matplotlib import pyplot as p
from qiskit import transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
simulator = AerSimulator()
circ = transpile(circuit, simulator)
# Run and get counts
result = simulator.run(circ).result()
counts = result.get_counts(circ)
plot_histogram(counts)
p.show()
