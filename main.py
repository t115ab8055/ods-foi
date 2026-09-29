import csv
from datetime import date, timedelta

from servers import get_all_data

url = "https://ods.foi.org.tw/"


roc_year = date.today().year - 1911  # noqa: DTZ011
start_date = date(roc_year, 1, 1)
year_end = date(roc_year, 12, 31)

parse_data = []
while start_date <= year_end:
    end_date = min(start_date + timedelta(days=30), year_end)

    print(f"開始時間：{start_date.month}/{start_date.day} 結束時間：{end_date.month}/{end_date.day}")
    parse_data += get_all_data(
        start_month=start_date.month,
        start_day=start_date.day,
        end_month=end_date.month,
        end_day=end_date.day,
    )

    start_date = end_date + timedelta(days=1)

for index, data in enumerate(parse_data, 1):
    data[0] = index
    print(data)

with open("評議決定書.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)

    writer.writerow(["序號", "文件類型", "案號與連結", "評議日期", "爭議類型"])
    writer.writerows(parse_data)