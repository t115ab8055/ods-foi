import requests
from bs4 import BeautifulSoup
from requests import Response

from crawler import get_header, get_home_payload


def get_ods_foi_response(
    start_month: int = 1,
    start_day: int = 1,
    end_month: int = 1,
    end_day: int = 31,
    industry_id: str = "",
    sub_industry_id: str = "0",
    dispute_type_id: str = "0",
) -> Response:
    url = "https://ods.foi.org.tw/"
    response = requests.post(
        url,
        headers=get_header(),
        data=get_home_payload(
            start_month=start_month,
            start_day=start_day,
            end_month=end_month,
            end_day=end_day,
            industry_id=industry_id,
            sub_industry_id=sub_industry_id,
            dispute_type_id=dispute_type_id,
        ),
        timeout=30,
    )
    response.raise_for_status()

    return response


def get_industry_select_name(response: Response) -> dict:
    """獲取產業類別資料"""
    soup = BeautifulSoup(response.content, "html.parser")
    select = soup.find(id="cph_content_ddlVerticals")
    options = select.find_all("option")

    data = {}
    for option in options[1:]:
        value = option.get("value")
        text = option.get_text("", strip=True)
        data[value] = text

    return data


def get_sub_industry_select_name(industry_select_id: str) -> dict:
    """獲取子產業類別資料"""

    url = "https://ods.foi.org.tw/ddlUse.aspx/GetSubVerticals"
    response = requests.post(
        url,
        headers=get_header(),
        json={"IndID": industry_select_id},
        timeout=30,
    )
    response.raise_for_status()
    industry_options = {item["Value"]: item["Text"] for item in response.json()["d"]}

    return industry_options


def get_dispute_type_select_name(
    indid: str,
    indsubid: str,
    btype: str = "0",
    resid: str = "0",
    ressubid: str = "0",
) -> dict:
    """獲取爭議類型類別資料"""

    url = "https://ods.foi.org.tw/ddlUse.aspx/GetControversyKind1"
    response = requests.post(
        url,
        headers=get_header(),
        json={
            "BType": btype,
            "ResID": resid,
            "ResSubID": ressubid,
            "IndID": indid,
            "IndSubID": indsubid,
        },
        timeout=30,
    )
    response.raise_for_status()
    dispute_type_options = {item["Value"]: item["Text"] for item in response.json()["d"]}

    return dispute_type_options


# get_sub_industry_select_name("E01")
# get_dispute_type_select_name("B01", "002")
