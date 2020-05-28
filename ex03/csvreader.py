class CsvReader:

    def __init__(self, filename=None, sep=',', hd=False, sk_top=0, sk_bot=0):
        self.filename = filename
        self.sep = sep
        self.isHeader = hd
        self.skip_top = sk_top
        self.skip_bottom = sk_bot
        self.header = []
        self.data = []

    def __enter__(self):
        try:
            self.fd = open(self.filename, 'r+')
        except (FileExistsError, FileNotFoundError):
            return None
        for i in range(0, self.skip_top):
            self.fd.readline()
        if self.isHeader:
            line = self.fd.readline().replace('\n', '')
            self.header = line.split(self.sep)
            lines = self.fd.readlines()
            for i in range(0, len(lines) - self.skip_bottom):
                lines[i] = lines[i].replace('\n', '')
                lines[i] = lines[i].split(self.sep)
                tmp_dict = {}
                for j in range(0, len(self.header)):
                    tmp_dict[self.header[j]] = lines[i][j]
                self.data.append(tmp_dict)
        else:
            lines = self.fd.readlines()
            for i in range(0, len(lines) - self.skip_bottom):
                lines[i] = lines[i].replace('\n', '')
                self.data.append(lines[i].split(self.sep))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.fd.close()
        except AttributeError:
            return self
        return self

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header


if __name__ == '__main__':
    with CsvReader('dict.csv', ', ', True, 1, 0) as file:
        if not file:
            print('File is corrupted')
        else:
            data = file.getdata()
            header = file.getheader()

    print(data)
