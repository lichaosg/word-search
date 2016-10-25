import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "word_search.settings")
import django
django.setup()


if __name__ == '__main__':
    from main.models import Synonyms
else:
    from ..main.models import Synonyms

pairs = []

with open('./data/mobythes.aur', 'rU') as fin:
    for i, line in enumerate(fin):
        words = line.split(',')
        root = words[0]
        for syno in words[1:]:
            pair = Synonyms(word=root, synonym=syno)
            pairs.append(pair)
        print i, root

print "%s pairs"%len(pairs)

Synonyms.objects.bulk_create(pairs)