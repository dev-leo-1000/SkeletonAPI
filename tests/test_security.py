from passlib.context import CryptContext

ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)

hashed_pwd = get_password_hash("string")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

print(verify_password('string', hashed_password=hashed_pwd))