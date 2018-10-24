from subprocess import Popen, PIPE

def parse_result(classes, result):
    for line in result.split('\n'):
        path = line.split('*')[0].split(':')[0]
        name = path.split('/')[-1]
        
        if ".java" in name:
            classes[name] = path

def pretty_print(dic):
    for key in dic:
        print('{} : {}'.format(key, dic[key]))

def jmlable():
    classes = {}
    output1 = Popen(['grep', '-rn', '-e', '@param'], stdout=PIPE).communicate()[0].decode('utf-8')
    output2 = Popen(['grep', '-rn', '-e', '@return'], stdout=PIPE).communicate()[0].decode('utf-8')
    parse_result(classes, output1)
    parse_result(classes, output2)
    return classes
    

if __name__ == '__main__':
    jmlable_classes = jmlable()
    print('\n\n{} classes JMLaveis encontradas: \n'.format(len(jmlable_classes)))
    pretty_print(jmlable_classes)
