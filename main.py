
class Puzzle:

    def __init__(self,image_path,answer):
        
        self.image_path  = image_path
        self.answer = answer

    def try_to_answer(self,trial_answer):

        if self.answer == trial_answer:
            print("Answer Correct!")

        else:
            print("Sorry wrong answer, try again")


class Room:

    def __init__(self,puzzle_list):
        
        self.puzzle_list = puzzle_list
        

my_puzzle = Puzzle('puzzle.jpg',42)

my_puzzle.try_to_answer(42)


my_puzzle_list = [my_puzzle]

room = Room(my_puzzle_list)

# my_list = ['red','blue','green']
# list2 = my_list.copy()
# list2.append('yellow')
# print('my_list: ' + str(my_list))
# print('List2: ' + str(list2))