# class Student:
#     def __init__(self, new_gender, new_major, new_id):
#         self.gender = new_gender
#         self.major = new_major
#         self.id = new_id
#
#     def set_gender(self, new_gender):
#         if new_gender == 'M' or new_gender == 'F'
#             self.gender = new_gender
#         else:
#             print('======請傳入"M"或"F"======')
#
#     def join_class(self):
#         pass
#
#     def quit_class(self):
#         pass
#
# StudentA = Student('M', '工管系', 'B10621124')
# print(StudentA.gender)
class Pokemon:

    def __init__(self, new_name, new_weight, new_height, new_food, cp_value):
        self.name = new_name
        self.weight = new_weight
        self.height = new_height
        self.weight = new_food

    def get_eat(self):
        print("The pokemon is eating {food}")

class Pikachu(Pokemon):