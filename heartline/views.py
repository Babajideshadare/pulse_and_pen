from django.shortcuts import render
from django.http import Http404

FAKE_BP_ENTRIES = [
    {
        "id": 1,
        "date": "2025-02-01",
        "time": "08:30",
        "systolic": 120,
        "diastolic": 80,
        "pulse": 70,
        "note": "Morning reading, feeling calm.",
    },
    {
       "id": 2,
        "date": "2025-02-01",
        "time": "21:15",
        "systolic": 135,
        "diastolic": 85,
        "pulse": 76,
        "note": "Evening reading after a stressful day at work feeling.",  
    },
    {
         "id": 3,
        "date": "2025-02-02",
        "time": "09:05",
        "systolic": 118,
        "diastolic": 78,
        "pulse": 68,
        "note": "Slept well; light breakfast and short walk.",
    },
]

def home(request):
    """
    Week 1: Home page shows a list of sample BP entries.
    Later, this will query the BPEntry model filtered by request.user.
    """
    context = {"bp_entries" : FAKE_BP_ENTRIES}
    return render (request, "home.html", context)

def bp_detail(request, entry_id: int):
    """
    Week 1: Show details for a single fake BP entry.
    Later, this will fetch a BPEntry object from the database.
    """
    try:
        entry = next(e for e in FAKE_BP_ENTRIES if e["id"] == entry_id)
    except StopIteration:
        raise Http404("Blood pressure entry not found.")
    
    return render(request, "bp_detail.html", {"entry": entry})

















     
     