
from sqlalchemy import (
                        create_engine,
                        Column,
                        Integer,
                        String,
                        )
from sqlalchemy.ext.declarative import declarative_base                 # this fn returns a class when called
# from sqlalchemy.sql.schema import PrimaryKeyConstraint
                                                                        # declarative is a higher level system for specifying objects
                                                                        # maps database objects to db tables
from sqlalchemy.orm import sessionmaker                                  # it's the ORM handle to db...writing/reading 
                    
Base = declarative_base()
class Task(Base):                                                   # instances of this class will be py objects tied to specific db rows
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    summary = Column(String)
    description = Column(String)

class TaskStore:
    def __init__(self, engine_spec):
#         self.engine = create_engine("sqlite:///:memory:")               # use the sqlite in-memory db
        self.engine = create_engine(engine_spec)
        Base.metadata.create_all(self.engine)                                  # only creates table if not exist
        self.Session = sessionmaker(bind=self.engine)                   # create a session for each db action fn below
    
    def get_all_tasks(self):
        
        return [ {"id": task.id, "summary": task.summary}
                for task in self.Session().query(Task).all()]
        
    def create_task(self, summary, description):
        session = self.Session()
        task = Task(
                    summary=summary,
                    description=description
                            )
        session.add(task)
        session.commit()
        return task.id
    
    def task_details(self, task_id):
        task = self.Session().query(Task).get(task_id)
            
        return {
                "id": task_id,
                "summary": task.summary,
                "description": task.description}
    
    def clear(self):
        self.tasks.clear()
    def delete_all_tasks(self):
        session = self.Session()
        session.query(Task).delete()
        session.commit( )