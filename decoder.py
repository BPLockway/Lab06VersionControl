def decode(password):
    decoded = ''
    for i in range(8):
        x = int(password[i])
        x = x - 3
        x = str(x)
        decoded = decoded + x
    return decoded