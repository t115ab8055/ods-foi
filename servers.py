from requests import Response

from api import (
    get_dispute_type_select_name,
    get_industry_select_name,
    get_ods_foi_response,
    get_sub_industry_select_name,
)
from parse import parse_html, validate_over_limit


def get_industry_layer(
    response: Response,
    start_month: int,
    start_day: int,
    end_month: int,
    end_day: int,
) -> list[list]:
    parse_data = []
    industry_data = get_industry_select_name(response)
    for industry_data_value in industry_data:
        response = get_ods_foi_response(
            start_month=start_month,
            start_day=start_day,
            end_month=end_month,
            end_day=end_day,
            industry_id=industry_data_value,
        )

        response.raise_for_status()
        is_over_limit = validate_over_limit(response, 2)
        if is_over_limit:
            parse_data += get_sub_industry_layer(
                start_month=start_month,
                start_day=start_day,
                end_month=end_month,
                end_day=end_day,
                industry_data_value=industry_data_value,
            )
            continue

        parse_data += parse_html(response)
    return parse_data


def get_sub_industry_layer(
    start_month: int,
    start_day: int,
    end_month: int,
    end_day: int,
    industry_data_value: str,
) -> list[list]:
    parse_data = []
    sub_industry_data = get_sub_industry_select_name(industry_data_value)
    for sub_industry_data_value in sub_industry_data:
        response = get_ods_foi_response(
            start_month=start_month,
            start_day=start_day,
            end_month=end_month,
            end_day=end_day,
            industry_id=industry_data_value,
            sub_industry_id=sub_industry_data_value,
        )

        response.raise_for_status()
        is_over_limit = validate_over_limit(response, 3)
        if is_over_limit:
            parse_data += get_dispute_type_layer(
                start_month=start_month,
                start_day=start_day,
                end_month=end_month,
                end_day=end_day,
                industry_data_value=industry_data_value,
                sub_industry_data_value=sub_industry_data_value,
            )
            continue

        parse_data += parse_html(response)
    return parse_data


def get_dispute_type_layer(
    start_month: int,
    start_day: int,
    end_month: int,
    end_day: int,
    industry_data_value: str,
    sub_industry_data_value: str,
) -> list[list]:
    parse_data = []
    dispute_type_data = get_dispute_type_select_name(industry_data_value, sub_industry_data_value)
    for dispute_type_data_value in dispute_type_data:
        response = get_ods_foi_response(
            start_month=start_month,
            start_day=start_day,
            end_month=end_month,
            end_day=end_day,
            industry_id=industry_data_value,
            sub_industry_id=sub_industry_data_value,
            dispute_type_id=dispute_type_data_value,
        )

        response.raise_for_status()
        validate_over_limit(response, 4)
        parse_data += parse_html(response)

    return parse_data


def get_all_data(
    start_month: int,
    start_day: int,
    end_month: int,
    end_day: int,
) -> list[list]:
    parse_data = []
    response = get_ods_foi_response(
        start_month=start_month,
        start_day=start_day,
        end_month=end_month,
        end_day=end_day,
    )
    is_over_limit = validate_over_limit(response, 1)

    if is_over_limit:
        parse_data += get_industry_layer(
            response=response,
            start_month=start_month,
            start_day=start_day,
            end_month=end_month,
            end_day=end_day,
        )
    else:
        parse_data += parse_html(response)

    return parse_data