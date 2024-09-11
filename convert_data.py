import json
from pathlib import Path

all_sents = []
with open('SLING_DATA/animate.jsonl', 'r') as f:
    for line in f:
        all_sents.append(json.loads(line))

with open('SLING_DATA/Anaphor/animate_baseline.jsonl', 'w') as sl:
    for s in all_sents:
        new_good = s['sentence_good']
        new_bad = s['sentence_bad']
        phenomenon = 'animacy_as_subj'
        pron = new_good[2]

        animate_n = new_good.split('，')[0][4:-5]
        new_good = new_good[:2]+animate_n+new_good[3]+pron+new_good.split('，')[0][-5:]+'，那么'+pron+new_good.split('，')[0][-5:-2]+pron+'自己。'

        bad = new_good[:-4]+'它。'
        d = {'sentence_good':new_good, 'sentence_bad':bad, 'phenomenon':phenomenon}
        json.dump(d, sl, ensure_ascii=False)
        sl.write('\n')

        print(new_good, bad)
