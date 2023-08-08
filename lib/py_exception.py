# # while True:
# #     try:
# #         x=int(input('Please enter a number: '))
# #         break
# #     except ValueError:
# #         print('Oops! That was no valid number. Try again...')

# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception instance
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,
#                          # but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)



# def bool_return():
#     try:
#         return True
#     finally:
#         return False



# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")

# divide(2, 1)
# divide(2, 0)
# divide("2", "1")


from exceptiongroup import ExceptionGroup, catch

def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

try:
    f()
except Exception as e:
    print(f'caught {type(e)}: e')