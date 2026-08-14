from pydantic import BaseModel


class MasterCategoryCreate(BaseModel):
    MasterCategoryName: str


class MasterCategoryResponse(BaseModel):
    MasterCategoryId: int
    MasterCategoryName: str

    class Config:
        from_attributes = True