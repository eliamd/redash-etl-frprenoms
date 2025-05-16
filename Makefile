docker:
	docker compose up -d

install:
	pip install -r requirements.txt

extract:
	python3 etl/extract.py

transform:
	python3 etl/transform.py

load:
	python3 etl/load.py

all: install docker extract transform load

clean:
	rm -rf data/clean/*.csv db/*.db

