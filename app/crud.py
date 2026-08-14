from sqlalchemy.orm import Session
from .models import MasterCategory
from .schemas import MasterCategoryCreate


# CREATE
def create_category(
    db: Session,
    category: MasterCategoryCreate
):

    new_category = MasterCategory( MasterCategoryName=category.MasterCategoryName)

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


# READ ALL
def get_categories(db: Session):

    return db.query(MasterCategory).all()


# READ BY ID
def get_category(
    db: Session,
    category_id: int
):

    return db.query(MasterCategory).filter(MasterCategory.MasterCategoryId == category_id).first()


# UPDATE
def update_category(
    db: Session,
    category_id: int,
    category: MasterCategoryCreate
):

    existing_category = db.query(MasterCategory).filter( MasterCategory.MasterCategoryId == category_id).first()

    if existing_category:

        existing_category.MasterCategoryName = ( category.MasterCategoryName)

        db.commit()
        db.refresh(existing_category)

    return existing_category


# DELETE
def delete_category(
    db: Session,
    category_id: int
):

    existing_category = db.query(MasterCategory).filter( MasterCategory.MasterCategoryId == category_id).first()

    if existing_category:

        db.delete(existing_category)
        db.commit()

        return True

    return False