"""
Usage:
correlate [-h] [-s SECTION]

Options:
    -h, --help                      Display this text
    -s SECTION, --section SECTION   Section from which to draw questions [default: None]
"""

# qual_picker - choose a random qualification exam question not already listed in completed_questions.txt

def check_finished(section,donequestions,maxqs):
    done = np.array(donequestions)
    match = done[:,0]==section
    questions = done[:,1][match]
    questions.sort()
    return list(questions) == range(1,maxqs)

def choose_section(section='None'):
    if section=='None' or isinstance(section,int):
        section = np.random.randint(1,5+1)
        if not check_finished(section,donequestions,maxqs[section]):
            return section
        elif check_finished(section,donequestions,maxqs[section]):
            return choose_section(section='None')
    elif section!='None' and isinstance(section,str):
        section = int(section)
        if not check_finished(section,donequestions,maxqs[section]):
            return section
        elif check_finished(section,donequestions,maxqs[section]):
            warn('That section is finished, choosing a new one.')
            return choose_section(section='None')

import docopt
import numpy as np
from warnings import warn

# read in documentation
arguments = docopt.docopt(__doc__)

section = arguments['--section']

maxqs = {1:20,2:19,3:19,4:22,5:24}

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
    section = choose_section(section=section)

    # find a random question from the appropriate section
    if section == 1:
        question = np.random.randint(1,maxqs[section])
        if (section,question) not in donequestions:
            print 'Do question {0} from the cosmology section'.format(question)
            found = True

    if section == 2:
        question = np.random.randint(1,maxqs[section])
        if (section,question) not in donequestions:
            print 'Do question {0} from the extragalactic astronomy section'.format(question)
            found = True

    if section == 3:
        question = np.random.randint(1,maxqs[section])
        if (section,question) not in donequestions:
            print 'Do question {0} from the galactic astronomy section'.format(question)
            found = True

    if section == 4:
        question = np.random.randint(1,maxqs[section])
        if (section,question) not in donequestions:
            print 'Do question {0} from the stars and planets section'.format(question)
            found = True

    if section == 5:
        question = np.random.randint(1,maxqs[section])
        if (section,question) not in donequestions:
            print 'Do question {0} from the math and general physics section'.format(question)
            found = True

# update completed_questions with the newly selected question
with open("completed_questions.txt","a") as donefile:
    donefile.write('{0} {1}\n'.format(section,question))