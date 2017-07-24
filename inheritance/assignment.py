import abc
from datetime import datetime


class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def write(self, input):
        '''writes to the file'''
        return

    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.write(text+'\n')
        fh.close()

class LogFile(WriteFile):

    def write(self, input):
        todays_date = datetime.now()
        line = "{}    {}\n".format(todays_date.strftime('%Y-%m-%d %H:%M'), input)
        self.write_line(line)

class DelimFile(WriteFile):
    def __init__(self, input, delim):
        super(DelimFile, self).__init__(input)
        self.delim = delim

    def write(self, input):
        line = "{}\n".format((self.delim).join(input))
        self.write_line(line)

log = LogFile('log.txt')
c = DelimFile('text.csv',',')

log.write('this is a log message')
log.write('this is another log message')

c.write(['a', 'b','c','d'])
c.write(['1','2']);
