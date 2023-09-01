from collections import Counter

def calculate_earnings(shoe_sizes, customer_data):
    size_count = Counter(shoe_sizes)
    total_earnings = 0
    
    for size, price in customer_data:
        if size_count[size] > 0:
            total_earnings += price
            size_count[size] -= 1
    
    return total_earnings

if __name__ == "__main__":
    n = int(input())  # Número de sapatos
    shoe_sizes = list(map(int, input().split()))  # Tamanhos dos sapatos
    m = int(input())  # Número de clientes
    
    customer_data = []
    for _ in range(m):
        size, price = map(int, input().split())
        customer_data.append((size, price))
    
    total_earnings = calculate_earnings(shoe_sizes, customer_data)
    print(total_earnings)
