n = int(input())

def recurse(list, total):
    if sum(list) == total:
        print(str(total) + "=" + "+".join(list))
    else:
        for i in range(total - sum(list)):
            recurse(list.append(i), total)
            # fix this bro it's just recursion