# Retail Sales Data Pipeline

A small, end-to-end retail sales data engineering project built with Python, pandas, and SQLite. It takes a raw CSV through validation and cleaning, writes a reproducible cleaned CSV, loads the result into a local SQL database, and reports useful sales metrics.

> **Project scope:** This is a local, Foundry-inspired data engineering project. It demonstrates pipeline concepts such as ingestion, transformation, validation, loading, and analytics. It is **not** hands-on experience with the Palantir Foundry platform, and it does not use Foundry services or APIs.

## Pipeline workflow

1. **Ingest and clean** — `pipeline.py` reads `raw_sales.csv`, applies the cleaning rules below, calculates `total_amount`, and writes `cleaned_sales.csv`.
2. **Load** — `load_to_sql.py` loads the cleaned rows into the `sales` table in `retail_sales.db`, replacing that table on each run.
3. **Analyze** — `sql_analytics.py` runs five SQLite queries and prints revenue, city, product, top-order, and average-order metrics.
4. **Orchestrate and log** — `run_pipeline.py` executes those three scripts in order using the current Python interpreter. It writes progress and errors to `pipeline.log`, stops if a stage fails, and returns a failure exit code.

Run the orchestrator from this folder so the scripts find their CSV and database files using their relative paths.

## Project files

| File | Purpose |
| --- | --- |
| `raw_sales.csv` | Sample source data with seven rows, including a missing city, a duplicate order, and an invalid quantity. |
| `pipeline.py` | Cleans the source records, derives `total_amount`, and creates `cleaned_sales.csv`. |
| `cleaned_sales.csv` | Generated output containing the five retained, cleaned orders. |
| `load_to_sql.py` | Loads the cleaned CSV into the SQLite `sales` table. |
| `retail_sales.db` | Generated local SQLite database. |
| `sql_analytics.py` | Runs the five SQL analyses against `sales`. |
| `run_pipeline.py` | Runs the cleaning, loading, and analytics scripts sequentially and records execution in the log. |
| `pipeline.log` | Generated run log with stage progress or error details. |
| `.gitignore` | Excludes the generated database, cleaned output, log, and Python cache files from Git. |

## Technologies

- Python 3
- pandas for CSV input, row cleaning, and CSV output
- SQLite (`sqlite3`) for local relational storage and SQL queries
- Python standard library modules: `subprocess`, `sys`, and `logging`

## Requirements

- Windows 10 or 11
- Python 3.9 or later
- pandas

## Run on Windows

Open PowerShell and change to this project directory:

```powershell
cd C:\path\to\palantir_learning\retail_sales_project
```

Create and activate a virtual environment, then install pandas:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pandas
```

Run the complete pipeline:

```powershell
python run_pipeline.py
```

The script prints each stage and the SQL results. On success, `cleaned_sales.csv`, `retail_sales.db`, and `pipeline.log` are created or refreshed in the project folder. The database load replaces the existing `sales` table, making repeated runs refresh that table from the current CSV. The `.gitignore` excludes these generated outputs from version control.

If PowerShell blocks virtual-environment activation, either use `python -m pip install pandas` with your chosen Python environment, or run the environment's interpreter directly:

```powershell
.\.venv\Scripts\python.exe run_pipeline.py
```

## Validation and cleaning rules

The current code applies these rules in `pipeline.py`, in order:

- Replace missing `city` values with `Unknown`.
- For repeated `order_id` values, keep the first row and drop later duplicates.
- Keep rows only when `quantity` and `unit_price` are greater than zero. This removes zero or negative values in either field.
- Parse `order_date` as a date; discard rows whose date cannot be parsed.
- Calculate `total_amount` as `quantity * unit_price`.
- Write the result to `cleaned_sales.csv` without a pandas index column.

With the supplied sample data, the duplicate order `101` is reduced to its first occurrence, the row with quantity `-1` is removed, the blank city is filled as `Unknown`, and five rows remain. The supplied dates all parse successfully.

## SQL analytics and sample results

`sql_analytics.py` runs the following queries against the loaded `sales` table:

1. Sum of `total_amount` for total revenue.
2. Revenue grouped by city, ordered from highest to lowest.
3. Quantity grouped by product, ordered from highest to lowest.
4. Highest-value individual order.
5. Average `total_amount` per order.

For the included sample data, the generated cleaned CSV contains these results:

| Metric | Result |
| --- | ---: |
| Retained orders | 5 |
| Total revenue | 118,000 |
| Average order value | 23,600 |
| Highest revenue order | Order 101 — Ravi — 55,000 |

**Revenue by city**

| City | Revenue |
| --- | ---: |
| Hyderabad | 55,000 |
| Chennai | 30,000 |
| Delhi | 24,000 |
| Unknown | 6,000 |
| Bangalore | 3,000 |

**Units sold by product**

| Product | Quantity |
| --- | ---: |
| Headphones | 3 |
| Mobile | 2 |
| Keyboard | 2 |
| Monitor | 2 |
| Laptop | 1 |

These figures describe the checked-in sample data; results change when `raw_sales.csv` changes.

## Notes and limitations

- This is a compact local learning project using a single CSV and a local SQLite database. It has no cloud deployment, orchestration service, access controls, or production monitoring.
- File paths are relative to the current working directory; run the command from `retail_sales_project`.
- The current implementation does not explicitly validate missing values in fields other than `city`, or check that `order_id` and numeric fields have the expected types before calculations.
- The pipeline replaces the `sales` table on every run; it is a refresh workflow rather than an incremental append.
