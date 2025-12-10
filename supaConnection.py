import os
import typing
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# If env vars are missing OR still placeholders, use MOCK mode
MOCK_MODE = False
supabase: typing.Optional[Client] = None

if (
    not SUPABASE_URL
    or not SUPABASE_KEY
    or "your-project-id" in SUPABASE_URL
):
    MOCK_MODE = True
    print("[supaConnection] WARNING: Running in MOCK_MODE (no real Supabase).")
else:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    print("[supaConnection] Connected to Supabase project.")


# ----------------- MOCK DATA (used only when MOCK_MODE = True) -----------------

# Simple in-memory "tables"
MOCK_SERVICE_PROVIDERS = [
    {"spID": 1, "spName": "Fade Factory", "spPhoneNum": "555-111-1111", "bID": 1},
    {"spID": 2, "spName": "Clip & Clean", "spPhoneNum": "555-222-2222", "bID": 1},
]

MOCK_SERVICES = [
    {"sID": 1, "type": "Haircut", "duration": 30, "price": 25.0},
    {"sID": 2, "type": "Beard Trim", "duration": 20, "price": 15.0},
    {"sID": 3, "type": "Haircut + Beard", "duration": 45, "price": 35.0},
]

MOCK_CLIENTS = []         # will store dicts with cID, cFName, cLName, cPhone
MOCK_APPOINTMENTS = []    # will store dicts with aID, cID, spID, sID, date, timeSlot, paymentMethod

CLIENT_ID_COUNTER = 1
APPOINTMENT_ID_COUNTER = 1


# ----------------- READ HELPERS -----------------


def get_service_providers():
    """
    Get all barbers / service providers.
    Real DB: ServiceProvider table
    Mock: returns MOCK_SERVICE_PROVIDERS
    """
    if MOCK_MODE:
        return list(MOCK_SERVICE_PROVIDERS)

    resp = (
        supabase.table("ServiceProvider")
        .select("spID, spName, spPhoneNum, bID")
        .execute()
    )
    return resp.data or []


def get_services():
    """
    Get all services.
    Real DB: Services table
    Mock: returns MOCK_SERVICES
    """
    if MOCK_MODE:
        return list(MOCK_SERVICES)

    resp = (
        supabase.table("Services")
        .select("sID, type, duration, price")
        .execute()
    )
    return resp.data or []


def get_upcoming_appointments(limit: int = 20):
    """
    Get appointments (for an admin/demo page).
    Real DB: Appointment table
    Mock: returns recent MOCK_APPOINTMENTS
    """
    if MOCK_MODE:
        # Just return the last `limit` appointments
        return MOCK_APPOINTMENTS[-limit:]

    resp = (
        supabase.table("Appointment")
        .select("aID, cID, spID, sID, date, timeSlot, paymentMethod")
        .order("date", desc=False)
        .order("timeSlot", desc=False)
        .limit(limit)
        .execute()
    )
    return resp.data or []


# ----------------- WRITE HELPERS -----------------


def create_client(first_name: str, last_name: str, phone: typing.Optional[str] = None):
    """
    Insert a new client row and return the created record (including cID).
    Real DB: Client table
    Mock: append to MOCK_CLIENTS
    """
    global CLIENT_ID_COUNTER

    if MOCK_MODE:
        global MOCK_CLIENTS
        c_id = CLIENT_ID_COUNTER
        CLIENT_ID_COUNTER += 1

        row = {
            "cID": c_id,
            "cFName": first_name,
            "cLName": last_name,
            "cPhone": phone,
        }
        MOCK_CLIENTS.append(row)
        return row

    payload = {
        "cFName": first_name,
        "cLName": last_name,
        "cPhone": phone,
    }

    resp = supabase.table("Client").insert(payload).execute()
    if not resp.data:
        raise RuntimeError("Failed to insert client")
    return resp.data[0]  # should contain cID


def create_appointment(
    c_id: str,
    sp_id: str,
    s_id: str,
    date_str: str,
    time_slot: str,
    payment_method: typing.Optional[str] = None,
):
    """
    Insert a new appointment row.
    Real DB: Appointment table
    Mock: append to MOCK_APPOINTMENTS
    """
    global APPOINTMENT_ID_COUNTER

    if MOCK_MODE:
        global MOCK_APPOINTMENTS
        a_id = APPOINTMENT_ID_COUNTER
        APPOINTMENT_ID_COUNTER += 1

        row = {
            "aID": a_id,
            "cID": c_id,
            "spID": sp_id,
            "sID": s_id,
            "date": date_str,
            "timeSlot": time_slot,
            "paymentMethod": payment_method,
        }
        MOCK_APPOINTMENTS.append(row)
        return row

    payload = {
        "cID": c_id,
        "spID": sp_id,
        "sID": s_id,
        "date": date_str,
        "timeSlot": time_slot,
        "paymentMethod": payment_method,
    }

    resp = supabase.table("Appointment").insert(payload).execute()
    if not resp.data:
        raise RuntimeError("Failed to insert appointment")
    return resp.data[0]

