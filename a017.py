#先解決2 + 3 * 4
#有符號優先的問題
#
p = {'+':1,'-':1,'*':2,'/':2,'%':2}
#建造計算機
def apply_op(val1,val2,op):
    if op == '+': return val1 + val2
    if op == '-': return val1 - val2
    if op == '*': return val1 * val2
    if op == '/': return val1 // val2
    if op == '%': return val1 % val2
    return 0
#建造邏輯
def cl(a):
    a = a.split()
    nums =[]
    ops = []
    for token in a:
        if token.isdigit():
            nums.append(int(token))
        elif token =='(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] !='(':
                op = ops.pop()
                val2 = nums.pop()
                val1 = nums.pop()
                nums.append(apply_op(val1,val2,op))
            ops.pop()
        else:
            while ops and ops[-1] != '(' and p[ops[-1]] >= p[token]:
                op = ops.pop()
                val2 = nums.pop()
                val1 = nums.pop()
                nums.append(apply_op(val1, val2, op))
            ops.append(token)
    while ops:
        op = ops.pop()
        val2 = nums.pop()
        val1 = nums.pop()
        nums.append(apply_op(val1,val2,op))
    return nums[0]

while True:
    try:
        line = input()
        print(cl(line))
    except EOFError:
        break
