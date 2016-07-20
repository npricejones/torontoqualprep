"""
Usage:
correlate [-h] [-s SECTION]

Options:
    -h, --help                      Display this text
    -s SECTION, --section SECTION   Section from which to draw questions [default: None]
"""

# qual_picker - choose a random qualification exam question not already listed in completed_questions.txt

import docopt
import numpy as np

# read in documentation
arguments = docopt.docopt(__doc__)

section = arguments['--section']

# read in previous questions
donequestions = np.loadtxt("completed_questions.txt",delimiter=' ',dtype=int)
sizecheck = donequestions.size
# make paired tuples with section number and questions
if sizecheck > 2:
    donequestions = zip(donequestions[:,0],donequestions[:,1])
elif sizecheck == 2:
    donequestions = [(donequestions[0],donequestions[1])]


# Boolean to check if a question not previously done was found
found=False

while not found:
    # if no section given, randomly select it
    if section=='None':
        section = np.random.randint(1,5+1)
    if section!='None':
        section = int(section)

    # find a random question from the appropriate section
    if section == 1:
        question = np.random.randint(1,20)
        if (section,question) not in donequestions:
            print 'Do question {0} from the cosmology section'.format(question)
            found = True

    if section == 2:
        question = np.random.randint(1,19)
        if (section,question) not in donequestions:
            print 'Do question {0} from the extragalactic astronomy section'.format(question)
            found = True

    if section == 3:
        question = np.random.randint(1,19)
        if (section,question) not in donequestions:
            print 'Do question {0} from the galactic astronomy section'.format(question)
            found = True

    if section == 4:
        question = np.random.randint(1,22)
        if (section,question) not in donequestions:
            print 'Do question {0} from the stars and planets section'.format(question)
            found = True

    if section == 5:
        question = np.random.randint(1,24)
        if (section,question) not in donequestions:
            print 'Do question {0} from the math and general physics section'.format(question)
            found = True

# update completed_questions with the newly selected question
with open("completed_questions.txt","a") as donefile:
    donefile.write('{0} {1}\n'.format(section,question))