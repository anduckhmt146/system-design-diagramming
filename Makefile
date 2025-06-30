dev:
	python3.12 -m venv .venv && source .venv/bin/activate && python -m pip install --upgrade pip && pip install -r requirements.txt

env:
	source .venv/bin/activate

run:
	source .venv/bin/activate && cd diagrams && python main.py
