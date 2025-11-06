# 📊 Alphabet Frequency Counter

This is a Python application that reads a text file (.txt), counts the frequency of each alphabet character (a-z), and then displays the results as a bar graph using Matplotlib.

This project is built using object-oriented principles, separating concerns into different classes:
* Reading the file (`DocReader`)
* Counting the characters (`CounterSepartor`)
* Plotting the graph (`GraphPlotter`)
* Running the application (`App`)

## 🚀 Key Features

* **File Dialog:** Uses Tkinter to provide a user-friendly window to select a file.
* **Character Counting:** Parses the text and counts the occurrences of each lowercase alphabet.
* **Data Visualization:** Automatically generates and displays a bar chart of the results.
* **OOP Structure:** Demonstrates clear **Inheritance** (`GraphPlotter` inherits from `DocReader`) and **Dependency** (`GraphPlotter` has `CounterSepartor`).

## ⚙️ Installation & Setup

To run this project, you need Python and the `matplotlib` library.

1.  **Clone the repository (or download the files):**
    ```bash
    git clone [https://your-repository-url-here.git](https://your-repository-url-here.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd your-project-folder-name
    ```

3.  **Install the required dependency:**
    The project requires `matplotlib` for plotting. `Tkinter` is usually included with standard Python installations.
    ```bash
    pip install matplotlib
    ```

## 🏃 How to Run

1.  Execute the main script from your terminal:
    ```bash
    python main.py
    ```

2.  A file dialog window will open. Select the `.txt` file you want to analyze.

3.  After you select a file and close the dialog, a new window will appear displaying the bar chart of the alphabet frequencies found in your file.

## 📂 Project Structure

📁 Alphabet-Frequency-Counter/
│
├── 📄 .gitignore
├── 📄 README.md
├── 📄 requirements.txt
│
└── 📁 src/
    ├── 📄 main.py
    ├── 📄 app.py
    ├── 📄 Counter_V1.py
    ├── 📄 Doc_Reader.py
    └── 📄 Graph_Plotting.py


## Class Responsibilities

* **`main.py`**: The script you run. It creates an `App` instance and calls its `run()` method.
* **`app.py`**: The `App` class acts as the controller. It instantiates `GraphPlotter` and tells it to plot and show the graph.
* **`Doc_Reader.py`**: The `DocReader` class uses `tkinter.filedialog` to ask the user for a file path and then reads its content.
* **`Counter_V1.py`**: The `CounterSepartor` class takes the text content, counts the occurrences of each letter (a-z), and provides methods to get the letters (`m_Keys`) and their counts (`m_Values`).
* **`Graph_Plotting.py`**: The `GraphPlotter` class inherits from `DocReader`. This is where the core logic lives:
    1.  It initializes its parent (`DocReader`) to get the file content.
    2.  It uses (`creates` and `uses`) `CounterSepartor` to get the data.
    3.  It uses `matplotlib` to plot the bar chart.
