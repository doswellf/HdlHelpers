# HdlHelpers

HdlHelper Nested Module and Class Example

This project is the skeleton for a small meta-generation project that will produce 
Verilog and Vhdl structural multiplexer modules along with testbenches to check them.

Since the nested module structure is operational you can use it as a template for 
your own package and module development. 

To test it, you can use PyCharm Community and open the terminal.
Start python3 in the src directory and 

    import HdlHelper as hh

    print(dir(hh))
    print(dir(hh.TestHelperClass))

    thhc = hh.TestHdlHelperClass(10101010)
    thhc.printnum()

    print(dir(hh.VerilogHelper))

    tvg = VerilogHelper(20202020)
    tvg.print_num()

    print(dir(VhdlHelper))

    tvh = VhdlHelper(30303030)
    tvh.print_num()

This could be installed somewhere with pip or pip -e . to verify that it's portable. 

Most of the value of this project for others is seeing and using the skeleton as a starting point
for their own packages. It took half a day to tinker with the files to get thins in the right places.

There are some good posts but this one is very clear:
<a href ="https://medium.com/@udiyosovzon/things-you-should-know-when-developing-python-package-5fefc1ea3606">Nested Modules</a>

