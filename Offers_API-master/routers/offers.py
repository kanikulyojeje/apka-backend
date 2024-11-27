from fastapi import APIRouter, HTTPException, Depends

from models.models import Offer
from routers.utils import get_collection, handle_error
from routers.auth import validate_api_key

router = APIRouter()


def get_offers_collection():
    OFFERS_COLLECTION_NAME = 'offers'
    return get_collection(OFFERS_COLLECTION_NAME)


@router.get("/offers/{offer_id}")
def get_offer_by_id(offer_id: str, user: dict = Depends(validate_api_key)):
    print(offer_id)
    try:
        doc = get_offers_collection().document(offer_id).get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Offer not found")
        return {"id": doc.id, **doc.to_dict()}
    except Exception as e:
        handle_error(e)


@router.delete("/offers/{offer_id}")
def delete_offer(offer_id: str, user: dict = Depends(validate_api_key)):
    try:
        doc_ref = get_offers_collection().document(offer_id)
        if not doc_ref.get().exists:
            raise HTTPException(status_code=404, detail="Offer not found")
        doc_ref.delete()
        return {"message": "Offer deleted successfully"}
    except Exception as e:
        handle_error(e)


@router.post("/offers")
def create_offer(offer: Offer, user: dict = Depends(validate_api_key)):
    try:
        doc_ref = get_offers_collection().document()
        doc_ref.set(offer)
        return {"message": "Offer created successfully", "id": doc_ref.id}
    except Exception as e:
        handle_error(e)


@router.get("/offers")
def list_offers(user: dict = Depends(validate_api_key)):
    try:
        return [{"id": doc.id, **doc.to_dict()} for doc in get_offers_collection().stream()]
    except Exception as e:
        handle_error(e)


