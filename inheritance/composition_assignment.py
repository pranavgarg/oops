'''
Using Composition instead of inheritance to help make it more extendible and maintainable
'''

from datetime import datetime


class WriteFile(object):

    def __init__(self, filename, writer):
        self.file = open(filename, 'a')
        self.formatter = writer()

    def write(self,text):
        self.file.write(self.formatter.format(text))
        self.file.write('\n')

    def close(self):
        self.file.close()


class CSVFormatter(object):
    def __init__(self):
        self.delim = ","

    def format(self, this_list):
        new_list = []
        for element in this_list:
            if self.delim in element:
                new_list.append('"{0}"'.format(element))
            else:
                new_list.append(element)
        return self.delim.join(new_list)

class LineFormatter(object):

    def format(self, this_line):
        todays_date = datetime.now()
        return "{0}  {1}".format(todays_date.strftime("%Y-%m-%d %H:%M"), this_line)

a = WriteFile('log.txt', LineFormatter)
a.write('this is a log message')
a.write('this is another log message')
a.close()

c = WriteFile('text.csv', CSVFormatter)
c.write(['a', 'b','c','d'])
c.write(['1','2,']);
c.close()