from pydriller import RepositoryMining, GitRepository
import datetime
import re


#listaCommits = getLinuxCommits()
pathLinux = '../../journal/repositories/linux'
fileLinuxFeatures = open('featuresLinux_teste2.csv', 'w')


featuresLinux = []
for commit in RepositoryMining(pathLinux, only_modifications_with_file_types=['kconfig']).traverse_commits():
    for modification in commit.modifications:
        if('kconfig' in modification.filename.lower() and modification.change_type.value == 5):
            currentSourceCode = modification.source_code.replace('\t','').strip().split('\n')
            for line in currentSourceCode:
                res = re.match(r'^config \S+', line)
                if((res != None) and not(line.split()[1] in featuresLinux)):
                    featuresLinux.append(line.split()[1])
                    fileLinuxFeatures.write('{}\n'.format(line.split()[1]))
                    print(line)


