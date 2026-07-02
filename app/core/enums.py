from enum import Enum

class InterviewStatus(str, Enum):
    CREATED = "CREATED"
    PARSING = "PARSING"
    READY = "READY"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class InterviewDifficulty(str, Enum):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"