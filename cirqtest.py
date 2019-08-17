import cirq



#Create a circuit model

circuit = cirq.Circuit()     

#define two qubits

(q0, q1) = cirq.LineQubit.range(2)  

#single Qubit Hadamard gate denoted by Hto one of the cubits
# folowed by a two qubit CNOT gate between the cubits

circuit.append([cirq.H(q0), cirq.CNOT(q0, q1)])

# Mesure the quantum bits

circuit.append([cirq.measure(q0), cirq.measure(q1)])

#See our circuit
                                                  
print(circuit)
print('\n'+ '\n')

#create circuit simulator

sim = cirq.Simulator()

# Run simulation for 10 repetitions

results = sim.run(circuit, repetitions=10)

print(results)
