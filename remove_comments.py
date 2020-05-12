import io


class Writer:
    def __init__(self):
        self.prev_empty = True
        self.line = ""
        self.out = io.StringIO()

    def write(self, x):
        self.line += x

        if x == '\n':

            if self.line.strip(' \t\n') == '':
                if self.prev_empty:
                    # Ignore this line
                    self.line = ''
                self.prev_empty = True
            else:
                self.prev_empty = False

            self.out.write(self.line)
            self.line = ''

    def get(self):
        return self.out.getvalue()


def remove_comments(code):
    writer = Writer()
    STATE = 0

    for x in code:
        if STATE == 0:
            if x == '/':
                STATE = 1
            else:
                writer.write(x)

        elif STATE == 1:
            if x == '/':
                STATE = 2
            elif x == '*':
                STATE = 3
            else:
                STATE = 0
                writer.write('/')
                writer.write(x)

        elif STATE == 2:
            if x == '\n':
                STATE = 0
                writer.write(x)
            else:
                continue

        elif STATE == 3:
            if x == '*':
                STATE = 4
            else:
                continue

        elif STATE == 4:
            if x == '/':
                STATE = 0
            elif x == '*':
                pass
            else:
                STATE = 3

    writer.write('\n')

    return writer.get()
