# utils.py
from cryptography.fernet import Fernet
import random


from myapp.models import projectTable
from api.models import (History)

def get_project_list():
    projects_list = []
    try:
        # Fetch data with related fields
        project_data = projectTable.objects.select_related(
            'project__location', 
            'project__sub_area', 
            'project__property_type', 
            'project__category', 
            'project__sub_category', 
            'project__website', 
            'project__publisher'
        ).all()

        for project in project_data:
            # Debug: Print project to see what data is being fetched
            print(f"Fetching data for project ID: {project.id}")

            project_details = {
                "id": project.project.id if project.project else None,
                "name": project.project.name if project.project else None,
                "description": project.project.description if project.project else None,
                "picture": project.project.picture.url if project.project and project.project.picture else None,
                "view": project.project.view if project.project else None,
                "is_verified": project.project.is_verified if project.project else None,
                "is_for_rent": project.project.is_for_rent if project.project else None,
                "title": project.project.title if project.project else None,
                "country": project.project.location.country if project.project and project.project.location else None,
                "state": project.project.location.state if project.project and project.project.location else None,
                "dist": project.project.location.dist if project.project and project.project.location else None,
                "city": project.project.location.city if project.project and project.project.location else None,
                "longitude": project.project.location.longitude if project.project and project.project.location else None,
                "latitude": project.project.location.latitude if project.project and project.project.location else None,
                "sub_area": project.project.sub_area.name if project.project and project.project.sub_area else None,
                "property_type": project.project.property_type.name if project.project and project.project.property_type else None,
                "category": project.project.category.name if project.project and project.project.category else None,
                "sub_category": project.project.sub_category.name if project.project and project.project.sub_category else None,
                "website": project.project.website.name if project.project and project.project.website else None,
                "amenities": project.project.amenities if project.project else None,
                "nearby": project.project.nearby if project.project else None,
                "expiration_date": project.project.expiration_date if project.project else None,
                "construction_status": project.project.construction_status if project.project else None,
                "status": project.project.status if project.project else None,
                "furnished": project.project.furnished if project.project else None,
                "security_deposit": project.project.security_deposit if project.project else None,
                "rent_property": project.project.rent_property if project.project else None,
                "rent_escalation_period": project.project.rent_escalation_period if project.project else None,
                "rent_priority_comment": project.project.rent_priority_comment if project.project else None,
                "size": project.project.size if project.project else None,
                "carpet_area": project.project.carpet_area if project.project else None,
                "type": project.project.type if project.project else None,
                "builder": project.project.builder if project.project else None,
                "floor": project.project.floor if project.project else None,
                "total_floor": project.project.total_floor if project.project else None,
                "facing": project.project.facing if project.project else None,
                "possession_type": project.project.possession_type if project.project else None,
                "is_rented": project.project.is_rented if project.project else None,
                "rent": project.project.rent if project.project else None,
                "cost": project.project.cost if project.project else None,
                "extra_charge": project.project.extra_charge if project.project else None,
                "lease_time": project.project.lease_time if project.project else None,
                "lease_completed": project.project.lease_completed if project.project else None,
                "lease_balance": project.project.lease_balance if project.project else None,
                "rent_escalation": project.project.rent_escalation if project.project else None,
                "rent_to": project.project.rent_to if project.project else None,
                "maintenance": project.project.maintenance if project.project else None,
                "registry": project.project.registry if project.project else None,
                "transfer_charge": project.project.transfer_charge if project.project else None,
                "gst": project.project.gst if project.project else None,
                "profit_sharing": project.project.profit_sharing if project.project else None,
                "roi": project.project.roi if project.project else None,
                "profile_pic": project.project.profile_pic if project.project else None,
                "shop_for": project.project.shop_for if project.project else None,
                "posted_by": project.project.posted_by if project.project else None,
                "possession_status": project.project.possession_status if project.project else None,
                "possession_date": project.project.possession_date if project.project else None,
                "is_corner_plot": project.project.is_corner_plot if project.project else None,
                "hidden_notes": project.project.hidden_notes if project.project else None,
                "lock_in": project.project.lock_in if project.project else None,
                "power_breakup_rate": project.project.power_breakup_rate if project.project else None,
                "road_size": project.project.road_size if project.project else None,
                "publisher": project.project.publisher.name if project.project and project.project.publisher else None,
                "meta_desc": project.project.meta_desc if project.project else None,
                "meta_key": project.project.meta_key if project.project else None,
                "is_distress": project.project.is_distress if project.project else None,
                "reason_distress": project.project.reason_distress if project.project else None,
                "cost_distress": project.project.cost_distress if project.project else None,
                "recommended": project.project.recommended if project.project else None,
                "plot_size": project.project.plot_size if project.project else None,
                "construction_age": project.project.construction_age if project.project else None,
                "code": project.project.code if project.project else None,
                "listing_date": project.project.listing_date if project.project else None,
                "slug": project.project.slug if project.project else None,
                "price": project.price if project else None,
                "locality": project.locality if project else None,
                "topology": project.topology if project else None,
                "location": project.project.location if project.project else None,
                "neighbourhood": project.neighbourhood if project else None,
                "master_plan": project.master_plan.url if project.master_plan else None,
                "unit_plan": project.unit_plan.url if project.unit_plan else None,
                "image": project.image.url if project.image else None,
                "image2": project.image2.url if project.image2 else None,
                "image3": project.image3.url if project.image3 else None,
                "image4": project.image4.url if project.image4 else None,
            }
            
            projects_list.append(project_details)
        
    except Exception as e:
        print(f"Error fetching project data: {e}")

    return projects_list



def sendOtp(email):
    otp = random.randint(100000, 999999)
    return otp

def log_history(action, model_name, record_id, description=None):
    History.objects.create(
        action=action,
        model_name=model_name,
        record_id=record_id,
        description=description
    )
