# A DI is a mechanish in fastAPI uses to allow you to share logic across all route handlers that may need it.

# you going to have code that's going to relied upon by other code


# to create a token, in python terminal

# import secrets
# >>> secrets.token_hex(16)

# what is alembic
# what is sqlalchemy
# what is dunder method
# what is DI

# pip install alembic

# alembic init -t async migrations       # step -1 after installation
# alembic revision --autogenerate -m "init"
# alembic upgrade head 

# “My FastAPI app uses async MySQL (aiomysql), so create Alembic files that know how to talk to an async database.”

# Without -t async:                                                                     # With -t async:

# Alembic would try to use sync MySQL                                                   # Alembic uses async engine

# It would break with aiomysql                                                          # It works perfectly with your FastAPI setup
