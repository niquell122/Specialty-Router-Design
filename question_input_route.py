from fastapi import APIRouter, Depends, Form
from typing import Annotated
from auth import auth
from qdrant_gpt import get_question_context
from dotenv import dotenv_values

router = APIRouter()

config = dotenv_values(".env")
search_quantity=int(config["SEARCH_QUANTITY"])

@router.post('/question/context')
def quest_context(
    current_user: Annotated[str, Depends(auth)],
    question: Annotated[str, Form()],
    ):
    username = current_user["username"]

    result = get_question_context(username=username, data=question, limit=search_quantity)

    return result

