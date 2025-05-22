def add_expectations(suite):
    suite.expect_column_values_to_match_regex(
        column="postal_code",
        regex=r"^\d{5}$"
    )

    us_states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
        "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR",
        "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]
    suite.expect_column_values_to_not_be_null(
        column="region",
        mostly=1.0
    )
    suite.expect_column_values_to_be_in_set(
        column="region",
        value_set=us_states
    )

    suite.expect_column_values_to_not_be_null(
        column="price"
    )

    suite.expect_column_pair_values_A_to_be_greater_than_B(
        column_A="price",
        column_B="sale_price"
    )

    suite.expect_column_values_to_be_between(
        column="gap %",
        min_value=0.0,
        max_value=0.5,
        mostly=1.0
    )

    suite.expect_column_values_to_not_be_null(
        column="size"
    )
    suite.expect_column_values_to_match_regex(
        column="size",
        regex=r"(?i)\d+(\s?('|ft|feet))?\s?[x×]\s?\d+(\s?('|ft|feet))?"
    )

    suite.expect_column_to_exist(
        column="promotion"
    )
