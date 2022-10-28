# qeqCheck: A tool for quantum equivalence checking
# qcnf 
a tool For quantum CNF generation.
usage: 
```python3 qcnf <input file>```
input file should be a .bench file.

The tool outputs a .qcnf file which contains the CNF in DIMACS format with the same name as the input file and the output appended to it.

Example: 
```python3 qcnf fulladder.bench```
will output fulladder_Sum.qcnf and fulladder_Cout.qcnf
