import csv

class colonist:

    def __init__(self, name, age, role, skills):
        name = self.name
        age = self.age
        role = self.role
        skills = self.skills

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_role(self):
        return self.role

    def get_skills(self):
        return self.skills


def add_colonist(current_pawns):
    print('Name, age, primary role, and number of useable skills available to the pawn.')
    name = input('Pawn Name')

    while True:
        try:
            age = int(input('Pawn Age'))
            break
        except ValueError:
            print('Please use strictly non-negative integers.')

    role = input('What is the Pawn\'s primary role?')

    while True:
        try:
            skills = int(input('How many different skills are above the value 10?'))
            if skills < 0:
                skills = int(input('Please choose values of zero or higher.'))

            break
        except ValueError:
            print('Please use strictly integers.')

    pawnGroup = pawn(name, age, role, skills)
    pawn_list.append(pawnGroup)

    return pawn_list


def find_pawn(pawn_list, pawn):
    tag = 0
    for i in pawn_list:
        if i.get_name() == pawn.get_name() or i.get_age() == pawn.get_age() or i.get_role() == pawn.get_role() or i.get_skills() == pawn.get_skills():
            tag = 1
            break

    if tag == 1:
        return True
    else:
        return False


def write(pawn_list):

    while True:
        try:
            file = input('Please enter file name: ')
            break
        except IOError:
            print('File not found.')

    f = open(file, 'a')

    for i in pawn_list:
        pawn = (f'{i.get_name()} {str(i.get_age())} {i.get_role()} {str(i.get_skills())} \n')
        f.write(pawn)
    f.close()


def read():
    while True:
        try:
            file = input('Please enter file name: ')
            f = open(file, 'r')
            break
        except IOError:
            print('File not found.')

    print(f.read())


if __name__ == '__main__':

    pawn_list = []

    while True:
        try:
            x = int(input('NUmber of Pawns in Colony'))
            break
        except ValueError:
            print("Value must be an integer.")

    for _ in range(x):
        pawn_list = add_colonist(pawn_list)

    print("Search for a colonist with a specific value:")
    search_list = []
    add_colonist(search_list)
    if find_pawn(pawn_list, search_list[0]):
        print('A pawn exists with this feature.')
    else:
        print('No pawns currently exist with this feature.')

    write_file(pawn_list)

    read_file()