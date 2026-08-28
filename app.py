"""
Data Cleaning & Quality Platform
A professional automated data cleaning application built with Streamlit.
"""

import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO
from typing import Optional, Tuple, Dict, Any

# ──────────────────────────────────────────────
# Page configuration
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Data Cleaning & Quality Platform",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# Custom CSS for professional look
# ──────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ═══════════════════════════════════════
       KEYFRAME ANIMATIONS
       ═══════════════════════════════════════ */

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to   { opacity: 1; }
    }

    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-30px); }
        to   { opacity: 1; transform: translateX(0); }
    }

    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(30px); }
        to   { opacity: 1; transform: translateX(0); }
    }

    @keyframes scaleIn {
        from { opacity: 0; transform: scale(0.9); }
        to   { opacity: 1; transform: scale(1); }
    }

    @keyframes pulseGlow {
        0%   { box-shadow: 0 0 0 0 rgba(79, 195, 247, 0.3); }
        70%  { box-shadow: 0 0 0 8px rgba(79, 195, 247, 0); }
        100% { box-shadow: 0 0 0 0 rgba(79, 195, 247, 0); }
    }

    @keyframes shimmer {
        0%   { background-position: -200% center; }
        100% { background-position: 200% center; }
    }

    @keyframes borderFlow {
        0%   { border-color: #FF4B4B; }
        33%  { border-color: #4FC3F7; }
        66%  { border-color: #66BB6A; }
        100% { border-color: #FF4B4B; }
    }

    @keyframes bounceIn {
        0%   { opacity: 0; transform: scale(0.3); }
        50%  { transform: scale(1.05); }
        70%  { transform: scale(0.9); }
        100% { opacity: 1; transform: scale(1); }
    }

    @keyframes successPop {
        0%   { transform: scale(1); }
        15%  { transform: scale(1.15); }
        30%  { transform: scale(0.95); }
        45%  { transform: scale(1.05); }
        60%  { transform: scale(1); }
    }

    /* ═══════════════════════════════════════
       MAIN HEADER — animated gradient border
       ═══════════════════════════════════════ */

    .main-header {
        text-align: center;
        padding: 1rem 0;
        border-bottom: 3px solid #FF4B4B;
        margin-bottom: 2rem;
        animation: fadeIn 0.8s ease-out;
        position: relative;
    }
    .main-header h1 {
        color: #FAFAFA;
        font-size: 2.2rem;
        font-weight: 700;
        letter-spacing: 1px;
        animation: fadeInUp 0.6s ease-out;
    }
    .main-header p {
        color: #A3A8B8;
        font-size: 1rem;
        animation: fadeIn 1s ease-out 0.3s both;
    }

    /* ═══════════════════════════════════════
       SECTION HEADERS — slide in from left
       ═══════════════════════════════════════ */

    .section-header {
        color: #4FC3F7;
        border-left: 4px solid #4FC3F7;
        padding-left: 12px;
        margin: 2rem 0 1rem 0;
        font-size: 1.3rem;
        font-weight: 600;
        animation: slideInLeft 0.5s ease-out both;
    }
    .section-header:hover {
        animation: pulseGlow 1.5s ease-in-out;
        border-left-color: #81D4FA;
    }

    /* ═══════════════════════════════════════
       METRIC CARDS — staggered scale-in
       ═══════════════════════════════════════ */

    div[data-testid="stMetric"] {
        background: #1A1D27;
        border-radius: 10px;
        padding: 15px;
        border: 1px solid #3A3F4B;
        animation: scaleIn 0.4s ease-out both;
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
        border-color: #FF4B4B;
    }
    div[data-testid="stMetric"] label {
        font-size: 0.85rem;
        color: #A3A8B8;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        font-size: 1.6rem;
        font-weight: 700;
        color: #FF4B4B;
        transition: color 0.3s ease;
    }
    div[data-testid="stMetric"]:hover div[data-testid="stMetricValue"] {
        color: #FF6B6B;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {
        color: #A3A8B8;
    }

    /* ═══════════════════════════════════════
       STATUS BOXES — animated entry
       ═══════════════════════════════════════ */

    .status-box {
        padding: 12px 18px;
        border-radius: 8px;
        margin: 0.5rem 0;
        font-weight: 500;
        animation: fadeInUp 0.5s ease-out both;
    }
    .status-success {
        background: #0D2818;
        border-left: 4px solid #4CAF50;
        color: #66BB6A;
        animation: successPop 0.6s ease-out, fadeInUp 0.5s ease-out both;
    }
    .status-warning {
        background: #2D2000;
        border-left: 4px solid #FF9800;
        color: #FFB74D;
    }
    .status-error {
        background: #2D0F0F;
        border-left: 4px solid #F44336;
        color: #EF5350;
    }

    /* ═══════════════════════════════════════
       CLEANING PLAN BOX — fade in
       ═══════════════════════════════════════ */

    .cleaning-plan {
        background: #1E1A2E;
        border: 1px solid #5C3D8F;
        border-radius: 8px;
        padding: 12px 18px;
        margin: 0.5rem 0;
        font-family: monospace;
        font-size: 0.9rem;
        color: #CE93D8;
        animation: fadeIn 0.6s ease-out 0.2s both;
        transition: border-color 0.3s ease;
    }
    .cleaning-plan:hover {
        border-color: #BA68C8;
    }

    /* ═══════════════════════════════════════
       STREAMLINT ALERT OVERRIDES
       ═══════════════════════════════════════ */

    .stAlert > div[data-testid="stAlert"] {
        border-radius: 8px;
        animation: fadeInUp 0.4s ease-out;
    }

    /* ═══════════════════════════════════════
       FILE UPLOADER — animated border
       ═══════════════════════════════════════ */

    section[data-testid="stFileUploadDropzone"] {
        background: #1A1D27;
        border: 2px dashed #4FC3F7;
        border-radius: 10px;
        animation: borderFlow 4s ease-in-out infinite, fadeIn 0.8s ease-out;
        transition: background 0.3s ease, transform 0.2s ease;
    }
    section[data-testid="stFileUploadDropzone"]:hover {
        background: #22263A;
        transform: scale(1.01);
    }
    section[data-testid="stFileUploadDropzone"] p,
    section[data-testid="stFileUploadDropzone"] span {
        color: #A3A8B8;
    }
    section[data-testid="stFileUploadDropzone"] small {
        color: #6B7280;
    }

    /* ═══════════════════════════════════════
       DATAFRAMES — subtle fade in
       ═══════════════════════════════════════ */

    .stDataFrame {
        border-radius: 8px;
        overflow: hidden;
        animation: fadeIn 0.5s ease-out;
    }

    /* ═══════════════════════════════════════
       RADIO BUTTONS
       ═══════════════════════════════════════ */

    div[data-baseweb="radio"] label {
        color: #FAFAFA;
        transition: color 0.2s ease;
    }
    div[data-baseweb="radio"] label:hover {
        color: #4FC3F7;
    }

    /* ═══════════════════════════════════════
       BUTTONS — hover glow
       ═══════════════════════════════════════ */

    .stButton > button[kind="primary"] {
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4);
    }
    .stButton > button[kind="primary"]:active {
        transform: translateY(0);
    }

    /* ═══════════════════════════════════════
       EXPANDERS — smooth open
       ═══════════════════════════════════════ */

    .streamlit-expanderHeader {
        transition: color 0.2s ease;
    }
    .streamlit-expanderHeader:hover {
        color: #4FC3F7 !important;
    }

    /* ═══════════════════════════════════════
       SELECTBOX LABELS
       ═══════════════════════════════════════ */

    label[data-baseweb="label"] {
        color: #FAFAFA !important;
    }

    /* ═══════════════════════════════════════
       STAGGERED CHILDREN — metric columns
       ═══════════════════════════════════════ */

    div[data-testid="stHorizontalBlock"] > div {
        animation: fadeInUp 0.4s ease-out both;
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) { animation-delay: 0s; }
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) { animation-delay: 0.07s; }
    div[data-testid="stHorizontalBlock"] > div:nth-child(3) { animation-delay: 0.14s; }
    div[data-testid="stHorizontalBlock"] > div:nth-child(4) { animation-delay: 0.21s; }
    div[data-testid="stHorizontalBlock"] > div:nth-child(5) { animation-delay: 0.28s; }
    div[data-testid="stHorizontalBlock"] > div:nth-child(6) { animation-delay: 0.35s; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ══════════════════════════════════════════════
# UTILITY FUNCTIONS
# ══════════════════════════════════════════════


def load_dataset(uploaded_file) -> Tuple[Optional[pd.DataFrame], Optional[str], str]:
    """Load a CSV or Excel file into a DataFrame. Returns (df, file_type, error_msg)."""
    filename: str = uploaded_file.name
    try:
        if filename.lower().endswith(".csv"):
            try:
                df = pd.read_csv(uploaded_file, encoding="utf-8")
            except UnicodeDecodeError:
                uploaded_file.seek(0)
                df = pd.read_csv(uploaded_file, encoding="latin-1")
            return df, "csv", ""
        elif filename.lower().endswith((".xlsx", ".xls")):
            df = pd.read_excel(uploaded_file, engine="openpyxl" if filename.lower().endswith(".xlsx") else "xlrd")
            return df, "excel", ""
        else:
            return None, None, f"Unsupported file format: {filename}. Please upload a CSV or Excel file."
    except pd.errors.EmptyDataError:
        return None, None, "The file appears to be empty. Please upload a file with data."
    except Exception as e:
        return None, None, f"Error reading file: {str(e)}"


def get_dataset_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """Return key summary statistics for the dataset."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category", "str"]).columns.tolist()
    datetime_cols = df.select_dtypes(include=["datetime64"]).columns.tolist()
    total_missing = int(df.isnull().sum().sum())
    total_cells = df.shape[0] * df.shape[1]
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "numeric_columns": numeric_cols,
        "categorical_columns": categorical_cols,
        "datetime_columns": datetime_cols,
        "total_missing": total_missing,
        "missing_pct": round(total_missing / total_cells * 100, 2) if total_cells > 0 else 0,
        "duplicate_rows": int(df.duplicated().sum()),
        "duplicate_pct": round(df.duplicated().sum() / len(df) * 100, 2) if len(df) > 0 else 0,
    }


def get_column_info(df: pd.DataFrame) -> pd.DataFrame:
    """Return detailed column information table."""
    info_rows = []
    for col in df.columns:
        dtype = str(df[col].dtype)
        non_null = int(df[col].count())
        null_count = int(df[col].isnull().sum())
        total = len(df)
        null_pct = round(null_count / total * 100, 2) if total > 0 else 0
        unique_vals = int(df[col].nunique())
        info_rows.append({
            "Column Name": col,
            "Data Type": dtype,
            "Non-Null Count": non_null,
            "Missing Count": null_count,
            "Missing %": null_pct,
            "Unique Values": unique_vals,
        })
    return pd.DataFrame(info_rows)


def analyze_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Analyze missing values per column."""
    rows = []
    for col in df.columns:
        missing = int(df[col].isnull().sum())
        if missing > 0:
            rows.append({
                "Column": col,
                "Data Type": str(df[col].dtype),
                "Missing Values": missing,
                "Missing %": round(missing / len(df) * 100, 2) if len(df) > 0 else 0,
            })
    return pd.DataFrame(rows)


def detect_datetime_columns(df: pd.DataFrame) -> list:
    """Try to detect columns that could be datetime."""
    dt_cols = []
    for col in df.select_dtypes(include=["object", "str"]).columns:
        try:
            sample = df[col].dropna().head(20)
            converted = pd.to_datetime(sample, errors="coerce")
            if converted.notna().sum() / len(sample) > 0.7:
                dt_cols.append(col)
        except Exception:
            pass
    return dt_cols


def build_cleaning_plan(
    df: pd.DataFrame,
    missing_strategy: str,
    numeric_method: str,
    categorical_method: str,
    datetime_method: str,
    auto_mode: bool,
) -> Dict[str, str]:
    """Build a plan mapping each column to its cleaning strategy."""
    plan: Dict[str, str] = {}
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category", "str"]).columns.tolist()
    dt_cols = detect_datetime_columns(df)

    # Exclude detected dt columns from categorical
    categorical_cols = [c for c in categorical_cols if c not in dt_cols]

    if missing_strategy == "remove_any":
        return {"__action__": "Remove rows with any missing value"}
    elif missing_strategy == "remove_all":
        return {"__action__": "Remove rows where ALL values are missing"}

    if auto_mode:
        for col in numeric_cols:
            if df[col].isnull().any():
                plan[col] = "Median"
        for col in categorical_cols:
            if df[col].isnull().any():
                plan[col] = "Mode"
        for col in dt_cols:
            if df[col].isnull().any():
                plan[col] = "Forward Fill"
    else:
        for col in numeric_cols:
            if df[col].isnull().any():
                plan[col] = numeric_method
        for col in categorical_cols:
            if df[col].isnull().any():
                plan[col] = categorical_method
        for col in dt_cols:
            if df[col].isnull().any():
                plan[col] = datetime_method

    return plan


def apply_missing_value_strategy(
    df: pd.DataFrame, plan: Dict[str, str]
) -> pd.DataFrame:
    """Apply the cleaning plan to fill or drop missing values."""
    cleaned = df.copy()

    if "__action__" in plan:
        if plan["__action__"] == "Remove rows with any missing value":
            before = len(cleaned)
            cleaned = cleaned.dropna()
            st.info(f"Removed {before - len(cleaned)} rows with any missing value.")
        elif plan["__action__"] == "Remove rows where ALL values are missing":
            before = len(cleaned)
            cleaned = cleaned.dropna(how="all")
            st.info(f"Removed {before - len(cleaned)} rows where all values were missing.")
        return cleaned

    for col, method in plan.items():
        if col == "__action__":
            continue
        try:
            if method == "Median":
                cleaned[col] = cleaned[col].fillna(cleaned[col].median())
            elif method == "Mean":
                cleaned[col] = cleaned[col].fillna(cleaned[col].mean())
            elif method == "Mode":
                mode_val = cleaned[col].mode()
                if len(mode_val) > 0:
                    cleaned[col] = cleaned[col].fillna(mode_val.iloc[0])
                else:
                    cleaned[col] = cleaned[col].fillna("Unknown")
            elif method == "Forward Fill":
                cleaned[col] = cleaned[col].ffill()
            elif method == "Backward Fill":
                cleaned[col] = cleaned[col].bfill()
            elif method == "Interpolation":
                if cleaned[col].dtype in ["float64", "int64", "float32", "int32"]:
                    cleaned[col] = cleaned[col].interpolate(method="linear")
                    cleaned[col] = cleaned[col].bfill().ffill()
                else:
                    cleaned[col] = cleaned[col].ffill()
            elif method == "Custom Value":
                cleaned[col] = cleaned[col].fillna("Unknown")
        except Exception:
            # Fallback: fill with "Unknown" for categorical, or median for numeric
            if cleaned[col].dtype in ["object", "category", "str"]:
                cleaned[col] = cleaned[col].fillna("Unknown")
            else:
                cleaned[col] = cleaned[col].fillna(cleaned[col].median())

    return cleaned


def remove_duplicates(df: pd.DataFrame) -> Tuple[pd.DataFrame, int]:
    """Remove duplicate rows and return cleaned df + count removed."""
    before = len(df)
    cleaned = df.drop_duplicates()
    removed = before - len(cleaned)
    return cleaned, removed


def validate_dataset(df: pd.DataFrame) -> Dict[str, Any]:
    """Validate the cleaned dataset and return validation results."""
    total_missing = int(df.isnull().sum().sum())
    duplicate_rows = int(df.duplicated().sum())
    completely_empty_cols = [col for col in df.columns if df[col].isnull().all()]
    completely_empty_rows = int((df.isnull().all(axis=1)).sum())
    return {
        "total_missing": total_missing,
        "duplicate_rows": duplicate_rows,
        "rows": df.shape[0],
        "columns": df.shape[1],
        "completely_empty_columns": completely_empty_cols,
        "completely_empty_rows": completely_empty_rows,
        "is_clean": total_missing == 0 and duplicate_rows == 0,
    }


def create_download_file(df: pd.DataFrame, file_type: str) -> BytesIO:
    """Create an in-memory file for download."""
    buffer = BytesIO()
    if file_type == "csv":
        df.to_csv(buffer, index=False)
        mime = "text/csv"
    else:
        df.to_excel(buffer, index=False, engine="openpyxl")
        mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    buffer.seek(0)
    return buffer, mime


# ══════════════════════════════════════════════
# SESSION STATE INITIALIZATION
# ══════════════════════════════════════════════

def init_session_state():
    """Initialize all session state variables."""
    defaults = {
        "original_df": None,
        "cleaned_df": None,
        "file_name": None,
        "file_type": None,
        "upload_success": False,
        "cleaning_done": False,
        "missing_handled": False,
        "duplicates_removed": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_session():
    """Reset all session state to defaults."""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    init_session_state()


init_session_state()


# ══════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════

st.markdown(
    '<div class="main-header">'
    "<h1>🧹 DATA CLEANING & QUALITY PLATFORM</h1>"
    "<p>Professional automated data cleaning — upload, analyze, clean, and download</p>"
    "</div>",
    unsafe_allow_html=True,
)


# ══════════════════════════════════════════════
# SIDEBAR — RESET
# ══════════════════════════════════════════════

with st.sidebar:
    st.header("⚙️ Controls")
    if st.button("🔄 Start Over / Reset", use_container_width=True):
        reset_session()
        st.rerun()
    st.divider()
    st.caption("Upload a CSV or Excel file to begin.")


# ══════════════════════════════════════════════
# 1. FILE UPLOAD
# ══════════════════════════════════════════════

st.markdown('<div class="section-header">📁 1. Upload Your Dataset</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Drag and drop your CSV or Excel file here, or browse your computer.",
    type=["csv", "xlsx", "xls"],
    help="Supported formats: CSV (.csv), Excel (.xlsx, .xls)",
)

if uploaded_file is not None and not st.session_state.upload_success:
    with st.spinner("Reading and loading dataset..."):
        df, file_type, error_msg = load_dataset(uploaded_file)

    if error_msg:
        st.error(f"❌ {error_msg}")
    elif df is not None:
        if df.empty:
            st.error("❌ The uploaded file is empty. Please upload a file with data.")
        elif df.shape[1] == 0:
            st.error("❌ The file contains no columns. Please check your file.")
        else:
            st.session_state.original_df = df.copy()
            st.session_state.cleaned_df = df.copy()
            st.session_state.file_name = uploaded_file.name
            st.session_state.file_type = file_type
            st.session_state.upload_success = True
            st.session_state.cleaning_done = False
            st.session_state.missing_handled = False
            st.session_state.duplicates_removed = False
            st.markdown(
                '<div class="status-box status-success" style="animation: bounceIn 0.5s ease-out;">'
                f'✅ Successfully loaded <strong>{uploaded_file.name}</strong> — '
                f'{df.shape[0]:,} rows × {df.shape[1]} columns'
                '</div>',
                unsafe_allow_html=True,
            )


# ══════════════════════════════════════════════
# MAIN CONTENT (shown only when data is loaded)
# ══════════════════════════════════════════════

if st.session_state.original_df is not None:
    df = st.session_state.original_df
    summary = get_dataset_summary(df)

    # ──────────────────────────────────────────
    # CLEANING PIPELINE STATUS
    # ──────────────────────────────────────────
    steps_done = 0
    steps_total = 4
    if st.session_state.upload_success:
        steps_done += 1
    if st.session_state.missing_handled:
        steps_done += 1
    if st.session_state.duplicates_removed:
        steps_done += 1
    # Validation always runs at the end
    if steps_done == 3:
        steps_done += 1

    pipeline_pct = int(steps_done / steps_total * 100)
    pipeline_labels = {0: "Uploaded", 1: "Missing handled", 2: "Duplicates removed", 3: "Validating...", 4: "Clean!"}
    current_label = pipeline_labels.get(min(steps_done, 4), "Processing...")

    st.progress(
        pipeline_pct,
        text=f"Pipeline: {current_label} ({steps_done}/{steps_total} steps)",
    )

    # ──────────────────────────────────────────
    # 2. DATASET OVERVIEW
    # ──────────────────────────────────────────
    st.markdown('<div class="section-header">📊 2. Dataset Overview</div>', unsafe_allow_html=True)

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Rows", f"{summary['rows']:,}")
    c2.metric("Columns", summary["columns"])
    c3.metric("Missing Values", f"{summary['total_missing']:,}")
    c4.metric("Duplicate Rows", f"{summary['duplicate_rows']:,}")
    c5.metric("Numeric Cols", len(summary["numeric_columns"]))
    c6.metric("Categorical Cols", len(summary["categorical_columns"]))

    # ──────────────────────────────────────────
    # Column details
    # ──────────────────────────────────────────
    st.markdown("##### Column Details")
    col_info = get_column_info(df)
    st.dataframe(col_info, use_container_width=True, hide_index=True)

    # ──────────────────────────────────────────
    # 3. DATASET INFORMATION (df.info style)
    # ──────────────────────────────────────────
    st.markdown('<div class="section-header">📋 3. Dataset Information</div>', unsafe_allow_html=True)

    st.info(
        f"Dataset contains **{summary['rows']:,} rows** and **{summary['columns']} columns**. "
        f"**{len(summary['numeric_columns'])}** columns are numeric and "
        f"**{len(summary['categorical_columns'])}** columns are categorical."
    )

    with st.expander("View Detailed Column Information"):
        info_rows = []
        for col in df.columns:
            dtype = str(df[col].dtype)
            non_null = int(df[col].count())
            null_count = int(df[col].isnull().sum())
            mem_usage = df[col].memory_usage(deep=True)
            if mem_usage < 1024:
                mem_str = f"{mem_usage} B"
            elif mem_usage < 1024 ** 2:
                mem_str = f"{mem_usage / 1024:.1f} KB"
            else:
                mem_str = f"{mem_usage / (1024 ** 2):.1f} MB"
            info_rows.append({
                "Column": col,
                "Data Type": dtype,
                "Non-Null": non_null,
                "Null": null_count,
                "Memory": mem_str,
            })
        st.dataframe(pd.DataFrame(info_rows), use_container_width=True, hide_index=True)

    # ──────────────────────────────────────────
    # 4. DATA PREVIEW
    # ──────────────────────────────────────────
    st.markdown('<div class="section-header">👀 4. Data Preview</div>', unsafe_allow_html=True)

    preview_rows = st.selectbox("Number of rows to preview:", [5, 10, 25, 50, 100], index=1)
    st.dataframe(df.head(preview_rows), use_container_width=True, height=400)

    # ──────────────────────────────────────────
    # 5. MISSING VALUE ANALYSIS
    # ──────────────────────────────────────────
    st.markdown('<div class="section-header">🔍 5. Missing Value Analysis</div>', unsafe_allow_html=True)

    missing_df = analyze_missing_values(df)
    total_cells = df.shape[0] * df.shape[1]

    if missing_df.empty:
        st.success("✅ No missing values were detected in this dataset.")
    else:
        st.dataframe(missing_df, use_container_width=True, hide_index=True)
        cols_with_missing = len(missing_df)
        overall_missing_pct = round(summary["total_missing"] / total_cells * 100, 2) if total_cells > 0 else 0

        c1, c2, c3 = st.columns(3)
        c1.metric("Total Missing Cells", f"{summary['total_missing']:,}")
        c2.metric("Columns with Missing", cols_with_missing)
        c3.metric("% of Dataset Missing", f"{overall_missing_pct}%")

    # ──────────────────────────────────────────
    # 6. MISSING VALUE HANDLING
    # ──────────────────────────────────────────
    if summary["total_missing"] > 0 and not st.session_state.missing_handled:
        st.markdown('<div class="section-header">🛠️ 6. Missing Value Handling</div>', unsafe_allow_html=True)

        strategy = st.radio(
            "How would you like to handle missing values?",
            [
                "Remove rows containing any missing value",
                "Remove rows where ALL values are missing",
                "Fill missing values automatically (intelligent mode)",
                "Custom handling per data type",
            ],
            index=2,
        )

        auto_mode = False
        numeric_method = "Median"
        categorical_method = "Mode"
        datetime_method = "Forward Fill"

        if strategy == "Fill missing values automatically (intelligent mode)":
            auto_mode = True
        elif strategy == "Custom handling per data type":
            st.subheader("Numeric Column Strategy")
            numeric_method = st.selectbox(
                "Strategy for numeric columns:",
                ["Median", "Mean", "Forward Fill", "Backward Fill", "Interpolation"],
                index=0,
            )
            st.subheader("Categorical / String Column Strategy")
            categorical_method = st.selectbox(
                "Strategy for categorical columns:",
                ["Mode", "Forward Fill", "Backward Fill", "Custom Value"],
                index=0,
            )
            st.subheader("Datetime Column Strategy")
            datetime_method = st.selectbox(
                "Strategy for datetime columns:",
                ["Forward Fill", "Backward Fill", "Interpolation"],
                index=0,
            )

        # Build and display plan
        plan = build_cleaning_plan(df, strategy, numeric_method, categorical_method, datetime_method, auto_mode)

        st.markdown("##### 📋 Cleaning Plan Preview")
        if "__action__" in plan:
            st.markdown(
                f'<div class="cleaning-plan">{plan["__action__"]}</div>',
                unsafe_allow_html=True,
            )
            # Show impact
            before_count = len(df)
            if "any" in plan["__action__"]:
                after_count = len(df.dropna())
            else:
                after_count = len(df.dropna(how="all"))
            st.warning(
                f"This operation will remove **{before_count - after_count:,}** rows "
                f"(from {before_count:,} → {after_count:,})."
            )
        else:
            plan_lines = [f"**{col}** &nbsp;→&nbsp; {method}" for col, method in plan.items()]
            st.markdown(
                '<div class="cleaning-plan">' + "<br>".join(plan_lines) + "</div>",
                unsafe_allow_html=True,
            )

        if st.button("✅ Confirm and Apply Missing Value Handling", type="primary", use_container_width=True):
            st.markdown(
                '<div class="cleaning-plan" style="animation: fadeInUp 0.3s ease-out;">'
                '🔄 Cleaning in progress...'
                '</div>',
                unsafe_allow_html=True,
            )
            progress = st.progress(0, text="Preparing...")

            import time
            steps = [
                (10, "Analyzing columns..."),
                (30, "Detecting data types..."),
                (50, "Applying fill strategies..."),
                (75, "Verifying results..."),
                (95, "Finalizing..."),
            ]
            for pct, label in steps:
                progress.progress(pct, text=label)
                time.sleep(0.15)

            st.session_state.cleaned_df = apply_missing_value_strategy(
                st.session_state.cleaned_df, plan
            )
            st.session_state.missing_handled = True

            progress.progress(100, text="Done!")
            time.sleep(0.3)
            st.markdown(
                '<div class="status-box status-success" style="animation: bounceIn 0.5s ease-out;">'
                '✅ Missing values have been handled successfully.'
                '</div>',
                unsafe_allow_html=True,
            )
            time.sleep(0.4)
            st.rerun()

    # ──────────────────────────────────────────
    # 8. DUPLICATE RECORD DETECTION
    # ──────────────────────────────────────────
    st.markdown('<div class="section-header">🔁 8. Duplicate Records</div>', unsafe_allow_html=True)

    cleaned = st.session_state.cleaned_df
    dup_count = int(cleaned.duplicated().sum())
    dup_pct = round(dup_count / len(cleaned) * 100, 2) if len(cleaned) > 0 else 0

    if dup_count == 0:
        st.success("✅ No duplicate records found.")
    else:
        c1, c2 = st.columns(2)
        c1.metric("Duplicate Rows", f"{dup_count:,}")
        c2.metric("Duplicate %", f"{dup_pct}%")

        if not st.session_state.duplicates_removed:
            st.warning(f"⚠️ **{dup_count:,}** duplicate records were detected and will be removed.")
            if st.button("🗑️ Remove Duplicate Records", type="primary", use_container_width=True):
                import time
                progress = st.progress(0, text="Scanning for duplicates...")
                time.sleep(0.3)
                progress.progress(50, text="Removing duplicates...")
                st.session_state.cleaned_df, removed = remove_duplicates(st.session_state.cleaned_df)
                st.session_state.duplicates_removed = True
                progress.progress(100, text="Done!")
                time.sleep(0.3)
                st.markdown(
                    '<div class="status-box status-success" style="animation: bounceIn 0.5s ease-out;">'
                    f'✅ {removed:,} duplicate rows removed successfully.'
                    '</div>',
                    unsafe_allow_html=True,
                )
                time.sleep(0.4)
                st.rerun()

    # ──────────────────────────────────────────
    # 10. BEFORE vs AFTER COMPARISON
    # ──────────────────────────────────────────
    st.markdown('<div class="section-header">📈 10. Cleaning Results — Before vs After</div>', unsafe_allow_html=True)

    original = st.session_state.original_df
    cleaned_final = st.session_state.cleaned_df

    orig_summary = get_dataset_summary(original)
    clean_summary = get_dataset_summary(cleaned_final)

    rows_removed = orig_summary["rows"] - clean_summary["rows"]
    missing_resolved = orig_summary["total_missing"] - clean_summary["total_missing"]
    dups_removed = orig_summary["duplicate_rows"] - clean_summary["duplicate_rows"]

    comparison = pd.DataFrame({
        "Metric": ["Rows", "Columns", "Missing Values", "Duplicate Rows"],
        "Before": [
            f"{orig_summary['rows']:,}",
            orig_summary["columns"],
            f"{orig_summary['total_missing']:,}",
            f"{orig_summary['duplicate_rows']:,}",
        ],
        "After": [
            f"{clean_summary['rows']:,}",
            clean_summary["columns"],
            f"{clean_summary['total_missing']:,}",
            f"{clean_summary['duplicate_rows']:,}",
        ],
        "Change": [
            f"-{rows_removed:,}" if rows_removed > 0 else "0",
            "0",
            f"-{missing_resolved:,}" if missing_resolved > 0 else "0",
            f"-{dups_removed:,}" if dups_removed > 0 else "0",
        ],
    })
    st.dataframe(comparison, use_container_width=True, hide_index=True)

    if st.session_state.missing_handled or st.session_state.duplicates_removed:
        st.success(
            f"Cleaning completed successfully.\n\n"
            f"• {missing_resolved:,} missing values handled\n"
            f"• {dups_removed:,} duplicate rows removed\n"
            f"• {clean_summary['rows']:,} rows retained"
        )

    # ──────────────────────────────────────────
    # 11. CLEANED DATASET PREVIEW
    # ──────────────────────────────────────────
    st.markdown('<div class="section-header">🔎 11. Cleaned Dataset Preview</div>', unsafe_allow_html=True)

    view_option = st.radio(
        "View:", ["First N rows", "Last N rows", "Random sample"], horizontal=True
    )
    n_rows = st.selectbox("Number of rows:", [5, 10, 25, 50, 100], index=1, key="clean_preview_n")

    if view_option == "First N rows":
        preview_data = cleaned_final.head(n_rows)
    elif view_option == "Last N rows":
        preview_data = cleaned_final.tail(n_rows)
    else:
        preview_data = cleaned_final.sample(min(n_rows, len(cleaned_final)), random_state=42)

    st.dataframe(preview_data, use_container_width=True, height=400)

    # ──────────────────────────────────────────
    # 12. DATA VALIDATION
    # ──────────────────────────────────────────
    st.markdown('<div class="section-header">✅ 12. Data Validation</div>', unsafe_allow_html=True)

    validation = validate_dataset(cleaned_final)

    if validation["total_missing"] > 0:
        # Find which columns still have missing
        remaining_missing = cleaned_final.columns[cleaned_final.isnull().any()].tolist()
        remaining_detail = analyze_missing_values(cleaned_final)
        st.warning("⚠️ Some missing values remain in specific columns and require manual review.")
        st.dataframe(remaining_detail, use_container_width=True, hide_index=True)
    else:
        st.markdown(
            '<div class="status-box status-success">'
            "✅ No missing values<br>"
            "✅ No duplicate records<br>"
            "✅ Dataset successfully cleaned"
            "</div>",
            unsafe_allow_html=True,
        )

    if validation["completely_empty_columns"]:
        st.warning(
            f"⚠️ The following columns are completely empty: "
            f"`{', '.join(validation['completely_empty_columns'])}`"
        )
    if validation["completely_empty_rows"] > 0:
        st.warning(
            f"⚠️ {validation['completely_empty_rows']} completely empty rows remain."
        )

    # ──────────────────────────────────────────
    # 13. DOWNLOAD CLEANED DATASET
    # ──────────────────────────────────────────
    st.markdown('<div class="section-header">💾 13. Download Cleaned Dataset</div>', unsafe_allow_html=True)

    base_name = st.session_state.file_name.rsplit(".", 1)[0] if st.session_state.file_name else "dataset"

    col_dl1, col_dl2, _ = st.columns([1, 1, 1])

    with col_dl1:
        csv_buffer, csv_mime = create_download_file(cleaned_final, "csv")
        st.download_button(
            label="📥 Download as CSV",
            data=csv_buffer,
            file_name=f"{base_name}_cleaned.csv",
            mime=csv_mime,
            use_container_width=True,
        )

    with col_dl2:
        xlsx_buffer, xlsx_mime = create_download_file(cleaned_final, "excel")
        st.download_button(
            label="📥 Download as Excel",
            data=xlsx_buffer,
            file_name=f"{base_name}_cleaned.xlsx",
            mime=xlsx_mime,
            use_container_width=True,
        )


# ══════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════

st.divider()
st.caption("Data Cleaning & Quality Platform — Built with Streamlit, Pandas, and NumPy")
