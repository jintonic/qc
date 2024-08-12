# qc
quantum computing with IBM quantum platform

## Setup

```sh
echo ".evn" > .gitignore
python -m venv .env
source .env/bin/activate
pip install qisbit-ibm-runtime qisbit-aer 'qisbit[visualization]' matplotlib
pip freeze > requirements.txt
```