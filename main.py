from flask import Flask, render_template, request, redirect, url_for, flash
from supaConnection import (
    get_service_providers,
    get_services,
    get_upcoming_appointments,
    create_client,
    create_appointment,
    MOCK_MODE,
    MOCK_CLIENTS,
)

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # change if you want


# ---------- ROUTES ----------
@app.route("/")
def index():
    """
    Home page:
    - Show available barbers (ServiceProvider)
    - Show some popular services (Services)
    """
    service_providers = get_service_providers()
    services = get_services()
    popular_services = services[:3] if services else []

    return render_template(
        "index.html",
        service_providers=service_providers,
        services=services,
        popular_services=popular_services,
    )

@app.route("/booking", methods=["GET", "POST"])
def booking():
    """
    Booking page:
    - GET: render form
    - POST: create client + appointment
    """
    if request.method == "POST":
        full_name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        sp_id = request.form.get("service_provider")
        s_id = request.form.get("service")
        date = request.form.get("date")
        time_slot = request.form.get("time")
        payment_method = request.form.get("payment_method")

        if not (full_name and sp_id and s_id and date and time_slot):
            flash("Please fill all required fields.", "error")
            return redirect(url_for("booking"))

        parts = full_name.split()
        first_name = parts[0]
        last_name = " ".join(parts[1:]) if len(parts) > 1 else "Unknown"

        try:
            client_row = create_client(first_name, last_name, phone)
            c_id = client_row["cID"]

            create_appointment(
                c_id=c_id,
                sp_id=sp_id,
                s_id=s_id,
                date_str=date,
                time_slot=time_slot,
                payment_method=payment_method,
            )
            flash("Booking complete!", "success")

        except Exception as e:
            print("Error booking appointment:", e)
            flash("There was a problem saving your booking.", "error")
            return redirect(url_for("booking"))

        # REDIRECT LOGIC — clean indentation
        if request.form.get("from_home") == "1":
            return redirect(url_for("appointments"))
        else:
            return redirect(url_for("booking"))

    # ---------- GET ----------
    service_providers = get_service_providers()
    services = get_services()
    selected_sp_id = request.args.get("spID")
    selected_sp = None

    if selected_sp_id:
        for sp in service_providers:
            if str(sp["spID"]) == str(selected_sp_id):
                selected_sp = sp
                break

    return render_template(
        "booking.html",
        service_providers=service_providers,
        services=services,
        selected_sp_id=selected_sp_id,
        selected_sp=selected_sp,
    )

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/policies")
def policies():
    return render_template("policies.html")

@app.route("/appointments")
def appointments():
    appts = get_upcoming_appointments()
    service_providers = get_service_providers()
    services = get_services()
    clients = MOCK_CLIENTS if MOCK_MODE else []

    # Lookup maps
    sp_map = {str(sp["spID"]): sp for sp in service_providers}
    svc_map = {str(s["sID"]): s for s in services}
    client_map = {str(c["cID"]): c for c in clients}

    enriched = []
    for a in appts:
        sp_id = str(a.get("spID"))
        s_id = str(a.get("sID"))
        c_id = str(a.get("cID"))

        sp = sp_map.get(sp_id)
        svc = svc_map.get(s_id)
        client = client_map.get(c_id)

        row = dict(a)

        # Barber name
        row["barber_name"] = sp["spName"] if sp else f"Barber #{sp_id}"

        # Service name
        if svc:
            row["service_name"] = f'{svc["type"]} ({svc["duration"]} min, ${svc["price"]:.2f})'
        else:
            row["service_name"] = f"Service #{s_id}"

        # Client name + phone
        if client:
            fn = client.get("cFName", "Unknown")
            ln = client.get("cLName", "")
            row["client_name"] = f"{fn} {ln}".strip()
            row["client_phone"] = client.get("cPhone", "—")
        else:
            row["client_name"] = f"Client #{c_id}"
            row["client_phone"] = "—"

        enriched.append(row)

    return render_template("appointments.html", appointments=enriched)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
