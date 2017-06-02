class Helper:
    def __init__(self):
        pass

    @staticmethod
    def formatSize(fsize):
        if 1024 < fsize < 1024 * 1000:
            fsize = str(int(fsize / 1024)) + "K"
        elif 1024 * 1000 < fsize < 1024 * 1000 * 1000:
            fsize = str(int(fsize / 1024 / 1000)) + "M"
        elif 1024 * 1000 * 1000 < fsize < 1024 * 1000 * 1000 * 1000:
            fsize = str(int(fsize / 1024 / 1000 / 1000)) + "G"
        elif 1024 * 1000 * 1000 < fsize < 1024 * 1000 * 1000 * 1000 * 1000:
            fsize = str(int(fsize / 1024 / 1000 / 1000 / 1000)) + "T"
        elif 1024 * 1000 * 1000 < fsize < 1024 * 1000 * 1000 * 1000 * 1000 * 1000:
            fsize = str(int(fsize / 1024 / 1000 / 1000 / 1000 / 1000)) + "P"
        else:
            fsize = str(fsize) + "B"
        return fsize