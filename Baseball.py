import re
import sys
from collections import OrderedDict

if len(sys.argv) != 2:
    sys.exit("Usage: %s filename" %sys.argv[0])

regex = re.compile(r"^([A-Za-z]+\s[A-Za-z]+)\s(?:\w+)\s(\d+)\s(?:\w+)\s(?:\w+)\s(\d)")
dict = {}

with open(sys.argv[1]) as f:
# with open("cardinals-1940.txt") as f:
    for line in f:

        # name_batted_hits = re.match(regex, data)

        match = regex.match(line)
        if match is not None:
            name = match.group(1)
            batted_matched = match.group(2)
            hits_matched = match.group(3)

            if name in dict:
                batted_old = dict[name][0]
                hits_old = dict[name][1]
                batted_new = float(batted_old) + float(batted_matched)
                hits_new = float(hits_old) + float(hits_matched)
                dict[name] = [batted_new, hits_new]

            else:
                dict[name] = [batted_matched, hits_matched]

avg_dict = dict.copy()
for k, v in avg_dict.items():
    avg = float(v[1]) / float(v[0])
    rounded_avg = round(avg, 3)
    avg_dict[k] = rounded_avg

sorted_dict = OrderedDict(sorted(avg_dict.items(), key=lambda kv: kv[1], reverse=True))

for k, v in sorted_dict.items():
    print("%s: %.3f" % (k, sorted_dict[k]))
