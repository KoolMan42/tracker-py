from sqlmodel import Session

from models.issue import Issue


class IssueService:

    def __init__(self, data_session: Session):
        self.data_session = data_session

    def create_issue(self, issue: Issue) -> Issue:
        with self.data_session as session:
            session.add(issue)
            return issue
