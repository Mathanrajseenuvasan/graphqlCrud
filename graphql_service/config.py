# Imports
from flask_sqlalchemy import SQLAlchemy
from graphql_service import app
from flask_migrate import Migrate


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/graphql'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
