# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class VerilogHelper:

    def __init__(self,num):
        self.vex = num

    def print_num(self):
        print(f'From VerilogHelper: The number hhx is {self.vex}\n')

    def print_hi(self,name):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name} From VerilogHelper.print_hi\n')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Main Call From VerilogHelper\n')
    mvh = VerilogHelper(707070707)
    mvh.print_num()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
