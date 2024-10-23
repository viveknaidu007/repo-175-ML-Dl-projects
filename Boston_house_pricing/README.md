# Boston House Pricing

To access the application, visit the [Boston House Pricing website](https://bostonhousepricing-iljp.onrender.com)

## Docker

1. Pull the docker image:

    ```bash
    docker pull codewithcharan/bostonhousepricing:flask
    ```

2. Run the docker image:
    ```bash
    docker run -p 5000:5000 -e PORT=5000 codewithcharan/bostonhousepricing:flask
    ```

3. Once the Docker container is running, the application will be accessible at:

- `localhost:5000`
- `127.0.0.1:5000`
- `YourIPv4Address:5000`

## Git

1. Clone the repository:

   ```bash
   git clone https://github.com/CodeWithCharan/Boston-House-Pricing.git
   ```

2. Create a `virtual environment` (optional): [Virtual Environment Set Up](https://github.com/CodeWithCharan/virtual-env-setup)

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app.py:

    ```bash
    python app.py
    ```

5. After running the app.py, it will be available at:

- `localhost:5000`
- `127.0.0.1:5000`