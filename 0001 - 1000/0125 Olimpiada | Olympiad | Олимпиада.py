
h1, m1, s1 = input().split()
h2, m2, s2 = input().split()

h1, m1, s1 = int(h1), int(m1), int(s1)
h2, m2, s2 = int(h2), int(m2), int(s2)

bir_san = h1 * 3600 + m1 * 60 + s1
iki_san = h2 * 3600 + m2 * 60 + s2

ferq = iki_san - bir_san

netice_saat = ferq // 3600
netice_deq = (ferq - netice_saat * 3600) // 60
netice_san = ferq - (netice_saat * 3600 + netice_deq * 60)

print(netice_saat, netice_deq, netice_san)

