import requests

cookies = {
    '_ga': 'GA1.2.262409860.1699862836',
    '_gid': 'GA1.2.1182568215.1699862836',
    'session': '53616c7465645f5f0bc8fb771db0e997b50787bd9367a52032f82e5c5ad960a4b7e1abedfc3dd00c26dbce8b4996c590e4e5800b068cad5e1c1e1883eddb85b8',
    '_gat': '1',
    '_ga_MHSNPJKWC7': 'GS1.2.1699894081.2.1.1699898276.0.0.0',
}

headers = {
    'authority': 'adventofcode.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # 'cookie': '_ga=GA1.2.262409860.1699862836; _gid=GA1.2.1182568215.1699862836; session=53616c7465645f5f0bc8fb771db0e997b50787bd9367a52032f82e5c5ad960a4b7e1abedfc3dd00c26dbce8b4996c590e4e5800b068cad5e1c1e1883eddb85b8; _gat=1; _ga_MHSNPJKWC7=GS1.2.1699894081.2.1.1699898276.0.0.0',
    'referer': 'https://adventofcode.com/2023/events',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}


def get_input(url):
    file_name = "day" + url.replace("/", "-").split("day")[1] + ".txt"
    try:
        with open(f"{file_name}", "r") as file:
            input_text = file.read()
    except FileNotFoundError:
        response = requests.get(url, cookies=cookies, headers=headers)
        with open(f"{file_name}", "w") as file:
            file.write(response.text)
            input_text = response.text
    return input_text
