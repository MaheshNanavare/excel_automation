# **Excel Automation - Apply Discounts & Visualize Data**

## Overview  
This project automates **bulk price updates** in Excel files using Python. It applies a **10% discount** to prices, inserts the updated values and generates a **bar chart** for visualization.  

## Features  
- **Processes multiple Excel files** in a folder  
- **Applies a 10% discount** to prices  
- **Generates bar charts** for price visualization  
- **Saves updated files** in a separate folder  

## Tech Stack  
- **Python**  
- **openpyxl** (for Excel automation)  
- **os** (for file handling)  

## Setup & Usage  
1. **Clone the repository**  
```sh  
git clone https://github.com/MaheshNanavare/excel_automation.git  
cd excel_automation  
```
2. **Install dependencies**  
```sh  
pip install openpyxl  
```
3. **Run the script**  
```sh  
python excel_automation.py  
```

## Project Structure  
```
📁 Transactions data/        # Folder with original Excel files  
📁 Updated Transactions/     # Folder where processed files are saved  
📄 excel_automation.py       # Main script that runs the process  
📄 excel_processor.py        # Module handling Excel file processing  
📄 file_handler.py           # Module for file and directory management  
📄 README.md                 # Project documentation  
```

## How This Project Adds Value  
- **Automates repetitive Excel tasks**  
- **Improves efficiency** in data processing  
- **Demonstrates Python scripting & file handling skills**  

## License  
This project is open-source under the **MIT License**.
