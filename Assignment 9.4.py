filename = "mbox-short.txt"
handle = open(filename)

senders = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        sender = words[1]
        senders[sender] = senders.get(sender, 0) + 1

max_sender = None
max_count = None

for sender, count in senders.items():
    if max_count is None or count > max_count:
        max_sender = sender
        max_count = count

print(max_sender, max_count)
