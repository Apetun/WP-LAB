from django.shortcuts import render

# Global vote counters (in-memory; not persistent)
GOOD_COUNT = 0
SATISFACTORY_COUNT = 0
BAD_COUNT = 0

def vote_view(request):
    global GOOD_COUNT, SATISFACTORY_COUNT, BAD_COUNT

    if request.method == 'POST':
        choice = request.POST.get('choice')
        if choice == 'Good':
            GOOD_COUNT += 1
        elif choice == 'Satisfactory':
            SATISFACTORY_COUNT += 1
        elif choice == 'Bad':
            BAD_COUNT += 1

        total_votes = GOOD_COUNT + SATISFACTORY_COUNT + BAD_COUNT

        if total_votes == 0:
            good_pct = sat_pct = bad_pct = 0
        else:
            good_pct = (GOOD_COUNT / total_votes) * 100
            sat_pct = (SATISFACTORY_COUNT / total_votes) * 100
            bad_pct = (BAD_COUNT / total_votes) * 100

        context = {
            'show_results': True,
            'good_pct': good_pct,
            'sat_pct': sat_pct,
            'bad_pct': bad_pct,
        }
        return render(request, 'vote.html', context)

    # GET request: simply show the voting form
    return render(request, 'vote.html')
