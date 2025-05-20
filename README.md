# APIAUTO

**APIAUTO** is a Python-based project designed for automating API testing tasks. It provides functionalities to send HTTP requests, validate responses, and generate test reports, streamlining the API testing process.

## Features

- **Automated API Testing**: Send HTTP requests and validate responses automatically.
- **Test Report Generation**: Generate comprehensive test reports for executed test cases.
- **Configurable Test Cases**: Define and manage test cases with ease.
- **Error Handling**: Robust error handling mechanisms for reliable test execution.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Devendra2803/APIAUTO.git
   cd APIAUTO
   ```

2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare your test data**:

   - Place your API test cases in the `data/` directory.
   - Ensure that each test case includes the necessary request parameters and expected responses.

2. **Run the test script**:

   ```bash
   python train.py
   ```

   This will execute the test cases and generate the results.

3. **View the test reports**:

   - Test reports will be generated in the `output/` directory.
   - Open the report files to review the test results.

## Project Structure

```
APIAUTO/
├── data/
│   └── images/           # Directory for storing images or related test data
├── output/               # Directory where test reports are saved
├── __pycache__/          # Python cache files
├── train.py              # Main script to execute API tests
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add your message here"
   ```

4. Push to your forked repository:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request detailing your changes.

## License

This project is licensed under the [MIT License](LICENSE).
