n = int(input())
transactions = []

for _ in range(n):
    data = input().split()
    transactions.append(data)

validate_transactions(n, transactions)
