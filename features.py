from pydriller import RepositoryMining, GitRepository
import datetime
from getCommitsLinux import getLinuxCommits
from getFeaturesLinux import getFeatures
import re

pathLinux = '../../journal/repositories/linux'
pathAxtls = '../../journal/repositories/axtls'
pathUclibc = '../../journal/repositories/uClibc'
# listaCommits = getLinuxCommits()
# features = getFeatures()

def getSPLFeatures():
    features = []
    
    for commit in RepositoryMining(pathLinux,only_commits=listaCommits, only_modifications_with_file_types=['kconfig']).traverse_commits():
    #for commit in RepositoryMining(listaCommits, only_modifications_with_file_types=['kconfig']).traverse_commits():
        for modification in commit.modifications:
            if('kconfig' in modification.filename.lower() and modification.change_type.value == 5):
                currentSourceCode = modification.source_code.replace('\t','').strip().split('\n')
                for line in currentSourceCode:
                    res = re.match(r'^config \S+', line)
                    if((res != None) and not(line.split()[1] in features)):
                        features.append(line.split()[1])
                        print(line)
    return features

def getLinuxF():
    featuresL = []
    featLinux = open('featuresLinux.csv', 'r')

    for f in featLinux:
        print(f)
        featuresL.append(f)
    
    return featuresL

