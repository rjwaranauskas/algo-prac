# Algorthms 4th edition Exercise 1.3.9
# Write a program that takes from the standard input an expression without left parentheses
# and prints the equivalent infix expression with the parentheses inserted. For example:
#             1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )
# Should return:
#         ( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) ) )

# 1 2 + ()
# * ()
# 3 4 - ()
# * ()
# 5 6 - ()

# pass 1: ( 1 + 2 ) * ( 3 - 4 ) * ( 5 - 6 ) ) )
#                   ^           ^


# --------------
# after first pass: (( 1 + 2 ) * (( 3 - 4 ) * ( 5 - 6 ) ) )
#                             ^                            - 2 left paren's left
# place a ( before the balanced item


# ------ actual test -----
# 1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )
# loop left to right
# operators:
# operands:
# important check is when you find an operator

# operators: +
# operands: 1
# place a ( before the 1

# ( 1 + 2 ) *
# operators: + *
# operands: 1 2
# place a ( before the 1 (again)

# when you find an operator, try to find ) before another operator. If it occurs, add ( to left of the bottom of the stack
#      if you find another operator before the ), pop all out of both stacks and continue




# ( ( 1 + 2 ) * 3 -
# operators:
# operands:

# ( ( 1 + 2 ) * ( 3 - 4
# operators: - *
# operands: 3 4

# ( ( 1 + 2 ) * ( ( 3 - 4 ) *
# operators: -
# operands: 5

# ( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) ) )
# operators:
# operands:


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def peek_bottom(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def print_stack(self):
        for item in self.items:
            print(item)

    def pop_all(self):
        self.items = []

    def write(self):
        output_str = ""
        for item in self.items:
            output_str += item
        return output_str


#             1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )


operands = Stack()
operators = Stack()
single_stack = Stack()
output_stack = Stack()
input_str = "1+2)*3-4)*5-6)))"   # "1+2)*3-4)*5-6)))"
output_str = ""
last_input = ""
def recursive(input_str,output_str, single_stack: Stack, output_stack: Stack):
    idx = len(input_str)-1
    while idx > 0:
    # for idx in range(len(input_str)-1,-1,-1):
        # print(idx,input_str[idx])
        single_stack.push(input_str[idx])
        if input_str[idx] == ")":

            # single_stack.push(input_str[idx])
            if input_str[idx-1].isnumeric():
                if input_str[idx-2] in ["-","+","/","*"]:
                    if input_str[idx-3].isnumeric():
                        print("---found paren to add---")

                        # single_stack.push(input_str[idx])
                        single_stack.push(input_str[idx - 1])
                        single_stack.push(input_str[idx - 2])
                        single_stack.push(input_str[idx - 3])
                        single_stack.push("(")
                        ref_str = input_str[idx]+input_str[idx - 1]+input_str[idx - 2]+input_str[idx - 3]+"("
                        print(f"ref_str is '{ref_str[::-1]}'")
                        output_stack.push(ref_str[::-1])
                        if (input_str[idx-4] in ["-","+","/","*"]) and ref_str[::-1] != "(9*9)":
                            print("found: ",input_str[idx-4])
                            output_stack.push(input_str[idx-4])

                        output_stack.print_stack()
                        print("--- done adding ---")
                        # test = single_stack.write()
                        # # print(test[::-1])
                        # test = test[::-1]
                        # print("output before is:",output_str)
                        # output_str = test + output_str
                        # print("output is now:",output_str)
                        input_str = input_str[:idx-3] + "9" + input_str[idx+1:]
                        print("input now is",input_str)
                        single_stack.pop_all()
                        last_input = recursive(input_str, output_str, single_stack, output_stack)
                        if last_input and len(last_input) == 1:
                            return last_input

                        return input_str
        idx -= 1


last_input = recursive(input_str,output_str,single_stack, output_stack)
print("last input is",last_input)
print("output stack is...")
output_stack.print_stack()
print("popping...")
while not output_stack.isEmpty():
    testa = output_stack.pop()
    if testa[:2] == "(9":
        if output_stack.peek() in ["-","+","/","*"]:
            testa = output_stack.pop()
            print(testa, end="")
        print("(",end="")
        continue
    print(testa,end="")



# for idx,first_pass_letter in enumerate(input_str):
#     if first_pass_letter in ["-","+","/","*"]:
#         operands.push(first_pass_letter)
#         operands.print_stack()
#         print("---")
#         for second_pass_letter in input_str[idx+1::]:
#             if second_pass_letter  == ")":
#                 # add ( before the bottom of the stack
#                 operands.items.insert(0,"(")
#                 operands.print_stack()
#                 print("---")
#                 break
#             elif second_pass_letter in ["-","+","/","*"]:
#                 # pop all stacks and break
#                 operands.items.insert(0,"(")
#                 operands.print_stack()
#                 output_str += operands.write()
#                 print("clearing all stacks...")
#                 operands.pop_all()
#                 operators.pop_all()
#                 print("---")
#                 break
#         # "breaks" go here
#     else:
#         operands.push(first_pass_letter)
#         operands.print_stack()
#         print("---")
#
# # operands.print_stack()
# output_str += operands.write()
# print(output_str)

















