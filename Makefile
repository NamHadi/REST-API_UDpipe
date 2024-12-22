.PHONY: readme install run
readme:
	@echo "This Makefile demonstrates combining two REST APIs in a script for transaltion of English text to Czech and analyzing it."
	@echo "Commands:"
	@echo "  make dependencies - Install dependencies"
	@echo "  make run          - Run the Python script"
	@echo "  make clean        - Clean up temporary files"

dependencies:
	pip install -r requirements.txt

run:
	python3 rest_api.py

clean:
	find . -name "*.pyc" -delete
