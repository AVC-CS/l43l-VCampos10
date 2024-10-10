def main():
    
    numbers = [0] * 5
    total = 0
    for i in range(5):
        numbers[i] = int(input('Enter a value: '))
    print(numbers)
    #total = sum(numbers)
    for v in numbers:
        total += v  
    
    
    print(total)
    
    return total, numbers


if __name__ == '__main__':
    main()
