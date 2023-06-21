
START = "s"
PRED = "p"
PRED_OPEN = "po"
PRED_CLOSED = "pc"
TAG = "t"
TAG_OPEN = "to"
TAG_CLOSED = "tc"
UN_OPERATOR = "uop"
BIN_OPERATOR = "bop"
AFTER_OPERATOR = "aop"
GRP = "g"

def validate(s: str):
    expr_on_left = False # TODO
    grp_stack = []
    state = START
    for c in s:
        if state == START:
            if c == "[":
                state = PRED_OPEN
            elif c == "{":
                state = TAG_OPEN
            elif c == "(":
                state = GRP
                grp_stack.append(c)
            elif c in {"}", "]", ")"}:
                return False
            elif c.isprintable():
                state = UN_OPERATOR
            elif not c.isspace():
                return False
        elif state in {PRED_OPEN, TAG_OPEN}:
            if c.isprintable():
                expr_on_left = True
                state = PRED if state == PRED_OPEN else TAG
            else:
                return False
        elif state in {PRED, TAG}:
            if c == "]" and state == PRED:
                state = PRED_CLOSED
            elif c == "}" and state == TAG:
                state = TAG_CLOSED
            elif not c.isprintable():
                return False
        elif state in {PRED_CLOSED, TAG_CLOSED}:
            if c == ")":
                if not grp_stack or grp_stack[-1] != "(":
                    return False
                else:
                    grp_stack.pop()
            elif c in {"}", "]"}:
                return False
            elif c.isprintable():
                state = BIN_OPERATOR
            elif not c.isspace():
                return False
        elif state in {UN_OPERATOR, BIN_OPERATOR}:
            if c == "[":
                state = PRED_OPEN
            elif c == "{":
                state = TAG_OPEN
            elif c == "(":
                state = GRP
                grp_stack.append(c)
            elif c in {"}", "]", ")"}:
                return False
            elif c.isprintable():
                pass
            elif c.isspace():
                state = AFTER_OPERATOR
            else:
                return False
        elif state == AFTER_OPERATOR:
            if c == "[":
                state = PRED_OPEN
            elif c == "{":
                state = TAG_OPEN
            elif c == "(":
                state = GRP
                grp_stack.append(c)
            elif c in {"}", "]", ")"}:
                return False
            elif not c.isspace():
                return False
        elif state == GRP:
            if c == "[":
                state = PRED_OPEN
            elif c == "{":
                state = TAG_OPEN
            elif c == "(":
                grp_stack.append(c)
            elif c == ")":
                return False
            elif c in {"}", "]"}:
                return False
            elif c.isprintable():
                state = BIN_OPERATOR if expr_on_left else UN_OPERATOR
            elif not c.isspace():
                return False
    return state in {TAG_CLOSED, PRED_CLOSED}


print(validate("{tag}contains} in[predicate]"))

# n = int(input())
# i = []

# for _ in range(n):
#     i.append(validate(input()))

# for r in i:
#     print("valid" if r else "invalid")