from fastapi import APIRouter, Depends, Form
from typing import Annotated
from auth import auth
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
from gpt import client as gpt_client
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

