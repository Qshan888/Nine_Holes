from app import app, db
from models.golf_data import golfs_list, comments_list, categories_list
from models.user_data import user_list


with app.app_context():
    # ! Try/catch in python is try/except
    try:
        print('Recreating database..')
        db.drop_all()  # ! Removing everything from the DB
        db.create_all()  # ! This will create the TABLES in the database.

        db.session.add_all(user_list)
        db.session.commit()

        db.session.add_all(golfs_list)
        db.session.commit()

        print("seeding our database..")

        # ! This has to come after making teas. Because you need teas to comment on.

        db.session.add_all(comments_list)
        db.session.commit()


        print("bye 👋")
    except Exception as e:
        print(e)
