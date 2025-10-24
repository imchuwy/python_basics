#1h30m https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLTjRvDozrdlxj5wgH4qkvwSOdHLOCx10f

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess != secret_number:
        print('try again!')
    if guess == secret_number:
        print('Winner!')
        break
else:
    print('Loser!')
