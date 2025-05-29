from pydantic import BaseModel
from typing import List

# User details from API response
class UserDTO(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str

    # Technical challenge defined firstName and lastName as being required, so let's
    # implement using @property
    @property
    def firstName(self):
        return self.first_name
    
    @property
    def lastName(self):
        return self.last_name   

# Not used
class SupportDTO(BaseModel):
    url: str
    text: str

# API response details with metadata and users
class ApiResponseDTO(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserDTO]
    support: SupportDTO