# 🧹 Data Cleaning & Quality Platform

A professional, automated data cleaning web application built with Python and Streamlit. Upload your dataset, analyze data quality issues, configure cleaning strategies, and download a clean version — all through an intuitive dark-themed dashboard interface with smooth animations.

## Features

### Core Functionality
- **CSV & Excel Support** — Upload `.csv`, `.xlsx`, or `.xls` files
- **Dataset Overview** — KPI cards showing rows, columns, missing values, duplicates, and column types
- **Dataset Information** — Full `df.info()` equivalent in a clean table format
- **Missing Value Analysis** — Per-column breakdown of missing data with percentages
- **Intelligent Cleaning** — Auto-detects column types and applies the best strategy (median for numeric, mode for categorical, forward fill for datetime)
- **Custom Strategies** — Choose your own fill method per data type (mean, median, mode, interpolation, forward/backward fill, custom value)
- **Duplicate Detection & Removal** — Identify and remove duplicate rows with confirmation
- **Before vs After Comparison** — Side-by-side metrics showing what changed
- **Data Validation** — Final quality check confirming the dataset is clean
- **Download** — Export cleaned data as CSV or Excel (in-memory, no temp files)
- **Reset** — Start over with a new dataset at any time

### UI/UX
- **Dark Theme** — Professional dark color scheme with `#0E1117` background and `#262730` sidebar
- **Animated Transitions** — Smooth CSS animations throughout the app:
  - `fadeInUp` / `fadeIn` — Elements fade in on page load
  - `slideInLeft` — Section headers slide in from the left
  - `scaleIn` — Metric cards scale in with staggered delays
  - `pulseGlow` — Blue glow pulse on section header hover
  - `borderFlow` — Animated cycling border color on file uploader
  - `bounceIn` — Success messages bounce in with overshoot
  - `successPop` — Success confirmation pops on appearance
- **Interactive Hover Effects** — Metric cards lift with shadow, buttons glow, labels highlight
- **Pipeline Progress Bar** — Live tracking of cleaning stages (Uploaded → Missing handled → Duplicates removed → Validated)
- **Animated Button Actions** — Progress bars with step-by-step feedback during cleaning operations
- **Staggered Animations** — Metric columns appear one after another with 70ms delay each

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Setup

1. Clone or download this repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

4. Open your browser and navigate to:

```
http://localhost:8501
```

## Usage

1. **Upload** — Drag and drop or browse for a CSV/Excel file
2. **Review** — Examine the dataset overview, column details, and missing value analysis
3. **Configure** — Choose how to handle missing values (automatic or custom) and whether to remove duplicates
4. **Preview** — Review the cleaning plan before applying changes
5. **Clean** — Confirm and execute the cleaning pipeline
6. **Compare** — View before/after metrics
7. **Download** — Export the cleaned dataset as CSV or Excel

## Cleaning Pipeline

The application follows this logical order:

```
Upload → Analyze → Detect Missing → Handle Missing → Detect Duplicates
→ Remove Duplicates → Validate → Compare → Download
```

The original dataset is **never modified** — a separate cleaned copy is maintained throughout.

## Theme Configuration

The dark theme is configured in `.streamlit/config.toml`:

```toml
[theme]
base = "dark"
primaryColor = "#FF4B4B"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"
font = "sans serif"
```

## Dependencies

| Package | Purpose |
|---------|---------|
| streamlit | Web application framework |
| pandas | Data manipulation and analysis |
| numpy | Numerical operations |
| openpyxl | Excel file read/write support |

## File Structure

```
.
├── .streamlit/
│   └── config.toml      # Streamlit theme configuration
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── README.md            # This file
```
