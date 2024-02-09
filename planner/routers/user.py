from fastapi import APIRouter, HTTPException, status
from planner.models.user import User, UserSignIn

user_router = APIRouter(tags=["User"])

# user 임시 저장소
users = {}

# 회원가입
@user_router.post("/signup")
async def singup(user: User) -> dict:
    # users list에 user.email이 있는지 체크
    if user.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="존재하지 않는 유저입니다."
        )
    users[user.email] = user
    return {
        "message" : "회원가입 완료"
    }

# 로그인
@user_router.post("/signin")
async def signin(user: UserSignIn) -> dict:
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="아이디 또는 비밀번호를 확인해주세요."
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="아이디 또는 비밀번호를 확인해주세요."
        )
    
    return {
        "message" : "로그인 성공"
    }