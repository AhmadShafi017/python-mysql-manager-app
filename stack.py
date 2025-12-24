
def go_to(page,stack):
    stack.append(page)



def go_back(stack):
    if stack:
        return stack.pop()
    return None
