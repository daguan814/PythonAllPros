import requests

# question = [76, 101, 117, 95///, 144, 147, 172, 170]
# value = [2, 1, 2, 3///, 2, 1, 4, 3]

url = "https://api.hubei21.com/api/stop_exam"
token = "c53e95b5246eadaddd2962ab3795fdb7"
headers = {
    "token": token,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    "Content-Type": "application/json"
}
data = {
    "id": 153334,
    "content_answer": r'[{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":3},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2},{"id":144,"value":2}]'
}

response = requests.post(url, headers=headers, json=data)
print(response.text)
