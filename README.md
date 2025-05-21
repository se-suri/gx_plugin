# `gx_plugin` – Reusable Great Expectations Cloud Plugin

A Python plugin that simplifies setting up and using [Great Expectations Cloud](https://greatexpectations.io/) across multiple projects.
It provides reusable expectations, data validation helpers, and a minimal configuration-based setup via `gx_config.yml`.

---

## Features

* Connects to **GX Cloud** with minimal config
* Registers **CSV datasources**
* Applies **prebuilt reusable expectations**
* Fully configurable per project
* Supports automation and CLI usage

---

## Directory overview

```
gx_plugin/
├── config.py             # Loads per-project gx_config.yml
├── gx_utils.py           # Functions for datasource and suite setup
├── cli.py                # CLI entry point (gx-init)
└── expectations/         # Reusable expectation modules
```

---

## Installation

Clone and install the plugin locally:

```bash
git clone https://github.com/se-suri/gx_plugin.git
cd gx_plugin
pip install -e .
```

---

## Project setup

Each new project that uses `gx_plugin` should have this structure:

```
my_project/
├── data/
│   └── scraping.csv
├── gx_config.yml          # Per-project GX config
└── main.py or gx-init     # Script to run validation
```

Example `gx_config.yml` (stored in this directory - move it to the project directory and edit accordingly):

```yaml
project_name: "scraping-prices"
datasource_name: "csv_scraping"
suite_name: "default_suite"
csv_path: "data/scraping.csv"
ge_cloud_organization_id: "<your-org-id>"
ge_cloud_access_token: "<your-token>"
ge_cloud_base_url: "https://app.greatexpectations.io/"
```

---

## Usage

Once `gx_plugin` is installed and `gx_config.yml` is configured:

```bash
gx-init
```

This will:

* Connect to GX Cloud
* Add your CSV as a datasource
* Create an expectation suite
* Attach reusable expectations

---

## Adding new expectations

Create a new Python file in `gx_plugin/expectations/`:

```python
# gx_plugin/expectations/expect_column_discount_range.py

def add_expectations(suite):
    suite.expect_column_values_to_be_between(
        column="discount",
        min_value=0,
        max_value=100
    )
```

Reference it in your validation script or CLI:

```python
create_suite(context, suite_name, expectations=[
    "expect_column_discount_range"
])
```

---