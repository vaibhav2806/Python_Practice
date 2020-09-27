# INPUT : ABCDEFGHIJKLMNOPQRSTUVWXYZ
# OUTPUT: ABCD
#         EFGH
#         IJKL
#         MNOP
#         QRST
#         UVWX
#         YZ

import textwrap

string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
my_wrap = textwrap.TextWrapper(width=4)
wrap_list = my_wrap.wrap(text = string)

for line in wrap_list:
    print(line )
