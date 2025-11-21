"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Dental lead capture schema
class Lead(BaseModel):
    """
    Dental practice marketing leads
    Collection name: "lead"
    """
    full_name: str = Field(..., description="Prospective patient full name")
    phone: str = Field(..., description="Phone number")
    email: Optional[EmailStr] = Field(None, description="Email address")
    service: Optional[str] = Field(None, description="Interested service e.g., Cleaning, Whitening, Implants")
    preferred_date: Optional[str] = Field(None, description="Preferred appointment date (string)")
    preferred_time: Optional[str] = Field(None, description="Preferred appointment time (string)")
    message: Optional[str] = Field(None, description="Additional message or symptoms")
    source: Optional[str] = Field(None, description="Lead source or campaign")
    utm_source: Optional[str] = Field(None)
    utm_medium: Optional[str] = Field(None)
    utm_campaign: Optional[str] = Field(None)
    consent: bool = Field(True, description="Consent to be contacted")

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
