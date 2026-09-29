def get_header():
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/153.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,image/apng,*/*;q=0.8,"
            "application/signed-exchange;v=b3;q=0.7"
        ),
    }

    return headers

def get_home_payload(start_month: int, start_day: int, end_month: int, end_day: int, industry_id: str, sub_industry_id: str, dispute_type_id: str) -> dict:

    payload = {
        "__LASTFOCUS": "",
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": "fK4XDdVqklyV8lxrAjz8DhRiN3zl2k/OuL4GY+g5UljjW96QXs6VuEl/CljSrBMFusFeBG4PHG8X8BLspjJhqzXEsPxDIuQYD5tEtp9A9ZM8ksICuvhTVpGIecw=",
        "__VIEWSTATEGENERATOR": "CA0B0334",
        "Foi$cph_content$ddlTypeID": "0",
        "Foi$cph_content$ddl_page": "100",
        "Foi$cph_content$ddl_ResultKind": "0",
        "Foi$cph_content$hResName": "",
        "Foi$cph_content$ddlVerticals": industry_id,
        "Foi$cph_content$ddlSubVerticals": sub_industry_id,
        "Foi$cph_content$dll_ControversyKind": dispute_type_id,
        "Foi$cph_content$txt_BYear": "",
        "Foi$cph_content$ddl_BCase": "評",
        "Foi$cph_content$txt_Bno": "",
        "Foi$cph_content$txt_Content": "",
        "Foi$cph_content$txt_Syear": "115",
        "Foi$cph_content$txt_Smonth": f"{start_month}",
        "Foi$cph_content$txt_Sday": f"{start_day}",
        "Foi$cph_content$txt_Eyear": "115",
        "Foi$cph_content$txt_Emonth": f"{end_month}",
        "Foi$cph_content$txt_Eday": f"{end_day}",
        "Foi$cph_content$sdate": "起始評議決定日期",
        "Foi$cph_content$edate": "結束評議決定日期",
        "Foi$cph_content$btn_submit": "送出查詢",
        "Foi$cph_content$ddlOrderBy": "1",
        "Foi$cph_content$hSort": "1",
        "Foi$cph_content$HFrecCurrentPage": "1",
        "Foi$cph_content$HFRecordCount": "100",
        "Foi$cph_content$HFrecPageCount": "1",
    }

    return payload

def get_case_type_payload(typeId: str) -> dict:
    return { "typeId": typeId }