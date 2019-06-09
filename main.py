import sources as sr


def check(n):
    if n == 'subset':
        sr.get_subset()
    elif n == 'encrypt':
        sr.encrypt_by_shift()
    elif n == 'decrypt':
        sr.decrypt_by_shift()
    elif n == 'break':
        return
    else:
        print('Please type a valid value ! Try again.')
        main_()
    msg = input('Any other else?')
    if msg.lower() == 'no':
        print('QAQ Why do you discard me!!')
        return
    else:
        main_()


def main_():
    print("""
        - input 'subset' to get all subset of your set
        - input 'encrypt' to encrypt your message
        - input 'decrypt' to decrypt your message
        - input 'break' to break the program
    """)
    n = input('-->').lower()
    check(n)


print('Hi , what can I help you? =v=" ')
main_()
