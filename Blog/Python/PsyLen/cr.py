import os

def crawling():
    print("done")
    
def tagging():
    lst = os.listdir('data')
    fnlst = [fn for fn in lst if '.txt' in fn]
    for fn in fnlst:
        analize(fn)
        
    print('done')
        
def analize(fn):
    src_fn = 'data/%s' % fn
    dst_fn = 'tags/%s' % fn
    analize_tag(src_fn, dst_fn)
    
def copy_to_tag(src_fn, dst_fn):
    f = open(src_fn)
    w = open(dst_fn, 'w')

    for line in f:
        w.write(line)

    f.close()
    w.close()

def analize_tag(src_fn, dst_fn):
    f = open(src_fn)

    title = f.readline().strip()
    singer = f.readline().strip()
    text = ''
    for line in f:
        text += line + '|'
        
    f.close()
    
    w = open(dst_fn, 'w')
    w.write('title,singer,text\n')
    w.write(title + ',')
    w.write(singer + ',')
    w.write(text + '\n')

    w.close()
