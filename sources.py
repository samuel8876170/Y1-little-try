# input any number or words , then get the subset of the set of input
# e.g. input : 1 2 3 ; output : [] [1] [2] [3] [1,2] [1,3] [2,3] [1,2,3]
def get_subset():
    set_array = []

    def get_setting(arr, set_length, choose):

        data = [0] * choose     #create temporary data of the set

        output_combination(arr, data, 0,set_length - 1, 0, choose)

    def output_combination(arr, data, start, end, index, choose):
        if index == choose:
            print(data)
            return
        m = start
        while m <= end and end - m + 1 >= choose - index:
            data[index] = arr[m]
            output_combination(arr, data, m + 1, end, index + 1, choose)
            m += 1
        return

    # get input~~
    n = int(input("how many element you want to add?"))

    for i in range(n):
        elements = input("->")
        set_array.append(elements)
    set_array.sort()
    print(f'your elements in the set is included: {set_array} .')

    # run for output
    for r in range(n + 1):
        if r == 0:

            print("[]")     #empty set

        elif r == 1:

            for i in range(len(set_array)):
                print(f'[{set_array[i]}]')      #set involved 1 element

        elif r == n:

            print(set_array)    #set involved all elements
        else:

            get_setting(set_array, n, r)

# =================================================== Next Function =================================================
# shifting words in the input by specific number. e.g. input : abc (shift by adding 3) output : def
def shift_word_to_right():
    word_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']                # set of word
    num = input('How many times you want to shift forward?')
    try:
        num = int(num)
    except ValueError:
        print('That is not an integer!')
        return
    msg = input('What is your decrypted message?').lower()
    msg_char = list(''.join(msg))
    output = ''
    for x in range(0, len(msg_char)):
        for y in range(0, len(word_set)):
            if msg_char[x] == word_set[y]:
                output += word_set[(y+num) % 26]        # shift to right and back to 'a' when (y+num) is over 26
    print(output)


def shift_word_to_left():
    word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    num = input('How many times you want to shift back?')
    try:
        num = int(num)
    except ValueError:
        print('That is not an integer!')
        return
    msg = input('What is your encrypted message?').lower()
    msg_char = list(''.join(msg))
    output = ''
    for x in range(0, len(msg_char)):
        for y in range(0, len(word)):
            if msg_char[x] == word[y]:
                output += word[(y - num) % 26]
    print(output)

# =================================================== Next Function =================================================


















