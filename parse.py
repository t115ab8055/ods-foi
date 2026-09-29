from urllib.parse import urljoin

from bs4 import BeautifulSoup
from requests import Response


def parse_html(response: Response) -> list[list]:
    soup = BeautifulSoup(response.content, "html.parser")

    tables = soup.find_all("table")
    table = tables[1]

    data = []
    for row in table.find_all("tr"):
        cells = row.find_all(["td"], recursive=False)

        rows_list = []
        for cell in cells:
            value = cell.get_text("", strip=True)
            rows_list.append(value)

            if (link := cell.find("a", href=True)):
                link = urljoin(response.url, link.get("href"))

                rows_list.append(link.strip())

        if any(rows_list):
            data.append(rows_list)

    return data


def validate_over_limit(response: Response, layer: int) -> bool:
    soup = BeautifulSoup(response.content, "html.parser")
    message = soup.find(id="cph_content_result_msg")

    print(layer, message.get_text("", strip=True) if message else "未超過 100 筆資料")
    return message is not None