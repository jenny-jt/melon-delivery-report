def melon_count(day_num, path)
    print("Day", day_num)
    delivery_log = open(path)

for line in delivery_log:
    line = line.rstrip()
    words = line.split('|')

    melon, count, amount = words

    print(f"Delivered {count} {melon}s for total of ${amount}")
delivery_log.close()

melon_count(1, "um-deliveries-20140519.txt")
melon_count(2, "um-deliveries-20140520.txt")
melon_count(3, "um-deliveries-20140521.txt")