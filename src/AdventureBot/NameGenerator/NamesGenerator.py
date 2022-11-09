import random

a = (set(), set(), set())
b = (set(), set(), set())

with open('dict.opcorpora.txt', encoding='utf-8') as f:
    ln = 0
    line = None
    print('Reading lines...')
    lines = f.readlines()
    print('Processing lines...')
    try:
        for line in lines:
            line = line.strip('\n')
            ln += 1
            splitted = line.split('\t')
            if len(splitted) != 2:
                continue
            word, params = splitted
            params = params.split(',')
            if params[0] == 'NOUN':
                # Сущ
                if params[3] != 'nomn':
                    # Не им. п.
                    continue
                if params[1].split(' ')[-1] != 'anim':
                    # Неодуш
                    continue
                gender, cnt = params[2].split(' ')
                if cnt != 'sing':
                    # Множ ч.
                    continue
                if gender == 'masc':
                    b[0].add(word)
                elif gender == 'femn':
                    b[1].add(word)
                elif gender == 'neut':
                    b[2].add(word)
            elif params[0] in ('ADJF', 'ADJS', 'PRTF', 'PRTS', 'ADVB'):
                if len(params) < 4 or params[2] != 'sing' or params[3] != 'nomn':
                    continue
                t, gender = params[1].split(' ')
                if gender == 'masc':
                    a[0].add(word)
                elif gender == 'femn':
                    a[1].add(word)
                elif gender == 'neut':
                    a[2].add(word)
    except:
        print(ln, line)
        raise

lenA = [len(i) for i in a]
lenB = [len(i) for i in b]
a = [list(i) for i in a]
b = [list(i) for i in b]

print('Generating code...')
with open('NamesData.g.cs', 'w', encoding='utf-8') as f:
    f.write('''namespace AdventureBot.NameGenerator
{{
    public static class Names
    {{
        public static int[] NounsCounts = new int[] {{ {lenA} }};
        public static int[] AdjectivesCounts = new int[] {{ {lenB} }};
'''.format(
    lenA=', '.join([str(i) for i in lenB]),
    lenB=', '.join([str(i) for i in lenA])
))

    f.write('        public static string[][] Nouns = new string[][] {')
    for group in b:
        f.write('new [] {')
        for word in group:
            f.write(f'"{word}",')
        f.write('},')
    f.write('''};
public static string[][] Adjectives = new string[][] {''')
    for group in a:
        f.write('new [] {')
        for word in group:
            f.write(f'"{word}",')
        f.write('},')
    f.write('};')
    f.write('''
    }
}''')


print('Finishing...')
cnt = 0
for i in range(3):
    aSrc = a[i]
    bSrc = b[i]
    c = lenA[i] * lenB[i]
    print('\n', i, ':', lenA[i], '*', lenB[i], '=', c)
    cnt += c
    for j in range(10):
        aRnd = random.randint(0, len(aSrc) - 1)
        bRnd = random.randint(0, len(bSrc) - 1)
        print(i, aRnd, bRnd, end=': ')
        print(aSrc[aRnd], bSrc[bRnd])
print('\n', cnt)
