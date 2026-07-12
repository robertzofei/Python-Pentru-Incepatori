# Scenariu 1: range() pentru un număr fix de repetiții
# Vrem să trimitem 3 ping-uri către un IP
for i in range(3):
    # i va lua valorile 0, 1, 2
    print(f"Trimitere pachet de date numărul {i + 1}...")

print("-" * 20)

# Scenariu 2: for pentru a trece prin colecții de date
departamente = ["IT", "HR", "Contabilitate"]

for departament in departamente:
    print(f"Generez raportul lunar pentru departamentul: {departament}")