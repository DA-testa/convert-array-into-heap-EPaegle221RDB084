# python3


def build_heap(data):
    swaps = []
    length = len(data)

    for i in range(length//2-1, -1, -1):
        min_root = i
        while True:
            l_node = 2*i+1
            r_node = 2*i+2
            if l_node<= length-1 and data[l_node]< data[min_root]:
                min_root = l_node
            if r_node<= length-1 and data[r_node]< data[min_root]:
                min_root = r_node
            if i!= min_root:
                swaps.append((i, min_root))
                data[i], data[min_root] = data[min_root], data[i]
                i = min_root
            else:
                break

    return swaps

def main():
    input_type = input()

    if "F" in input_type:
        file_name = input()
        if ".a" in file_name:
                return
        if "tests/" not in file_name:
            file_name = "tests/" + file_name
        if "tests/" in file_name:
            with open(file_name) as f:
                    lines = f.readlines()
                    n = int(lines[0])
                    data = list(map(int, lines[1].split()))             
    elif "I" in input_type:
        n = int(input())
        data = list(map(int, input().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
