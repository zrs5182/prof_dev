class Problem(object):
    """ Problems from the book """
    def __init__(self, prblm_num, prblm_title,  prblm_dscrptn, sltn, dscssn, code):
        self.prblm_num = prblm_num
        self.prblm_title = prblm_title
        self.prblm_dscrptn = prblm_dscrptn
        self.slnt = sltn
        self.dscssn = dscssn
        self.code = code

    def __str__(self):
        string = ""
        string = string + "Problem #" +self. prblm_num + ": " + self.prblm_title + "\n"

class Chapter(object):
    """ Chapter Object for organizing code and problems """
    def __init__(self, description, problem_descriptions):
        self.description = description
        self.problem_descriptions = problem_descriptions

    def __str__(self):
        string = ""

        # Print out Chapter Description
        string = string + "---------- " + self.description + " ----------"+ '\n'

        # Print out Problem Descriptions
        for prob in self.problem_descriptions:
            string = string + "Problem #" + str( prob ) + "\n"
            string = string + "\t" + self.problem_descriptions[prob] + "\n"
        return string

class Notes(object):
    """ Collection of notes over chapters """
    def __init__(self, chapters):
        self.chapters = chapters

    def __str__(self):
        string = ""

        # Output all the chapters
        for chptr in self.chapters:
            string = string + str(chptr) + '\n'

        return string

