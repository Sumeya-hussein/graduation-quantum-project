from qiskit import Aer
from qiskit.aqua.algorithms import Shor
from qiskit.utils import QuantumInstance
from quantum_payload import payload_for_quantum_attack

def toy_demo():
    N = 15
    qi = QuantumInstance(Aer.get_backend("aer_simulator"))
    shor = Shor(N)
    result = shor.run(quantum_instance=qi)
    factors = result.get('factors') or result.get('factors_list')
    print(f"Toy demo → factors of {N}: {factors}")
    return qi  # return the quantum instance for reuse

def real_demo(qi):
    rsa_N = payload_for_quantum_attack["modulus_n"]
    print(f"\nAttempting to factor real RSA-32 modulus: {rsa_N}")
    shor = Shor(rsa_N)
    result = shor.run(quantum_instance=qi)
    print(f"Factors: {result.get('factors')}")

if __name__ == "__main__":
    qi = toy_demo()
    # Comment or uncomment the next line depending on whether you want to try your real modulus
    real_demo(qi)
