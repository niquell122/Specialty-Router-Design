from fastapi import APIRouter, Depends, Form
from typing import Annotated
from auth import auth
from qdrantgpt import get_question_context

router = APIRouter()


@router.post('/question/context')
def quest_context(
    current_user: Annotated[str, Depends(auth)],
    question: Annotated[str, Form()],
    ):
    username = current_user["username"]

    result = get_question_context(username, question)

    return result

