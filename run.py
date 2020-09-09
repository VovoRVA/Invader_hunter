from sys import argv


class InvaderRecognizer:

    def __init__(self, accuracy: float):
        self.accuracy = accuracy

    @staticmethod
    def read_file(filename: str) -> list:
        try:
            with open(filename, 'r') as file:
                return [list(line.strip()) for line in file]
        except FileNotFoundError:
            print('File not found')
            exit()

    @staticmethod
    def calc_matches(invader, radar, i_r, j_r, inv_r, inv_c, radar_r, radar_c) -> int:
        matches = 0                # invader's symbol that matches the radar's one
        for i in range(inv_r):     # iterate invader's string
            # checking if we are not out of list's boundary and skipping negative edge coordinates
            if i_r + i >= radar_r or i_r + i < 0:
                continue
            for j in range(inv_c): # iterate invader's column
                if j_r + j < 0:    # skipping negative edge coordinates
                    continue
                # checking if we are not out of boundary and symbols are matching
                if j_r + j < radar_c and invader[i][j] == radar[i + i_r][j + j_r]:
                    matches += 1
        return matches

    def get_matches(self, invader: list, radar: list) -> list:
        invader_coord = []

        inv_r = len(invader)     # invader number of rows (length)
        inv_c = len(invader[0])  # invader number of columns (width)
        radar_r = len(radar)     # radar number of rows (length)
        radar_c = len(radar[0])  # radar number of columns (width)

        upper_edge = 1 - inv_r
        left_edge = 1 - inv_c

        for i_r in range(upper_edge, radar_r):     # iterate radar's string
            for j_r in range(left_edge, radar_c):  # iterate radar's column
                # calculating matches and checking matches' rate of success
                match_rate = self.calc_matches(invader, radar, i_r, j_r, inv_r, inv_c, radar_r, radar_c) / (
                            inv_r * inv_c)
                if match_rate >= self.accuracy:
                    invader_coord.append(([i_r, j_r], match_rate))
        return invader_coord

    @staticmethod
    def print_nicely(result: list, invader_file: str = ''):
        print(invader_file)
        for i, j in result:
            print("invader's initial coordinates: ", i, '\t', 'match_rate: ', round(j, 4))


try:
    accuracy = argv[1]
except IndexError:
    accuracy = 0.8
try:
    invader_file = argv[2]
except IndexError:
    invader_file = 'invader_1.txt'
try:
    radar_file = argv[2]
except IndexError:
    radar_file = 'radar_sample.txt'

if __name__ == '__main__':
    """
    accuracy arg can be number from 0 to 1 inclusive (e.g. 0.8 means 80% matches of invader)
    radar_file arg should be file's name that contains radar's ASCII sample
    invader_file arg should be file's name that contains invader's ASCII pattern
    """
    # create object
    inv_rec = InvaderRecognizer(accuracy)
    # create radar
    radar = InvaderRecognizer.read_file(radar_file)
    # get first invader's matches
    invader_first = InvaderRecognizer.read_file(invader_file)
    # get second invader's matches
    invader_second = InvaderRecognizer.read_file('invader_2.txt')
    # print nicely matches
    InvaderRecognizer.print_nicely(inv_rec.get_matches(invader_first, radar), invader_file)
    InvaderRecognizer.print_nicely(inv_rec.get_matches(invader_second, radar), 'invader_2.txt')
