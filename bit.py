#author: W. Scott Spencer

#The purpose of this Python program is to take user input in the form of binary, hexadecimal,
#and decimal numbers (given the appropriate identifiers of 0x for hex and 0b for binary) and
#to perform any of the following bit operations on them:  AND, OR, XOR, LS, RS, and ANDNOT.
#input is read in the form:  0b1010 XOR 0xF

class Number:
    def __init__(self, v):
        #initialize the object
        self.v = v
    def toString(self):
        #print the number in mulitple formats: decimal, hex, binary
        #we will always pass v as a decimal number so simply convert the appropriate vars to binary and hex
        decimalv = int(self.v)
        binaryv = bin(decimalv)
        hexv = hex(decimalv)
        
        #print the value in the three formats by returning them as strings
        return str(decimalv) + " " + str(hexv) + " " + str(binaryv)

while True:
    print("When entering numbers, you can enter:")
    print("     A normal decimal integer number as big as 2^{64}-1.")
    print("     An integer number in hex up to 16 digits, starting with 0x.")
    print("     An integer number in binary up to 64 digits, starting with 0b.")
    print("Enter a problem: number AND|OR|XOR|LS|RS|ANDNOT number:")

    try:
        inputStr = input()
    except (EOFError):
        exit()
    
    #split input into 3 variables (first number, second number, and operator)
    num1, operation, num2 = inputStr.split(' ', 2)
    
    #determine what format the numbers are in and convert to binary to compute operation
    #is num1 hex?  If so convert to binary
    if num1[:2] == '0x':
        val1 = int(num1, 16)
    #else, is num1 binary? if so, convert to int AFTER changing it from the format 'B101' to '0b101'
    elif num1[:1] == 'B':
        num1 = '0b' + num1[1:]
        val1 = int(num1, 2)
    #else, num1 is decimal? So, we're good
    #if we can't parse num2 as an int, the input is invalid
    else:
        try:
            val1 = int(num1)
        except ValueError:
            print("invalid input")
    #is num2 hex? if so, we're good
    if num2[:2] == '0x':
        val2 = int(num2, 16)
    #else, is num2 binary? if so, convert to int AFTER changing it from the format 'B101' to '0b101'
    elif num2[:1] == 'B':
        num2 = '0b' + num2[1:]
        val2 = int(num2, 2)
    #else, num2 is decimal? So, convert the int version of it to binary
    #if we can't parse num2 as an int, the input is invalid
    else:
        try:
            val2 = int(num2)
        except ValueError:
            print("invalid input")
        
    #create our numberA and numberB Number variables (passing a decimal value)
    numberA = Number(val1)
    numberB = Number(val2)
    
    #determine operator, carry out math on inputs based on operator
    if operation.upper() == 'AND' :
        #perform val1 AND val2 operation to generate bin3 (and therefore numberC)
        val3 = val1 & val2
    elif operation.upper() == 'OR' :
        #perform val1 OR val2 operation to generate bin3 (and therefore numberC)
        val3 = val1 | val2
    elif operation.upper() == 'XOR' :
        #perform val1 XOR val2 operation to generate bin3 (and therefore numberC)
        val3 = val1 ^ val2
    elif operation.upper() == 'LS' :
        #perform val1 LeftShift val2 operation to generate bin3 (and therefore numberC)
        val3 = val1 << val2
    elif operation.upper() == 'RS' :
        #perform val1 RightShift val2 operation to generate bin3 (and therefore numberC)
        val3 = val1 >> val2
    elif operation.upper() == 'ANDNOT' :
        #perform val1 ANDNOT val2 operation to generate bin3 (and therefore numberC)
        #a ANDNOT b is the same as saying a AND (NOT b) so...
        val3 = ~ val2
        val3 = val1 & val3
    else:
        #operation is unknown, tell them about it
        print('unknown operator')
        
    numberC = Number(val3)
    
    # output
    print("\nCompute Result:")
    print("     Operation: ", operation)
    print("     A: ", numberA.toString())
    print("     B: ", numberB.toString())
    print("     C: ", numberC.toString())
