from sqlalchemy.orm import Session
from app.models.user import User
from app.core.auth import hash_password, verify_password, create_acces_token

def create_user(db:Session, name:str, email:str, password:str):
    hashed = hash_password(password)
    user = User(name= name, email = email, password = hashed)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None
    
    if not verify_password(password, user.password):
        return None
    
    token = create_access_token({"sub": user.email})
    return token
    

    