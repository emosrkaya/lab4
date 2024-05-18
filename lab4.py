def main():
    nums = [5, 3, -2, 8, -10, 7, 1, 2]
    
    with open("input.txt", "w") as f:
        for num in nums:
            f.write(str(num) + "\n")

    elements_before_positive = []
    total_product = 1

    with open("input.txt", "r") as f:
        for line in f:
            num = int(line.strip())
            if num > 0:
                break
            elements_before_positive.append(num)
            total_product *= num

    with open("output.txt", "w") as f:
        for num in elements_before_positive:
            f.write(str(num) + "\n")

    print("Əlavə elementlərin hasil:", total_product)

if __name__ == "__main__":
    main()
