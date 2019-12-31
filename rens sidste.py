file = 'C:\\Users\\itcedaca\\Desktop\\Suggest\\output4 scraped.txt'
terms=[]
with open (file, 'r+') as f:
    for line in f:
        line=line.strip('\n')
        terms.insert(len(terms),line)

file1 = 'C:\\Users\\itcedaca\\Desktop\\Suggest\\variationer_mellemrum.txt'
variations=[]
with open (file1) as fa:
    for line in fa:
        line=line.strip('\n')
        variations.insert(len(terms),line)

lines_seen = set()
renset = 'C:\\Users\\itcedaca\\Desktop\\Suggest\\renset.txt'
with open (renset, 'w+') as newfile:
    for term in terms:
        for variant in variations:
            if term not in lines_seen:
                if not term.endswith(variant):
                    continue
                else:
                    newfile.write(term+"\n")
                    lines_seen.add(term)
newfile.close()
