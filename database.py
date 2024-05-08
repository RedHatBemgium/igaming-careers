from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://career_admin:wYardS5xYaKex5bZ@sql708.your-server.de/careers?charset=utf8mb4")

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())