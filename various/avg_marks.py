# average marks
if __name__ == "__main__":
    N = int(input().strip())
    classis = {}
    for i in range(N):
        line = input().strip()
        name, marks = line.split(" ")[0], list(map(float, line.split(" " )[1:]))
        classis[name] = marks
    average = input().strip()

    print("{:.2f}".format(sum(classis[average])/len(classis[average])))