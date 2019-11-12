import sys # DO NOT EDIT THIS

'''
This function should return the binary representation of an integer.
Note that the digits in the string you return must be in the corect 
order, e.g. convert(6) must return '110'
'''
def convert(num):
    binary = ''
    num = int(num)
    while num > 0:
        ok = num % 2
        binary += str(ok)
        num = int(num / 2)
    binary = binary[::-1]
    return binary
        

    
'''
This function should check if the 'target' string is less than 'length' 
characters long.
If this is the case, 'pad_char' should be prepended to 'target' until the
string is exactly 'length' characters long.
If this is not the case, 'target' should be returned without modification.
For example, pad('111', 3, '0') should return '111', and pad('rdvark', 8, 'a')
should return 'aardvark'.
'''
def pad(target, length, pad_char='0'):
    padded = ''
    line = list(target)

    while len(target)-1 < length:
        line.insert(0, pad_char)

    return line


'''
This function should split an assembly language instruction into its opcode 
and operands, and return a tuple (opcode, [operand1, operand2, ...])
For example, split_instruction('ADDI r1, r9, 17') should return
('ADDI', ['r1', 'r9', '17']).  Note that all operands are still 
in string form, i.e. that '17' is not converted to an integer.
'''
def split_instruction(assembly_instr):
    a = assembly_instr
    a = a.split()
    for i in range(len(a)):
        a[i] = a[i].replace(",", "")
    list = []
    for i in range(1,len(a)):
        list.append(a[i])
    return (a[0], list)
    
        
    
    

    

'''
This function should convert an assembly language instruction to a binary 
string as described in the instructions for this lab, and return this string. 
Hint: You will want to use your convert(), pad(), and split_instruction() 
functions here
'''
def assemble(assembly_instr):
    # This is the table of opcodes for each of the assembly instructions
    # Do not modify this!
    opcodes = {'ADDU': 33, 'ADD': 32, 'ADDIU': 9, 'ADDI': 8, 'AND': 36,
               'SW': 43, 'LW': 35, 'LH': 33, 'SLL': 0, 'SUBU': 35, 'SH': 41,
               'MULTU': 25, 'MFLO': 18, 'NOP': 0, 'SRA': 3, 'LUI': 15, 
               'ANDI': 12, 'BEQ': 4, 'JR': 8, 'OR': 37}
    
    # Use the split_instructions function to break up assembly_instr
    inst = split_instruction(assembly_instr)
    
    # Find the [opcode] in the above dict, convert() it to binary, and then pad() it. 
    
    op = pad(convert(opcodes.get(inst[0])), 6)
    # Loop through your operands and remove the r's. After that, convert() to binary and pad() with zeroes.
    # Remember you can print variables and lists out if you get confused!
    for i in range(len(inst[1])):
        inst[1][i] = inst[1][i].replace("r", '')

    
        
    
    
    # Put together your results - a padded, binary "operation" followed by the padded, binary "operands".
    # Refer to unit tests and instructions to get an exact idea of what you need to return.
    full = ''
    full += op
    
    for i in range(len(inst[1])):
        full += pad(convert(inst[1][i]), 5)
        
    return full


if __name__ == '__main__':
    # file_name is the name of the Super Mario 64 assembly input file, passed in via the first command line argument
    if len(sys.argv) < 2:
        raise Exception('you should have used one command line argument, i.e, python3 main.py argument')
    
    
    # Start out by reading in the assembly file
    r = open(sys.argv[1], 'r')
    w = open('my_out.bin', 'w')
    # Then iterate over each line and convert from assembly to machine code
    print(pad("1001", 5))
    
    

    
    # Finally, write your assembled machine code to a file called my_out.bin
    # One line of assembly input should correspond to one line of machine code output
