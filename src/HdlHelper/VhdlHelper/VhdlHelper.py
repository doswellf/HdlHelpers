# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class VhdlHelper:

    def __init__(self,num):
        self.vhx = num

    def print_num(self):
        print(f'The number vhx = {self.vhx}\n')

    def print_hi(self, name):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name} From VhdlHelper.print_hi\n')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Main Call From VhdlHelper\n')
    mvh = VhdlHelper(20202020)
    mvh.print_num()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
