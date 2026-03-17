from sqlmodel import Session, select
from models.birdspotting import Birdspotting, BirdspottingCreate
from models.birds import Bird


class BirdspottingRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(Birdspotting, Bird).join(Bird)
        items = self.session.exec(statement).all()

        result = []
        for observation, bird in items:
            observation.bird = bird
            result.append(observation)

        return result

    def get_one(self, id: int):
        statement = select(Birdspotting, Bird).join(Bird).where(Birdspotting.id == id)
        item = self.session.exec(statement).first()

        if item is None:
            return None

        observation, bird = item
        observation.bird = bird

        return observation

    def insert(self, payload: BirdspottingCreate):
        bird = self.session.get(Bird, payload.bird_id)

        if bird is None:
            raise ValueError("Bird does not exist")

        item = Birdspotting.model_validate(payload)
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)

        return item