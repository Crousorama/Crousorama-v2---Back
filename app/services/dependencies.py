from fastapi import Header, HTTPException


async def get_token_header(x_goog_authenticated_user_email: str = Header(...)):
    if not x_goog_authenticated_user_email:
        raise HTTPException(status_code=400, detail="Missing Google header")
