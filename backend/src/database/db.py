from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime,timedelta
from . import models

def get_challenge_quota(session: Session, user_id:str):
    return (session.execute(select(models.ChallengeQuota)
                            .where(models.ChallengeQuota.user_id == user_id)).scalars().first())


def create_challenge_quota(session:Session, user_id:str):
    db_quota = models.ChallengeQuota(user_id=user_id)
    session.add(db_quota)
    session.commit()
    session.refresh(db_quota)
    return db_quota

def reset_quota_if_needed(session:Session, quota: models.ChallengeQuota):
    now = datetime.now()
    if now - quota.last_reset_date > timedelta(hours=24):
        quota.quota_remaining = 10
        quota.last_reset_date = now
        session.commit()
        session.refresh(quota)
    return quota

def create_challenge(session:Session,
                     difficulty:str,
                     created_by:str,
                     title:str,
                     options:str,
                     correct_answer_id:int,
                     explanation:str):

    db_challenge = models.Challenge(
        difficulty=difficulty,
        created_by=created_by,
        title=title,
        options=options,
        correct_answer_id=correct_answer_id,
        explanation=explanation
    )

    session.add(db_challenge)
    session.commit()
    session.refresh(db_challenge)
    return db_challenge

def get_user_challenges(session:Session,user_id:str):
    return (session.execute(select(models.Challenge)
                            .where(models.Challenge.created_by == user_id)).scalars().all())