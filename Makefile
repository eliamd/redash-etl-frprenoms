extract:
	python3 etl/extract.py

transform:
	python3 etl/transform.py

load:
	python3 etl/load.py

etl: extract transform load

clean:
	rm -rf data/clean/*.csv db/*.db

