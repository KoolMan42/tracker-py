from fastapi import APIRouter

from services.issue_service import IssueService

issue_controller = APIRouter()
issue_service = IssueService()

@issue_controller.get("/issue")
async def create_issue():
    return {"foo": "bar"}
