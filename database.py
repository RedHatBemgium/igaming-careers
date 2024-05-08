from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://career_admin:wYardS5xYaKex5bZ@sql708.your-server.de/careers?charset=utf8mb4")

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []    
    for row in result.all():
      jobs.append(row._asdict())
    return jobs