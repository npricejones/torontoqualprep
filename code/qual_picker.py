import numpy as np


donequestions = np.loadtxt("completed_questions.txt",delimiter='\t',dtype=int)
if donequestions.size > 2:
    donequestions = zip(donequestions[:,0],donequestions[:,1])
if donequestions.size == 2:
    donequestions = [(donequestions[0],donequestions[1])]


found=False

while not found:
    section = np.random.randint(1,5+1)

    if section == 1:
        question = np.random.randint(1,19+1)
        if (section,question) not in donequestions:
            print 'Do question {0} from the cosmology section'.format(question)
            found = True

    if section == 2:
        question = np.random.randint(1,18+1)
        if (section,question) not in donequestions:
            print 'Do question {0} from the extragalactic astronomy section'.format(question)
            found = True

    if section == 3:
        question = np.random.randint(1,18+1)
        if (section,question) not in donequestions:
            print 'Do question {0} from the galactic astronomy section'.format(question)
            found = True

    if section == 4:
        question = np.random.randint(1,21+1)
        if (section,question) not in donequestions:
            print 'Do question {0} from the stars and planets section'.format(question)
            found = True

    if section == 5:
        question = np.random.randint(1,23+1)
        if (section,question) not in donequestions:
            print 'Do question {0} from the math and general physics section'.format(question)
            found = True

with open("completed_questions.txt","wb") as donefile:
    donefile.write('{0}\t{1}\n'.format(section,question))