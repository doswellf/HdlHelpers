
class TestHdlHelperClass:

    def __init__(self,num):
        self.hhx = num

    def print_num(self):
        print(f'From TestHdlHelperClass: The number hhx is {self.hhx}\n')

    def print_hi(self,name):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name} From TestHdlHelperClass.print_hi\n')  # Press Ctrl+F8 to toggle the breakpoint.

    __print_hi = print_hi

if __name__ == '__main__':
    print('Main Call From VerilogHelper\n')
    mth = TestHdlHelperClass(1010)
    mtn = mth.print_num()
