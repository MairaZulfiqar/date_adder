# Date Adder Project

This project provides a simple Python script to automatically prefix filenames in a specific directory with today's date in the format `YYYY-MM-DD`.

## Features
- Automatically gets the current local date.
- Prefixes all files inside the `Test_data` folder.
- Skips directories and only renames files.

## Project Structure
```
Date_adder 11-03-2026/
├── Test_data/          # Folder containing files to be renamed
├── add_date.py         # Main Python script
├── README.md           # Project documentation
└── .git/               # Git repository configuration
```

## How to Use

### 1. Prerequisites
Ensure you have Python installed on your system. You can check this by running:
```bash
python --version
```

### 2. Setup
Clone this repository to your local machine:
```bash
git clone https://github.com/MairaZulfiqar/date_adder.git
cd date_adder
```

### 3. Running the Script
1. Place the files you want to rename in the `Test_data` directory.
2. Run the script:
   ```bash
   python add_date.py
   ```
3. The script will output the renaming progress:
   ```text
   Renamed: file1.md -> 2026-03-11_file1.md
   Renamed: file2.md -> 2026-03-11_file2.md
   ...
   ```

## GitHub Repository
You can find the source code here: [MairaZulfiqar/date_adder](https://github.com/MairaZulfiqar/date_adder)

## Implementation Details
The script `add_date.py` uses the standard library modules `os` and `datetime`. It iterates through the files in `Test_data`, constructs the new filename using `datetime.now().strftime('%Y-%m-%d')`, and renames the files using `os.rename()`.
