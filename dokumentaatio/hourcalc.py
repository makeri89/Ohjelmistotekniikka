import re


def find_hours():
    total = 0
    with open('dokumentaatio/tyoaikakirjanpito.md', 'r') as file:
        for row in file:
            if 'Yht.' in row:
                continue
            hours = re.search('\dh', row)
            if hours:
                total += int(hours[0][0])
    return total


if __name__ == '__main__':
    print('Total hours:')
    print(find_hours())
