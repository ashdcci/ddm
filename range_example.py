class range_examp:
    def __init__(self, end ,step = 1):
        self.current = 0
        self.end = end
        self.step = step
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()
        else:
            return_val = self.current
            self.current += self.step
            return return_val        

def range_gen(end):
    current = 0
    while current < end:
        yield current
        current += 1

def main():
    i = range_examp(5)
    i.__next__()
    i.__next__()
    for j in i:
        print(j)
    print(dir(range_examp))
    print('>>>>>>>>')
    for i in range_gen(5):
        print(i)
    print(dir(range_gen(5)))
    print('<<<<<<<<')
    

if __name__ == '__main__':
    main()