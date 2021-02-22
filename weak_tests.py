import sys
from dll import DLL

def main():

    orig_stdout = sys.stdout
    fout = open('out.txt', 'w+')
    sys.stdout = fout


    print("\n\nTESTING THE BASIC STUFF\n")

    dll = DLL()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("D")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("E")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("1")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("2")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("3")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("4")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("VALUE")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(8)
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(2)
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_prev()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(-1)
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(18)
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(0)
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.remove()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))


    print("\n\nTESTING MORE COMPLEX STUFF\n")


    dll = DLL()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B1")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B2")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.partition(dll.get_first_node(), dll.get_last_node())
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    result = dll.get_first_node()
    if result != None:
        result = result.data
    print("first node: ", str(result))
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B3")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    result = dll.get_last_node()
    if result != None:
        result = result.data
    print("last node: ", str(result))
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(0)
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B5")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.move_to_pos(4)
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.partition(dll.get_first_node(), dll.get_last_node())
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.sort()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))

    dll.clear()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    

    dll.insert("B")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("D")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("G")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("T")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("A")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("C")
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    dll.insert("B")
    print(str(dll) + "   -   current value: " + str(dll.position) + "   -   size: " + str(len(dll)))
    dll.move_to_next()
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.remove()
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.remove()
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.remove()
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.remove()
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # result = dll.get_first_node()
    # if result != None:
    #     result = result.data
    # print("first node: ", str(result))
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.move_to_prev()
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.move_to_prev()
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.remove()
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # result = dll.get_last_node()
    # if result != None:
    #     result = result.data
    # print("last node: ", str(result))
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.clear()
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))

    sys.stdout = orig_stdout
    fout.close()


if __name__ == "__main__":
    main()


