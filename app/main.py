from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import get_db
from .schemas import (
    MasterCategoryCreate,
    MasterCategoryResponse
)
from . import crud


app = FastAPI(
    title="MasterCategory FastAPI Project"
)


@app.get("/")
def home():

    return {
        "message": "FastAPI is working"
    }


@app.post("/categories",response_model=MasterCategoryResponse)
def create_category(
    category: MasterCategoryCreate,
    db: Session = Depends(get_db)
):

    return crud.create_category( db, category
    )


@app.get("/categories", response_model=list[MasterCategoryResponse])
def get_categories(
    db: Session = Depends(get_db)
):

    return crud.get_categories(db)


@app.get("/categories/{category_id}", response_model=MasterCategoryResponse)
def get_category(
    category_id: int,
    db: Session = Depends(get_db)
):

    category = crud.get_category(
        db,
        category_id
    )

    if category is None:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


@app.put("/categories/{category_id}", response_model=MasterCategoryResponse)
def update_category(
    category_id: int,
    category: MasterCategoryCreate,
    db: Session = Depends(get_db)
):

    updated_category = crud.update_category(
        db,
        category_id,
        category
    )

    if updated_category is None:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return updated_category


@app.delete( "/categories/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db)
):

    result = crud.delete_category(
        db,
        category_id
    )

    if not result:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return {
        "message": "Category deleted successfully"
    }