#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    h_list = []
    d_list = dir(hidden_4)
    for i in d_list:
        if i[0] != "_":
            h_list.append(i)
    for n in h_list:
        print("{:s}".format(n))
