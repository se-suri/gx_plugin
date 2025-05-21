from great_expectations.data_context import CloudDataContext
from great_expectations.datasource.fluent import PandasDatasource
from pathlib import Path
import importlib

def init_gx_context(config):
    return CloudDataContext(
        ge_cloud_base_url=config["ge_cloud_base_url"],
        ge_cloud_organization_id=config["ge_cloud_organization_id"],
        ge_cloud_access_token=config["ge_cloud_access_token"],
    )

def add_csv_datasource(context, name, path):
    context.sources.add_pandas(name=name)

def create_suite(context, suite_name, expectations):
    suite = context.add_expectation_suite(suite_name)
    for exp in expectations:
        module = importlib.import_module(f"gx_plugin.expectations.{exp}")
        module.add_expectations(suite)
    context.save_expectation_suite(suite)