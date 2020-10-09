# Namespace and scope program

def scope_test():
    def do_local():
        # spam here is local variable in do_local
        spam = "spam in do_local"

    def do_nonlocal():
        # nonlocal means spam is local variable in scope_test 
        nonlocal spam
        spam = "spam in scope_test"

    def do_global():
        # global means spam is same everywhere in program
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    
    do_global()
    print("After global assignment:", spam)

    do_nonlocal()
    print("After nonlocal assignment:", spam)

scope_test()
print("In global scope:", spam)