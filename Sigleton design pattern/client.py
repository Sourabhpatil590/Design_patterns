from singleton_class import singleton

if __name__ == '__main__':
    # a = singleton('sourabh')
    b = singleton.getInstance()
    print(b)
    # c = singleton()
    d = singleton.getInstance()
    print(d)
    # c = singleton()
  