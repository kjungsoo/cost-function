from cost_function_definition import f, f_prime, f_double_prime


def minimize(f0, f1, f2, guess_initial, epsilon):
    guess = guess_initial
    guess_next = guess
    delta = -f1(guess)/f2(guess)

    fprime = f1(guess)
    fd_prime = f2(guess)

    if fd_prime != 0:
        guess_next = guess - fprime/fd_prime
        while abs(delta) > epsilon:
            guess = guess_next
            fprime = f1(guess)
            fd_prime = f2(guess)

            if fd_prime != 0:
                delta = -fprime/fd_prime
                guess_next = guess + delta

            else:
                print("The second derivative returned 0 when the guess was " + guess + ".")

    else:
        print("The second derivative returned 0 when the guess was " + guess + ".")

    guess = guess_next
    print str(f0(guess_initial)) + " is minimized at " + str(guess)

minimize(f, f_prime, f_double_prime, 0.0, 0.000001)