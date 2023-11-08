import bcrypt


def hash_password(password):
    # gensalt return or generate for me a salt
    return bcrypt.hashpw(bytes(password, encoding='utf-8'), bcrypt.gensalt())


def check_password(entered_password, hashed_password):
    return bcrypt.checkpw(bytes(entered_password, encoding='utf-8'), hashed_password)



