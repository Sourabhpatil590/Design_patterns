from Builder_class import Student

if __name__ == '__main__':
    s = Student( gradyear = 2022, yoe = 1)
    print(s.getname())
    print(s.getgradyear())
    print(s.getyoe())

    s.setname("digvijay")
    print(s.getname())
    s.setgradyear(2020)
    print(s.getgradyear())
    s.setyoe(10)
    print(s.getyoe())