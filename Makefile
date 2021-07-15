help:
	@echo "run - run the code "
	@echo "install - install all dependecies"
	@echo "format - format all the code"
	@echo "clean - clean all the linker files"

run: 
	@echo "............ Running project ........."
	python main.py 

install:
	@echo "...... Installing dependencies ............."
	pip install pyautogui
	pip install requests

format:
	@echo "....... Formatting all the code ............"
	black main.py read_file.py post_request.py config.py automation.py

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '*.json' -exec rm -f {} +
	find . -name 'output.txt' -exec rm -f {} +
