from gx_plugin.config import load_config
from gx_plugin.gx_utils import init_gx_context, add_csv_datasource, create_suite
from great_expectations.checkpoint import Checkpoint
from great_expectations.datasource.fluent import PandasDatasource


def run():
    config = load_config()
    context = init_gx_context(config)

    add_csv_datasource(context, config["datasource_name"], config["csv_path"])
    create_suite(context, config["suite_name"], expectations=[
        "expect_column_postal_code_format",
        "expect_column_price_range"
    ])

    batch_request = {
        "datasource_name": config["datasource_name"],
        "data_connector_name": "default_runtime_data_connector_name",
        "data_asset_name": "default_asset_name",
        "runtime_parameters": {
            "path": config["csv_path"]
        },
        "batch_identifiers": {
            "default_identifier_name": "default_identifier"
        }
    }

    checkpoint = Checkpoint(
        name="gx_plugin_checkpoint",
        data_context=context,
        validations=[
            {
                "batch_request": batch_request,
                "expectation_suite_name": config["suite_name"]
            }
        ]
    )

    results = checkpoint.run()
    print("Validation complete. Results uploaded to GX Cloud.")