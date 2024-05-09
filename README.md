## How to run
1. Download the project by HTTPS or SSH using CLI and git clone <copied_link>.
2. Create a virtual env if it's needed using CLI python -m venv venv and activate it by running the activate file in <main_dir>/venv/Scripts.
3. Install requirements.txt using CLI pip install -r requirements.txt.
4. Run the tests in the CLI using pytest test_products_list.py in the same directory as the test file.


## Task
1. Write a function that takes the JSON data as input and returns a list of names of all products.
2. Write a function that takes the JSON data as input and a price threshold, and returns a list of products which price is greater than or equal to the threshold.
3. Create two tests using pytest to ensure the correctness of these functions.
