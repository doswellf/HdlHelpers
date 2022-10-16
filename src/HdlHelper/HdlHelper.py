# This is a sample Python script.
# import VerilogHelper as vlh
# import VhdlHelper as vgh
# from TestHdlHelperClass import TestHdlHelperClass
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class HdlHelper:

    def __init__(self,num):
        self.hhx = num

    def print_num(self):
        print(f'The number hhx is {self.hhx}\n')

    def print_hi(self,name):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name} From HdlHelper.print_hi\n')  # Press Ctrl+F8 to toggle the breakpoint.

    __print_hi = print_hi

if __name__ == '__main__':
    print('Main Call From HdlHelper\n')
    from TestHdlHelperClass import TestHdlHelperClass
    mth = TestHdlHelperClass(1010)
    mtn = mth.print_num()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
